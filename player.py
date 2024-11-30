import pygame

class Player:
    def __init__(self, x, y):
        self.width = 50
        self.height = 70
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5
        self.jumping = False
        self.health = 3

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0

        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -12
            self.jumping = True

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.rect.y + self.height >= 600:  # Ground level
            self.vel_y = 0
            self.jumping = False
            self.rect.y = 600 - self.height

    def update(self, platforms):
        self.move()
        self.apply_gravity()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Platform collision
        for platform in platforms:
            if self.rect.colliderect(platform) and self.vel_y > 0:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.jumping = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def take_damage(self):
        self.health -= 1
