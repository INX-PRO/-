#Создай собственный Шутер!

from pygame import *
from random import*
font.init()
window =  display.set_mode((700,500))
display.set_caption("пинпонг")
background = transform.scale(image.load('galaxy.jpg'),(700,500))

sprite1 = transform.scale(image.load('l.png'),(100,100))

win_height = 500
win_width = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

while game:
    
        



        clock.tick(FPS)
        display.update()