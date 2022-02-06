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
class Wall(sprite.Sprite):
	def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
		super().__init__()
		self.color = (color_1, color_2, color_3)
		self.width = wall_width
		self.height = wall_height

		self.image = Surface((self.width, self.height))
		self.image.fill(self.color)

		self.rect = self.image.get_rect()
		self.rect.x = wall_x
		self.rect.y = wall_y
	def draw_wall(self):
		windows.blit(self.image, (self.rect.x, self.rect.y))
player = Player("hero.png",5,win_height - 80,4) 
cyborg = Enemy("cyborg.png",win_width - 80,280,2)
finish = GameSprite("treasure.png",550,400,2)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 190, 100, 10, 380)
w5 = Wall(154, 205, 50, 280, 20, 10, 380)
w6 = Wall(154, 205, 50, 370, 100, 10, 380)
w7 = Wall(154, 205, 50, 460, 100, 10, 380)

font.init()
font1 = font.SysFont('Arial',70)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
game = True
clock = time.Clock()
fps = 60
finishB = False
while game:
	for e in event.get():
		if e.type == QUIT:
			game = False
	if not finishB:
		windows.blit(background,(0,0))
		player.update()
		cyborg.update()
		player.reset()
		cyborg.reset()
		finish.reset()
		w1.draw_wall()
		w2.draw_wall()
		w3.draw_wall()
		w4.draw_wall()
		w5.draw_wall()
		w6.draw_wall()
		w7.draw_wall()
		if sprite.collide_rect(player, finish):
			finishB = True
			windows.blit(win, (200,200))
		if sprite.collide_rect(player, cyborg):
			finishB = True
			windows.blit(lose, (200,200))
		if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
			finishB = True
			windows.blit(lose, (200,200))
	display.update()
	clock.tick(fps)
