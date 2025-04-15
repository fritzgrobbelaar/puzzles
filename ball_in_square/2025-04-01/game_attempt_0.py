import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Square with Yellow Ball")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Square properties
square_size = 200
square_pos = [WIDTH // 2, HEIGHT // 2]
square_angle = 0
rotation_speed = 0.5  # degrees per frame

# Ball properties
ball_radius = 30
ball_color = YELLOW

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
    
    # Draw the rotated square
    pygame.draw.polygon(screen, WHITE, corners, 2)
    
    # Draw the yellow ball (always centered)
    pygame.draw.circle(screen, ball_color, square_pos, ball_radius)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()

