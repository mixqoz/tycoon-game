import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.Rect((300,250,50,50))

run = True
while run:
	
	screen.fill("blue")
	pygame.draw.rect(screen, (255,0,0), player)

	key = pygame.key.get_pressed()
	if key[pygame.K_w] == True:
		player.move_ip(0,-1)
	if key[pygame.K_s] == True:
		player.move_ip(0,1)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()