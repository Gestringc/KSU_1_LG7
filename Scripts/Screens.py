import pygame


#----------------------------------------------------------------------------------------------------------------------#
##   End of Game Screen ##
def end_game_screen(message, Game_Screen, button_font, dead_image, font, Froggie_Music):
    Froggie_Music.stop()
    Screen_Music = pygame.mixer.Sound("./Music/Screen_Music.mp3")
    Screen_Music.set_volume(0.6)
    Screen_Music.play(2)
    running = True
    retry_text, retry_button = button_font.render("Play Again", (255, 255, 255), size=36)
    quit_text, quit_button = button_font.render("Quit", (255, 255, 255), size=36)

    retry_rect = pygame.Rect(Game_Screen.get_width() / 2 - retry_button.width / 2, Game_Screen.get_height() / 2,
                             retry_button.width, retry_button.height)
    quit_rect = pygame.Rect(Game_Screen.get_width() / 2 - quit_button.width / 2, Game_Screen.get_height() * 2 / 3,
                            quit_button.width, quit_button.height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    Screen_Music.stop()
                    Froggie_Music.play(-1)
                    return True
                elif quit_rect.collidepoint(event.pos):
                    Screen_Music.stop()
                    return False

        Game_Screen.blit(dead_image, (350, 200))
        text_surface, rect = font.render(message, (255, 255, 255), size=100)
        Game_Screen.blit(text_surface, (Game_Screen.get_width() / 2 - rect.width / 2, 45))
        Game_Screen.blit(retry_text, retry_rect)
        Game_Screen.blit(quit_text, quit_rect)
        pygame.display.flip()

    return False
#----------------------------------------------------------------------------------------------------------------------#
## Pause Game Screen ##
def pause_game_screen(message, Game_Screen, button_font, dead_image, font, Froggie_Music):
    Froggie_Music.stop()
    Screen_Music = pygame.mixer.Sound("./Music/Screen_Music.mp3")
    Screen_Music.set_volume(0.6)
    Screen_Music.play(-1)
    running = True
    retry_text, retry_button = button_font.render("Resume Game", (255, 255, 255), size=36)
    quit_text, quit_button = button_font.render("Quit", (255, 255, 255), size=36)

    retry_rect = pygame.Rect(Game_Screen.get_width() / 2 - retry_button.width / 2, Game_Screen.get_height() / 2,
                             retry_button.width, retry_button.height)
    quit_rect = pygame.Rect(Game_Screen.get_width() / 2 - quit_button.width / 2, Game_Screen.get_height() * 2 / 3,
                            quit_button.width, quit_button.height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    Screen_Music.stop()
                    Froggie_Music.play(-1)
                    return True
                elif quit_rect.collidepoint(event.pos):
                    Screen_Music.stop()
                    return False

        Game_Screen.blit(dead_image, (350, 200))
        text_surface, rect = font.render(message, (255, 255, 255), size=100)
        Game_Screen.blit(text_surface, (Game_Screen.get_width() / 2 - rect.width / 2, 45))
        Game_Screen.blit(retry_text, retry_rect)
        Game_Screen.blit(quit_text, quit_rect)
        pygame.display.flip()

    return False
