import pygame

pygame.init()
dark_blue=(44,44,127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")

clock= pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            SystemExit() #sys.exit()
    #drawing

    screen.fill(dark_blue)
    pygame.display.update()
    clock.tick(60)