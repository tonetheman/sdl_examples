
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
my_dir = None
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

class Block(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
	def update(self):
		if my_dir == EAST:
			self.rect.left = self.rect.left + 1
		elif my_dir == WEST:
			self.rect.left = self.rect.left - 1
		elif my_dir == NORTH:
			self.rect.top = self.rect.top - 1
		elif my_dir == SOUTH:	
			self.rect.top = self.rect.top + 1



pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
stop_game = False
block_group = pygame.sprite.Group()
block_group.add(Block())

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
			elif evt.key == pygame.constants.K_DOWN:
				my_dir = SOUTH
			elif evt.key == pygame.constants.K_UP:
				my_dir = NORTH
			elif evt.key == pygame.constants.K_LEFT:
				my_dir = WEST	
			elif evt.key == pygame.constants.K_RIGHT:
				my_dir = EAST	

	
	screen.fill(BLACK)
	
	block_group.update()
	for b in block_group.sprites():
		screen.blit(b.image,b.rect)

	pygame.display.flip()
