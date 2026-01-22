import pygame
import random
SCREEN_WIDTH , SCREEN_HEIGHT  = 500 , 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.jpg") , (SCREEN_WIDTH , SCREEN_HEIGHT))
font = pygame.font.SysFont("Times new roman" , FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self , color , height , width):
        super().__init__()
        self.image = pygame.Surface([height , width])
        self.image.fill(pygame.Color('dogerblue'))
        pygame.draw.rect(self.image , color , pygame.Rect(0 , 0 , height , width))
        self.rect =self.image.get_rect()
    def move(X_change,Y_change):
        self.rect.x = max(min(self.rect.x + X_change , SCREEN_WIDTH - self.rect.width) , 0)
        self.rect.y = max(min(self.rect.y + Y_change , SCREEN_HEIGHT - self.rect.height) , 0)
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('black') , 20 , 30)
sprite1.rect.x,sprite1.rect.y = random.randint( 0 , SCREEN_WIDTH - sprite1 .rect.width ) , random.randint(0 , SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color('red'), 20 , 30)
sprite2.rect.x,sprite2.rect.y = random.randint( 0 , SCREEN_WIDTH - sprite2 .rect.width ) , random.randint(0 , SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
all_sprites.add(sprite2)
running , won = True , False
clock = pygame.time.Clock()
while running :
    for event in pygame,event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won :
          

