import pygame
import sys
import pygame.locals as pl
import main

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('puzzle')
GOLD = (200, 200, 0)


def draw_text(text, font, color, surface, x, y):
    """функция для отрисовки текста"""
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def button_1(pup):
    """создаёт кнопку play"""
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font('fonts/undertale battle font_0.ttf', min(int(h / 8), int(w / 8)))

    mx, my = pygame.mouse.get_pos()

    button1 = pygame.Rect(2 * w / 6, 3 * h / 8, w / 3, h / 8)

    if button1.collidepoint((mx, my)):
        pygame.draw.rect(main.screen, (255, 0, 0), button1)
        if pup:
            game()
    else:
        pygame.draw.rect(main.screen, (0, 0, 255), button1)
    draw_text('play', font, (255, 255, 255), main.screen, w / 2 - min(int(h / 8), int(w / 8)), 77 * h / 200)


def button_2(pup):
    """создаёт кнопку quit"""
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font('fonts/undertale battle font_0.ttf', min(int(h / 8), int(w / 8)))
    draw_text('main menu', font, (255, 255, 255), main.screen, w / 200, h / 20)

    mx, my = pygame.mouse.get_pos()

    button2 = pygame.Rect(2 * w / 6, 5 * h / 8, w / 3, h / 8)
    if button2.collidepoint((mx, my)):
        pygame.draw.rect(main.screen, (255, 0, 0), button2)
        if pup:
            quit()
    else:
        pygame.draw.rect(main.screen, (0, 255, 255), button2)
    draw_text('quit', font, (255, 255, 255), main.screen, w / 2 - min(int(h / 8), int(w / 8)), 127 * h / 200)


def main_menu():
    """вызывает менюшку"""
    click = False
    pic = pygame.image.load("image/fon.jpg")
    while True:
        button_1(click)
        button_2(click)
        if click:
            main.screen.blit(pygame.transform.scale(pic, main.screen.get_size()), (0, 0))
            click = False
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pl.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            elif event.type == pl.VIDEORESIZE:
                main.screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
            elif event.type == pl.VIDEOEXPOSE:  # handles window minimising/maximising
                main.screen.fill((0, 0, 0))
                main.screen.blit(pygame.transform.scale(pic, main.screen.get_size()), (0, 0))

        pygame.display.update()
        mainClock.tick(60)


def finished_menu():
    """
    Функция выызывается при проождении всех уровней
    """
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font('fonts/undertale battle font_0.ttf', min(int(h / 8), int(w / 8)))
    main.clear_screen(main.screen)
    draw_text("You win", font, GOLD, main.screen, w / 4, h / 3)
    pygame.display.update()
    while not main.finished[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.cur_level = 0
                    main.LEVELS[main.cur_level] = main.levels.LIST_OF_LEVELS[main.cur_level](main.screen)
                    main.finished[0] = True


def game():
    """
    Функция, запускающая игру. Это вызывается кнопкой меню,
    здесь меню можно отключить и т.д.
    """
    main.clear_screen(main.screen)


    pygame.display.update()
    while not main.finished[0]:
        main.cur_level = main.game_process(main.finished, main.cur_level)
        if main.cur_level == len(main.LEVELS):
            finished_menu()
    main.finished[0] = False


main_menu()
