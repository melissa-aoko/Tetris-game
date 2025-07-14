import pygame
import sys
from game import Game
from colors import Colors
from auth import sign_up, log_in, update_high_score, load_users, get_high_score

pygame.init()

# ----- Fonts & Text -----
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.purple)
high_score_surface = title_font.render("High Score", True, Colors.purple)
next_surface = title_font.render("Next", True, Colors.purple)
game_over_surface = title_font.render("GAME OVER", True, Colors.purple)

#score_rect = pygame.Rect(320, 55, 170, 60)
#next_rect = pygame.Rect(320, 215, 170, 180)

score_rect = pygame.Rect(320, 55, 170, 60)
high_score_rect = pygame.Rect(320, 145, 170, 60)
next_rect = pygame.Rect(320, 250, 170, 180)  # moved down to fit


# ----- Screen -----
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# ----- Clock -----
clock = pygame.time.Clock()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


# ========== LOGIN SCREEN FUNCTION ==========
def login_screen():
    font = pygame.font.Font(None, 32)
    label_font = pygame.font.Font(None, 28)

    username_box = pygame.Rect(100, 80, 300, 32)
    password_box = pygame.Rect(100, 150, 300, 32)
    show_pass_box = pygame.Rect(410, 150, 20, 20)

    login_button = pygame.Rect(100, 210, 90, 30)
    signup_button = pygame.Rect(210, 210, 90, 30)

    input_color = pygame.Color("white")
    active_user = False
    active_pass = False
    username = ''
    password = ''
    show_password = False
    message = ''
    current_user = None

    def draw_login():
        screen.fill((240, 200, 220))  # Cute blush background

        # Labels
        screen.blit(label_font.render("Enter Username:", True, (80, 0, 80)), (100, 55))
        screen.blit(label_font.render("Enter Password:", True, (80, 0, 80)), (100, 125))

        # Input boxes
        pygame.draw.rect(screen, input_color, username_box, border_radius=8)
        pygame.draw.rect(screen, input_color, password_box, border_radius=8)

        # Password Toggle Box
        pygame.draw.rect(screen, pygame.Color("gray"), show_pass_box)
        screen.blit(label_font.render("👁" if show_password else "❌", True, (0, 0, 0)), (410, 150))

        # Buttons
        pygame.draw.rect(screen, pygame.Color("green"), login_button, border_radius=6)
        pygame.draw.rect(screen, pygame.Color("blue"), signup_button, border_radius=6)

        # Text inside boxes
        screen.blit(font.render(username, True, (0, 0, 0)), (username_box.x + 5, username_box.y + 5))
        pwd_display = password if show_password else '*' * len(password)
        screen.blit(font.render(pwd_display, True, (0, 0, 0)), (password_box.x + 5, password_box.y + 5))

        screen.blit(font.render("Login", True, (255, 255, 255)), (login_button.x + 10, login_button.y + 5))
        screen.blit(font.render("Sign Up", True, (255, 255, 255)), (signup_button.x + 5, signup_button.y + 5))

        if message:
            screen.blit(font.render(message, True, (200, 0, 0)), (100, 260))

        pygame.display.flip()

    while not current_user:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                active_user = username_box.collidepoint(event.pos)
                active_pass = password_box.collidepoint(event.pos)

                if show_pass_box.collidepoint(event.pos):
                    show_password = not show_password
                if login_button.collidepoint(event.pos):
                    success, msg = log_in(username, password)
                    if success:
                        current_user = username
                    message = msg
                elif signup_button.collidepoint(event.pos):
                    success, msg = sign_up(username, password)
                    if success:
                        current_user = username
                    message = msg

            elif event.type == pygame.KEYDOWN:
                if active_user:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_pass:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        draw_login()
        clock.tick(30)

    return current_user


# ========== MAIN ==========
if __name__ == "__main__":
    current_user = login_screen()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    # Save score if it's a high score
                    update_high_score(current_user, game.score)
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_p:
                    game.save_game_state(current_user)
                    print("Game saved!")

                if event.key == pygame.K_r:
                    game.load_game_state(current_user)
                    print("Game loaded!")


                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate()

            if event.type == GAME_UPDATE and not game.game_over:
                game.move_down()

        # === UI VALUES ===
        score_value_surface = title_font.render(str(game.score), True, Colors.purple)
        high_score = get_high_score(current_user)
        high_score_value_surface = title_font.render(str(high_score), True, Colors.purple)

        # === Clear screen ===
        screen.fill(Colors.blush_pink)

        # === SCORE ===
        screen.blit(score_surface, (365, 20))  # Label above box
        pygame.draw.rect(screen, Colors.white, score_rect, 0, 10)  # Box
        screen.blit(score_value_surface, score_value_surface.get_rect(center=score_rect.center))  # Value inside

        # === HIGH SCORE ===
        screen.blit(high_score_surface, (340, 115))  # Label above box
        pygame.draw.rect(screen, Colors.white, high_score_rect, 0, 10)
        screen.blit(high_score_value_surface, high_score_value_surface.get_rect(center=high_score_rect.center))

        # === NEXT BLOCK ===
        screen.blit(next_surface, (375, 220))  # Label above box
        pygame.draw.rect(screen, Colors.white, next_rect, 0, 10)

        # === GAME OVER ===
        if game.game_over:
            screen.blit(game_over_surface, (320, 450))

        # === GAME GRID ===
        game.draw(screen)

        # === DRAW NEXT BLOCK ===
        if game.next_block.id == 3:  # LBlock, slightly taller
            game.next_block.draw(screen, 255, 290)
        elif game.next_block.id == 4:  # OBlock, smaller
            game.next_block.draw(screen, 255, 280)
        else:
            game.next_block.draw(screen, 270, 270)

        # === UPDATE SCREEN ===
        pygame.display.update()


        clock.tick(60)
