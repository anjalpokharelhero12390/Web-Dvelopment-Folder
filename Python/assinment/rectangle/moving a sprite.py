import pygame

pygame.init()
clock = pygame.time.Clock()
sprite1 = pygame.Rect(50, 50, 40, 40)    
sprite2 = pygame.Rect(150, 150, 40, 40)  
speed = 5
running = True
print("Sprite1 = Arrow keys | Sprite2 = W A S D")
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    # Sprite 2 (WASD)
    if keys[pygame.K_w]:
        sprite2.y -= speed
    if keys[pygame.K_s]:
        sprite2.y += speed
    if keys[pygame.K_a]:
        sprite2.x -= speed
    if keys[pygame.K_d]:
        sprite2.x += speed
    print(f"S1: {sprite1.topleft}  S2: {sprite2.topleft}", end="\r")
pygame.quit()
