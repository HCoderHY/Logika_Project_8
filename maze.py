from pygame import *
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
win_width = 700
win_height = 500
windows = display.set_mode((win_width,win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"),(win_width,win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        windows.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 0
    def update(self):
        if self.rect.x <= 470:
            self.direction = 1
        if self.rect.x >= win_width - 85:
            self.direction = 0

        if self.direction == 0:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed   
player = Player("hero.png",5,win_height - 80,4) 
cyborg = Enemy("cyborg.png",win_width - 80,280,2)
finish = GameSprite("treasure.png",550,400,2)
game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    windows.blit(background,(0,0))
    player.update()
    cyborg.update()
    player.reset()
    cyborg.reset()
    finish.reset()
    display.update()
    clock.tick(fps)
-*- coding: utf-8 -*-