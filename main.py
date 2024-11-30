import pygame
import sys
from random import randint
from player import Player
from enemy import Enemy
from level import Level
from utils import draw_text, pause_menu

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced 2D Platformer")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Frame rate
FPS = 60

# Game variables
game_paused = False
game_over = False
score = 0

# Initialize game objects
player = Player(100, 500)
enemies = [Enemy(500, 500), Enemy(600, 400)]
level = Level()
power_up = pygame.Rect(randint(50, 750), randint(50, 550), 30, 30)  # Random power-up location

# Game clock
clock = pygame.time.Clock()

# Main game loop
def main():
    global game_paused, game_over, score

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause the game
                    game_paused = True
                    pause_menu(screen, clock, FPS)  # Pause menu handling
                if event.key == pygame.K_r and game_over:  # Restart the game
                    restart_game()

        if not game_over:
            # Game logic
            update_game()
        else:
            # Display game over screen
            display_game_over()

        # Update the display and maintain FPS
        pygame.display.flip()
        clock.tick(FPS)

def update_game():
    """Update all game elements."""
    global score, power_up

    screen.fill(WHITE)
    
    # Update player and enemy logic
    player.update(level.platforms)
    for enemy in enemies:
        enemy.update()
        if player.rect.colliderect(enemy.rect):  # Collision with enemies
            player.take_damage()
            if player.health <= 0:
                end_game()

    # Collision with power-up
    if player.rect.colliderect(power_up):
        score += 10
        relocate_power_up()

    # Draw everything
    level.draw(screen)
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    pygame.draw.rect(screen, YELLOW, power_up)  # Draw power-up
    draw_text(screen, f"Score: {score}", 10, 10)
    draw_text(screen, f"Health: {player.health}", 10, 40)

def end_game():
    """Handle game over logic."""
    global game_over
    game_over = True

def display_game_over():
    """Display game over screen."""
    screen.fill(WHITE)
    draw_text(screen, "Game Over", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, size=50)
    draw_text(screen, f"Final Score: {score}", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10)
    draw_text(screen, "Press R to Restart", SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50)

def relocate_power_up():
    """Relocate the power-up to a new random position."""
    power_up.x = randint(50, SCREEN_WIDTH - 50)
    power_up.y = randint(50, SCREEN_HEIGHT - 50)

def restart_game():
    """Restart the game with initial settings."""
    global game_over, score
    game_over = False
    score = 0
    player.health = 3
    relocate_power_up()

if __name__ == "__main__":
    main()
