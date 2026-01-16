import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rectangle")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 0, 0))         
    pygame.draw.rect(screen, (255, 255, 255), (120, 100, 160, 80))  # rectangle
    pygame.display.update()
pygame.quit()
