import pygame
import sys

def draw_text(surface, text, x, y, size=30, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def pause_menu(screen, clock, fps):
    game_paused = True
    while game_paused:
        screen.fill((255, 255, 255))
        draw_text(screen, "Game Paused", 300, 250, size=50)
        draw_text(screen, "Press P to Resume", 280, 310)
        draw_text(screen, "Press Q to Quit", 290, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(fps)
