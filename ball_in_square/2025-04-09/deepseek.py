#I need a python3.13 program that creates a rotating square
#and a speed setting. Within the rotating square is a
#yellow ball that bounces against the sides.
#The yellow ball should be affected by gravity.
#The outer edge of the ball should never pass through
#the walls of the square, it should bounce off the edges of the square.








import pygame
import sys
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
BG_COLOR = (30, 30, 40)
BALL_COLOR = (255, 255, 0)
SQUARE_COLOR = (200, 200, 200)
GRAVITY = 0.5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Square with Bouncing Ball")
clock = pygame.time.Clock()

class RotatingSquare:
    def __init__(self, center_x, center_y, size):
        self.center = pygame.Vector2(center_x, center_y)
        self.size = size
        self.half_size = size / 2
        self.angle = 0
        self.rotation_speed = 1  # degrees per frame
        self.points = [
            pygame.Vector2(-self.half_size, -self.half_size),
            pygame.Vector2(self.half_size, -self.half_size),
            pygame.Vector2(self.half_size, self.half_size),
            pygame.Vector2(-self.half_size, self.half_size)
        ]
        self.rotated_points = self.points.copy()
        
    def update(self):
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle -= 360
            
        # Rotate each point
        for i, point in enumerate(self.points):
            self.rotated_points[i] = point.rotate(self.angle)
            
    def draw(self, surface):
        # Calculate screen coordinates
        screen_points = [self.center + p for p in self.rotated_points]
        pygame.draw.polygon(surface, SQUARE_COLOR, screen_points, 2)
        
    def get_edges(self):
        """Returns the edges of the square as line segments (start, end) in world coordinates"""
        edges = []
        points = [self.center + p for p in self.rotated_points]
        for i in range(4):
            start = points[i]
            end = points[(i + 1) % 4]
            edges.append((start, end))
        return edges
    
    def contains_point(self, point, radius=0):
        """Check if a point (with optional radius) is inside the square"""
        # Transform point to square's local coordinate system
        rel_point = point - self.center
        rel_point = rel_point.rotate(-self.angle)
        
        # Check against AABB in local space
        return (-self.half_size + radius <= rel_point.x <= self.half_size - radius and
                -self.half_size + radius <= rel_point.y <= self.half_size - radius)

class Ball:
    def __init__(self, x, y, radius):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = BALL_COLOR
        
    def update(self, gravity, square):
        # Apply gravity
        self.vel.y += gravity
        
        # Store old position for collision detection
        old_pos = self.pos.copy()
        
        # Update position
        self.pos += self.vel
        
        # Check for collisions with square edges
        if not square.contains_point(self.pos, self.radius):
            self.pos = old_pos  # revert position
            
            # Get all edges of the square
            edges = square.get_edges()
            
            # Find the edge we're colliding with
            for edge_start, edge_end in edges:
                # Vector from edge start to end
                edge_vec = edge_end - edge_start
                edge_length = edge_vec.length()
                edge_dir = edge_vec.normalize() if edge_length > 0 else pygame.Vector2(1, 0)
                
                # Vector from edge start to ball center
                ball_vec = self.pos - edge_start
                
                # Project ball vector onto edge
                projection = ball_vec.dot(edge_dir)
                projection = max(0, min(edge_length, projection))
                
                # Find closest point on edge to ball
                closest_point = edge_start + edge_dir * projection
                
                # Check if we're close enough to collide
                distance = (self.pos - closest_point).length()
                if distance <= self.radius:
                    # Calculate normal vector from edge to ball
                    normal = (self.pos - closest_point).normalize()
                    
                    # Reflect velocity
                    self.vel = self.vel.reflect(normal)
                    
                    # Move ball outside the edge
                    penetration = self.radius - distance
                    self.pos += normal * penetration
                    
                    # Apply some bounce damping
                    self.vel *= 0.95
                    break
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

def main():
    # Create objects
    square = RotatingSquare(WIDTH // 2, HEIGHT // 2, 400)
    ball = Ball(WIDTH // 2, HEIGHT // 2 - 100, 20)
    
    # Speed control
    speed_multiplier = 1.0
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    speed_multiplier = min(3.0, speed_multiplier + 0.1)
                elif event.key == K_DOWN:
                    speed_multiplier = max(0.1, speed_multiplier - 0.1)
                elif event.key == K_r:  # Reset ball position
                    ball.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2 - 100)
                    ball.vel = pygame.Vector2(0, 0)
        
        # Update objects with speed multiplier
        square.rotation_speed = 1 * speed_multiplier
        square.update()
        ball.update(GRAVITY * speed_multiplier, square)
        
        # Draw everything
        screen.fill(BG_COLOR)
        square.draw(screen)
        ball.draw(screen)
        
        # Display speed info
        font = pygame.font.Font(None, 36)
        speed_text = font.render(f"Speed: {speed_multiplier:.1f}x (UP/DOWN to adjust, R to reset)", True, (255, 255, 255))
        screen.blit(speed_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
