import pygame

class Level:
    def __init__(self):
        self.platforms = []
        self.create_level()

    def create_level(self):
        self.platforms = [
            pygame.Rect(100, 500, 200, 20),
            pygame.Rect(400, 400, 250, 20),
            pygame.Rect(700, 300, 150, 20),
        ]

    def draw(self, surface):
        for platform in self.platforms:
            pygame.draw.rect(surface, (0, 255, 0), platform)
