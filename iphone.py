
import pygame
import math

WIDTH=320
HEIGHT=480
WIDTH_2 = WIDTH/2
HEIGHT_2 = HEIGHT/2
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)
LAUNCHER_CENTER=(WIDTH_2, 480)
LAUNCHER_RADIUS = 40

def generate_launcher_path():
	PI = 3.14159
	fidelity = PI/180
	angle = 0
	cx = LAUNCHER_CENTER[0]
	cy = LAUNCHER_CENTER[1]
	while angle<2*PI:
		x = math(angle) * LAUNCHER_RADIUS +
		angle = angle + fidelity	

generate_launcher_path()

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill(BLACK)
		pygame.draw.circle(self.image,
			BLUE, (100,100), 10)
		self.rect = self.image.get_rect()
		
	def update(self):
		pass

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
stop_game = False

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

	# fill with black
	screen.fill((0,0,0))

	# dont fall below this line
	pygame.draw.line(screen, RED, (0, 480-50),
		(WIDTH,480-50))

	# circle at the bottom that does not change
	pygame.draw.circle(screen, WHITE,
		LAUNCHER_CENTER, LAUNCHER_RADIUS)

	pygame.display.flip()


