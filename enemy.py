import pygame

class Enemy:
    def __init__(self, x, y):
        self.width = 50
        self.height = 70
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = -3

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x <= 0 or self.rect.x >= 800 - self.width:  # Screen boundaries
            self.vel_x *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
