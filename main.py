import pygame 
import os
pygame.init()

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path


WIN_WIDTH = 900
WIN_HEIGHT = 600
FPS = 40

fon = pygame.image.load(file_path(r"images\fon2.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self ,x , y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite(450, 0, 100, 100, r"images\pngwing.com (6).png" )
enemy = GameSprite(450, 240, 70, 70, r"images\Peg-Leg_Pete.png" )
finish =  GameSprite(500, 405, 50, 35, r"images\crystal.png" )




level = 1
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.blit(fon, (0, 0))
        player.show()
        enemy.show()
        finish.show()


    clock.tick(FPS)
    pygame.display.update()