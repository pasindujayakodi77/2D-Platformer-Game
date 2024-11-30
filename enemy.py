import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        self.vel_x = -3  # Enemies move left to right
        
        # Load images (replace with your actual image files)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Example color

        # Enemy's rectangle for collision detection
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, player_rect):
        # Simple enemy AI (move horizontally)
        self.rect.x += self.vel_x
        if self.rect.x < 0 or self.rect.x > 750:  # Wrap around
            self.vel_x = -self.vel_x

    def draw(self, surface):
        surface.blit(self.image, self.rect)
