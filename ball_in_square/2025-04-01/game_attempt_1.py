import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Square properties
square_size = 300
square_pos = [WIDTH // 2, HEIGHT // 2]
square_angle = 0
rotation_speed = 0.5  # degrees per frame

# Ball properties
ball_radius = 20
ball_color = YELLOW
ball_pos = [square_pos[0], square_pos[1]]
ball_velocity = [3, 3.5]  # x and y velocity

# Main game loop
clock = pygame.time.Clock()

def get_rotated_square_corners(pos, size, angle):
    """Calculate the positions of the square's corners after rotation"""
    angle_rad = math.radians(angle)
    half_size = size // 2
    corners = [
        (-half_size, -half_size),
        (half_size, -half_size),
        (half_size, half_size),
        (-half_size, half_size)
    ]
    
    rotated_corners = []
    for x, y in corners:
        # Apply rotation
        new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
        new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
        # Translate to screen position
        rotated_corners.append((pos[0] + new_x, pos[1] + new_y))
    
    return rotated_corners

def point_in_rotated_square(point, square_center, size, angle):
    """Check if a point is inside the rotated square"""
    angle_rad = -math.radians(angle)  # Inverse rotation
    half_size = size / 2
    
    # Translate point to square's coordinate system
    tx = point[0] - square_center[0]
    ty = point[1] - square_center[1]
    
    # Rotate point back to align with axis-aligned square
    rx = tx * math.cos(angle_rad) - ty * math.sin(angle_rad)
    ry = tx * math.sin(angle_rad) + ty * math.cos(angle_rad)
    
    # Check if point is within the axis-aligned square
    return -half_size <= rx <= half_size and -half_size <= ry <= half_size

def check_collision(ball_pos, ball_radius, square_center, square_size, square_angle):
    """Check if ball is colliding with the square's edges"""
    angle_rad = -math.radians(square_angle)
    half_size = square_size / 2
    
    # Translate ball position to square's coordinate system
    tx = ball_pos[0] - square_center[0]
    ty = ball_pos[1] - square_center[1]
    
    # Rotate ball position back to align with axis-aligned square
    rx = tx * math.cos(angle_rad) - ty * math.sin(angle_rad)
    ry = tx * math.sin(angle_rad) + ty * math.cos(angle_rad)
    
    # Check collision with each edge
    if abs(rx) + ball_radius > half_size or abs(ry) + ball_radius > half_size:
        # Determine which edge was hit
        if abs(rx) + ball_radius > half_size and abs(ry) + ball_radius > half_size:
            # Corner collision (reverse both velocities)
            return (-1, -1)
        elif abs(rx) + ball_radius > half_size:
            # Vertical edge collision (reverse x velocity)
            return (-1, 1)
        else:
            # Horizontal edge collision (reverse y velocity)
            return (1, -1)
    return (1, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Update rotation angle
    square_angle += rotation_speed
    if square_angle >= 360:
        square_angle = 0
    
    # Get rotated square corners
    corners = get_rotated_square_corners(square_pos, square_size, square_angle)
    
    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]
    
    # Check for collisions with square edges
    collision_factors = check_collision(ball_pos, ball_radius, square_pos, square_size, square_angle)
    ball_velocity[0] *= collision_factors[0]
    ball_velocity[1] *= collision_factors[1]
    
    # Draw the rotated square
    pygame.draw.polygon(screen, WHITE, corners, 2)
    
    # Draw the yellow ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
