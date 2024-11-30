import pygame

class Level:
    def __init__(self):
        self.platforms = []
        self.create_level()

    def create_level(self):
        # Example platform positions
        self.platforms.append(pygame.Rect(100, 550, 200, 20))  # Platform 1
        self.platforms.append(pygame.Rect(400, 400, 250, 20))  # Platform 2
        self.platforms.append(pygame.Rect(700, 300, 200, 20))  # Platform 3

    def draw(self, surface):
        # Draw platforms
        for platform in self.platforms:
            pygame.draw.rect(surface, (0, 255, 0), platform)
