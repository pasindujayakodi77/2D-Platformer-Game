import pygame
import sys
from player import Player
from enemy import Enemy
from level import Level
from utils import draw_text

# Initialize pygame and set up the screen dimensions
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Advanced 2D Platformer")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game clock and frame rate
clock = pygame.time.Clock()
FPS = 60

# Create player, enemies, and level objects
player = Player(100, 500)
level = Level()
enemies = [Enemy(500, 500), Enemy(600, 400)]  # Example enemies

def main_game_loop():
    # Game loop
    while True:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update game objects
        player.update()
        for enemy in enemies:
            enemy.update(player.rect)
        
        # Draw everything
        level.draw(screen)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Display score
        draw_text(screen, f"Score: {player.score}", 20, 20, font_size=30)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_game_loop()
