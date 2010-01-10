
import pygame
import math

WIDTH=320
HEIGHT=480
WIDTH_2 = WIDTH/2
HEIGHT_2 = HEIGHT/2
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
LAUNCHER_CENTER=(WIDTH_2, 480)
LAUNCHER_RADIUS = 40

def generate_launcher_path():
	tmp = []
	PI = 3.14159
	fidelity = PI/180
	angle = 0
	cx = LAUNCHER_CENTER[0]
	cy = LAUNCHER_CENTER[1]
	while angle<2*PI:
		x = int(math.cos(angle) * LAUNCHER_RADIUS + cx)
		y = int(math.sin(angle) * LAUNCHER_RADIUS + cy)
		if y>480:
			pass
		else:
			tmp.append((x,y))
		angle = angle + fidelity
	# removed the first element here
	# i think i was getting a reach around bug :)
	tmp = tmp[1:]	
	return tmp

launcher_path = generate_launcher_path()
print len(launcher_path)

class Launcher(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.cp = 0
		self.image = pygame.Surface((4,4))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.topleft = launcher_path[self.cp]
		self.len = len(launcher_path)
		self.dir = 1
	def update(self):
		self.cp = self.cp + self.dir
		if self.cp == self.len:
			self.cp = self.len-1
			self.dir = -1
		elif self.cp==0:
			self.cp = 0
			self.dir = 1
		self.rect.topleft = launcher_path[self.cp]

class Missile(pygame.sprite.Sprite):
	def __init__(self, start_x, start_y, velocity_x, velocity_y):
		pygame.sprite.Sprite.__init__(self)
		self.x = start_x
		self.y = start_y
		self.vel_x = velocity_x
		self.vel_y = velocity_y
		self.image = pygame.Surface((10,10))
		pygame.draw.circle(self.image,WHITE,(2,2),4)
		self.rect = self.image.get_rect()
		self.max = 100
	def update(self):
		self.rect.topleft= (self.x,self.y)
		self.x = self.x + self.vel_x
		self.y = self.y + self.vel_y
		self.max = self.max - 1
		if self.max == 0:
			self.kill()

class Particle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	def update(self):
		pass

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
stop_game = False
launcher = Launcher()
missile_group = pygame.sprite.Group()

def fire():
	init_x = launcher.rect.left
	init_y = launcher.rect.top
	missile_group.add(Missile(init_x,init_y,0.1,-3))

while 1:

	if stop_game:
		break	
	clock.tick(60)

	for evt in pygame.event.get():
		if evt.type == pygame.constants.QUIT:
			stop_game = True
			break
		elif evt.type == pygame.constants.KEYUP:
			if evt.key == pygame.constants.K_ESCAPE:
				stop_game = True
				break
		elif evt.type == pygame.constants.MOUSEBUTTONUP:
			print evt
			fire()

	# fill with black
	screen.fill((0,0,0))

	# dont fall below this line
	pygame.draw.line(screen, RED, (0, 480-50),
		(WIDTH,480-50))

	for (x,y) in launcher_path:
		pygame.draw.circle(screen,BLUE,(x,y),2)

	launcher.update()
	screen.blit(launcher.image,launcher.rect)

	missile_group.update()
	for m in missile_group.sprites():
		screen.blit(m.image,m.rect)

	pygame.display.flip()
	# pygame.display.update()


