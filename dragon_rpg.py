import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragon Gem Quest - Year 300")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load or create sprites (using placeholders if no image files)
def load_sprite(color, width, height):
    sprite = pygame.Surface((width, height))
    sprite.fill(color)
    return sprite

# Detailed sprite creation
player_sprite = load_sprite(BLUE, TILE_SIZE, TILE_SIZE)  # Blue square for player
dragon_sprite = load_sprite(RED, TILE_SIZE, TILE_SIZE)    # Red dragon with scales
blob_sprite = load_sprite(GREEN, TILE_SIZE, TILE_SIZE)    # Green blob with gooey texture
gem_sprite = load_sprite(WHITE, 10, 10)                  # Small white gem

# If you have image files, replace load_sprite with:
# player_sprite = pygame.image.load("player.png").convert_alpha()
# dragon_sprite = pygame.image.load("dragon.png").convert_alpha()
# blob_sprite = pygame.image.load("blob.png").convert_alpha()
# gem_sprite = pygame.image.load("gem.png").convert_alpha()

# Game entities
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gems = 0
        self.stones = []
        self.stone_cycle = ["Fire Stone", "Water Stone", "Earth Stone", 
                           "Air Stone", "Light Stone", "Dark Stone", 
                           "Void Stone", "Star Stone", "Moon Stone"]

    def move(self, dx, dy):
        new_x = self.x + dx * TILE_SIZE
        new_y = self.y + dy * TILE_SIZE
        if 0 <= new_x < SCREEN_WIDTH - TILE_SIZE and 0 <= new_y < SCREEN_HEIGHT - TILE_SIZE:
            self.x = new_x
            self.y = new_y

    def collect_gems(self, amount):
        self.gems += amount
        while self.gems >= 24 and len(self.stones) < len(self.stone_cycle):
            self.gems -= 24
            self.stones.append(self.stone_cycle[len(self.stones)])

    def draw(self):
        screen.blit(player_sprite, (self.x, self.y))

class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.type = enemy_type  # "dragon" or "blob"
        self.alive = True

    def draw(self):
        if self.alive:
            sprite = dragon_sprite if self.type == "dragon" else blob_sprite
            screen.blit(sprite, (self.x, self.y))

# Initialize game objects
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
enemies = []
for _ in range(5):
    x = random.randrange(0, SCREEN_WIDTH - TILE_SIZE, TILE_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE)
    enemy_type = random.choice(["dragon", "blob"])
    enemies.append(Enemy(x, y, enemy_type))

# Font for displaying gems and stones
font = pygame.font.SysFont("arial", 24)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
            elif event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)

    # Check for collisions
    player_rect = pygame.Rect(player.x, player.y, TILE_SIZE, TILE_SIZE)
    for enemy in enemies:
        if enemy.alive:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, TILE_SIZE, TILE_SIZE)
            if player_rect.colliderect(enemy_rect):
                enemy.alive = False
                gems_dropped = 2 if enemy.type == "dragon" else 4
                player.collect_gems(gems_dropped)
                # Respawn enemy
                x = random.randrange(0, SCREEN_WIDTH - TILE_SIZE, TILE_SIZE)
                y = random.randrange(0, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE)
                enemy_type = random.choice(["dragon", "blob"])
                enemies.append(Enemy(x, y, enemy_type))
                enemies.remove(enemy)
                break

    # Draw everything
    screen.fill(BLACK)
    player.draw()
    for enemy in enemies:
        enemy.draw()

    # Display gems and stones
    gem_text = font.render(f"Gems: {player.gems}", True, WHITE)
    screen.blit(gem_text, (SCREEN_WIDTH - 150, 10))
    for i, stone in enumerate(player.stones):
        stone_text = font.render(f"{stone}", True, WHITE)
        screen.blit(stone_text, (SCREEN_WIDTH - 150, 40 + i * 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
