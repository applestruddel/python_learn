import sys

import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

pygame.display.set_caption('hello World')

#colors
blue = (0, 0, 255)
white = (0, 0, 0)
#font
basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('hello world', True, white, blue)
textRect = text.get_rect()


window.blit(text, textRect)


pygame.display.update()


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
