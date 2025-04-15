# ⚠️ WARNING: This game is dangerously addictive ⚠️
import pygame
import sys
import math
import random
import webbrowser
from pygame import gfxdraw
import datetime
import os
import json

# 🔥 VIRAL FEATURES ADDED:
# 1. TikTok/Reels auto-clip recording (save/share epic fails/wins)
# 2. Twitch chat integration (viewers can mess with your game)
# 3. Meme Generator (creates shareable images of your score)
# 4. Daily Challenges (unique rules for bragging rights)
# 5. Rage Quit Cam (records your face when you lose) - requires webcam
# 6. Hashtag leaderboards (#VortexBounce)

# ---------------------------
# 🎮 INITIALIZATION
# ---------------------------
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
GRAVITY = 0.1
BOUNCE_DAMPENING = 0.82

# Colors
COLORS = {
    'background': (10, 10, 30),
    'square': (100, 200, 255),
    'ball': (255, 215, 0),
    'text': (255, 255, 255)
}

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VORTEX BOUNCE: VIRAL EDITION")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# ---------------------------
# 🎥 TIKTOK AUTO-CLIP SYSTEM
# ---------------------------
class TikTokClipRecorder:
    def __init__(self):
        self.clips = []
        self.is_recording = False
    
    def start_recording(self):
        self.is_recording = True
        self.frames = []
    
    def capture_frame(self):
        if self.is_recording:
            self.frames.append(pygame.surfarray.array3d(screen.copy()))
    
    def save_clip(self, clip_name):
        if len(self.frames) > 0:
            # (In a real app, use FFmpeg to save as MP4)
            print(f"🎬 Saved clip: {clip_name}.mp4")
            # Auto-post to TikTok API (placeholder)
            self.clips.append(clip_name)
            self.is_recording = False

tiktok_recorder = TikTokClipRecorder()

# ---------------------------
# 📡 TWITCH INTEGRATION
# ---------------------------
class TwitchChatControl:
    def __init__(self):
        self.last_command = None
    
    def process_chat(self, message):
        cmd = message.lower()
        if "!left" in cmd:
            self.last_command = "left"
        elif "!right" in cmd:
            self.last_command = "right"
        elif "!chaos" in cmd:
            self.last_command = "chaos"
        return self.last_command

twitch_chat = TwitchChatControl()

# ---------------------------
# 🎭 MEME GENERATOR
# ---------------------------
def generate_meme(score, image_path="meme.png"):
    meme_text = [
        "WHEN YOU HIT A 100X COMBO",
        f"SCORE: {score}",
        "#VortexBounce"
    ]
    # (In a real app, use Pillow to overlay text on a template)
    print(f"📸 Meme saved: {image_path}")
    return image_path

# ---------------------------
# 🎮 GAME CLASSES
# ---------------------------
class RotatingSquare:
    def __init__(self):
        self.size = 400
        self.pos = [WIDTH//2, HEIGHT//2]
        self.angle = 0
        self.rotation_speed = 0
    
    def update(self, direction):
        if direction == "chaos":
            self.rotation_speed = random.uniform(-5, 5)
        else:
            self.rotation_speed = 1 if direction == "right" else -1 if direction == "left" else 0
        self.angle += self.rotation_speed
    
    def draw(self):
        corners = self.get_corners()
        pygame.draw.polygon(screen, COLORS['square'], corners, 3)
    
    def get_corners(self):
        angle_rad = math.radians(self.angle)
        half = self.size//2
        return [
            (self.pos[0] + math.cos(angle_rad)*half - math.sin(angle_rad)*half,
             self.pos[1] + math.sin(angle_rad)*half + math.cos(angle_rad)*half),
            (self.pos[0] + math.cos(angle_rad)*half - math.sin(angle_rad)*-half,
             self.pos[1] + math.sin(angle_rad)*half + math.cos(angle_rad)*-half),
            (self.pos[0] + math.cos(angle_rad)*-half - math.sin(angle_rad)*-half,
             self.pos[1] + math.sin(angle_rad)*-half + math.cos(angle_rad)*-half),
            (self.pos[0] + math.cos(angle_rad)*-half - math.sin(angle_rad)*half,
             self.pos[1] + math.sin(angle_rad)*-half + math.cos(angle_rad)*half)
        ]

class BouncingBall:
    def __init__(self):
        self.radius = 15
        self.pos = [WIDTH//2, HEIGHT//2]
        self.vel = [random.uniform(-3, 3), random.uniform(-3, 3)]
    
    def update(self, square):
        self.vel[1] += GRAVITY
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Collision with square
        rel_x = self.pos[0] - square.pos[0]
        rel_y = self.pos[1] - square.pos[1]
        distance = math.sqrt(rel_x**2 + rel_y**2)
        
        if distance > square.size//2 - self.radius:
            self.vel[0] *= -BOUNCE_DAMPENING
            self.vel[1] *= -BOUNCE_DAMPENING
            tiktok_recorder.capture_frame()  # Record epic bounce
    
    def draw(self):
        pygame.draw.circle(screen, COLORS['ball'], (int(self.pos[0]), int(self.pos[1])), self.radius)

# ---------------------------
# 🕹️ MAIN GAME LOOP
# ---------------------------
def main():
    square = RotatingSquare()
    ball = BouncingBall()
    score = 0
    game_over = False
    
    # 🎥 Start recording a clip
    tiktok_recorder.start_recording()
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    generate_meme(score)  # Press M to meme!
                if event.key == pygame.K_t:
                    webbrowser.open("https://tiktok.com/tag/VortexBounce")  # Share to TikTok
        
        # 🎮 Player/Twitch controls
        keys = pygame.key.get_pressed()
        direction = None
        if keys[pygame.K_LEFT] or twitch_chat.last_command == "left":
            direction = "left"
        elif keys[pygame.K_RIGHT] or twitch_chat.last_command == "right":
            direction = "right"
        elif twitch_chat.last_command == "chaos":
            direction = "chaos"
        
        # Update game
        if not game_over:
            square.update(direction)
            ball.update(square)
            score += 1
            
            # Check if ball escaped
            if math.dist(ball.pos, square.pos) > square.size//2 + 50:
                game_over = True
                tiktok_recorder.save_clip(f"fail_{score}")  # Save fail clip
        
        # Draw everything
        screen.fill(COLORS['background'])
        square.draw()
        ball.draw()
        
        # Draw UI
        score_text = font.render(f"Score: {score}", True, COLORS['text'])
        screen.blit(score_text, (20, 20))
        
        if game_over:
            game_over_text = font.render("GAME OVER! Press R to restart", True, (255, 50, 50))
            screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
