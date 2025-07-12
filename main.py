import pygame, sys
from game import Game
from colors import Colors

pygame.init()



title_font= pygame.font.Font(None, 40)
score_surface= title_font.render("Score", True, Colors.purple)
next_surface=title_font.render("Next", True, Colors.purple)
game_over_surface=title_font.render("GAME OVER", True, Colors.purple)

score_rect=pygame.Rect(320,55, 170, 60)
next_rect=pygame.Rect(320,215,170,180)


screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

clock= pygame.time.Clock()

game= Game()
GAME_UPDATE =pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit() 

        if event.type == pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over= False
                game.reset()
            if event.key== pygame.K_LEFT:
                game.move_left()
            if event.key== pygame.K_RIGHT:
                game.move_right()
            if event.key== pygame.K_DOWN:
                game.move_down()
                game.update_score(0,1)

            if event.key== pygame.K_UP:
                game.rotate()
        if event.type ==GAME_UPDATE and game.game_over==False:
            game.move_down()
   
   
    #drawing
    score_value_surface=title_font.render(str(game.score),True, Colors.purple)

    screen.fill(Colors.blush_pink)
    screen.blit(score_surface, (365, 20, 50,50))
    screen.blit(next_surface,(375,180,50,50))

    if game.game_over==True:
        screen.blit(game_over_surface,(320,450,50,50))
    
    pygame.draw.rect(screen, Colors.white, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx= score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.white, next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

    from colors import Colors
