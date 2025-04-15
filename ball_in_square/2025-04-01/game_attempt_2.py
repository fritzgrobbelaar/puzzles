import pygame
import math

class VortexGame:
    def __init__(self):
        self.square_size = 400
        self.square_pos = [400, 400]
        self.square_angle = 0
        self.ball_pos = [400, 400]
        self.ball_vel = [3, 3.5]
        self.ball_radius = 20
        self.score = 0
        self.game_over = False

    def update_physics(self):
        """Testable physics update without Pygame dependencies"""
        # Rotate square
        self.square_angle = (self.square_angle + 1) % 360
        
        # Move ball
        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]
        
        # Check boundary collisions
        buffer = self.ball_radius + 5
        if not (buffer <= self.ball_pos[0] <= 800 - buffer):
            self.ball_vel[0] *= -0.8
            self.score += 10
        if not (buffer <= self.ball_pos[1] <= 800 - buffer):
            self.ball_vel[1] *= -0.8
            self.score += 10

    def check_game_over(self):
        """Testable game over condition"""
        distance = math.dist(self.ball_pos, self.square_pos)
        self.game_over = distance > self.square_size // 2 + 100
        return self.game_over

