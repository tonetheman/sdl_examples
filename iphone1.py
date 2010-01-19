
import pygame

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
WIDTH=320
HEIGHT=480
screen = None
clock = None

class Block(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()

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
	
	screen.fill(BLACK)
	pygame.display.flip()
