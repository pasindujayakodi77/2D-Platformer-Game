import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5
        self.jumping = False
        self.score = 0
        
        # Load images (replace with your actual image files)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 128, 255))  # Example color
        
        # Player's rectangle for collision detection
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        # Get keys pressed for player movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0
        
        # Jumping
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -12
            self.jumping = True

    def apply_gravity(self):
        if self.rect.y + self.height < 600:  # Limit to screen height
            self.vel_y += self.gravity
        else:
            self.vel_y = 0
            self.jumping = False
            self.rect.y = 600 - self.height  # Reset to ground level
    
    def update(self):
        self.move()
        self.apply_gravity()
        
        # Update player position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def increment_score(self):
        self.score += 10
