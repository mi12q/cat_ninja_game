"""
Главный модуль, который создает окно и уровни в нем. Также запускает музыку.
"""

import pygame
import levels
import images

WIDTH = 600
HEIGHT = 600
FPS = 30

pygame.init()
clock = pygame.time.Clock()
finished = [False]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.load("Sound/Backround.mp3")
pygame.mixer.music.play(-1)
LEVELS = [levels.level1(screen), levels.level2(screen), levels.level3(screen), levels.level4(screen), levels.level5(screen)]
cur_level = 0


def clear_screen(window):
    window.fill((0, 0, 0))


def game_process(is_finished, _cur_level):
    """
    Функция, которая воспроизводит конкретный уровень
    """
    LEVELS[_cur_level].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                LEVELS[_cur_level].player_move('up')
            elif event.key == pygame.K_DOWN:
                LEVELS[_cur_level].player_move('down')
            elif event.key == pygame.K_LEFT:
                LEVELS[_cur_level].player.change_sprites(images.load_images_mirrored())
                LEVELS[_cur_level].player_move('left')
                LEVELS[_cur_level].player.to_left()
            elif event.key == pygame.K_RIGHT:
                LEVELS[_cur_level].player.change_sprites(images.load_images_player())
                LEVELS[_cur_level].player_move('right')
                LEVELS[_cur_level].player.to_right()
            elif event.key == pygame.K_ESCAPE:
                finished[0] = True
            elif event.key == pygame.K_r:
                LEVELS[_cur_level] = levels.LIST_OF_LEVELS[_cur_level](screen)

    LEVELS[_cur_level].player.update(0.4)
    LEVELS[_cur_level].check_interaction()
    if LEVELS[_cur_level].completed:
        clear_screen(screen)
        _cur_level += 1
    return _cur_level
