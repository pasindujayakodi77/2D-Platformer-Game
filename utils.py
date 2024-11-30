import pygame

def draw_text(surface, text, x, y, font_size=20):
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, (0, 0, 0))
    surface.blit(text_surface, (x, y))
