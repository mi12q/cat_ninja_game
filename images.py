"""
Модуль содержит функции, возвращающие изображения
в зависимости от самой функции.
"""
import pygame

sprites = {

    "player": [pygame.image.load('image/tile000.png'), pygame.image.load('image/tile001.png'),
               pygame.image.load('image/tile001.png'), pygame.image.load('image/tile003.png')],
    "player_mirrored": [pygame.image.load('image/m0.png'), pygame.image.load('image/m1.png'),
                        pygame.image.load('image/m2.png'), pygame.image.load('image/m3.png')],
    "kick_right": [pygame.image.load('image/k0.png'), pygame.image.load('image/k1.png'),
                   pygame.image.load('image/k2.png'), pygame.image.load('image/k3.png'),
                   pygame.image.load('image/k4.png'), pygame.image.load('image/k5.png')],
    "kick_left": [pygame.image.load('image/kl0.png'), pygame.image.load('image/kl1.png'),
                  pygame.image.load('image/kl2.png'), pygame.image.load('image/kl3.png'),
                  pygame.image.load('image/kl4.png'), pygame.image.load('image/kl5.png')],
    "box": [pygame.image.load('image/box.png'), pygame.image.load('image/bridge.png')],
    "water": [pygame.image.load('image/w0.png'), pygame.image.load('image/w1.png'), pygame.image.load('image/w2.png')],
    "grass": [pygame.image.load('image/Grass.jpg')],
    "ladder": [pygame.image.load('image/ladder.png')],
    "wall": [pygame.image.load('image/wall.png')],
    "walking_right": [pygame.image.load('image/v0.png'),
                      pygame.image.load('image/v1.png'), pygame.image.load('image/v2.png'),
                      pygame.image.load('image/v3.png'),
                      pygame.image.load('image/v4.png'), pygame.image.load('image/v5.png'),
                      pygame.image.load('image/v6.png'), pygame.image.load('image/v7.png')],
    "walking_left": [pygame.image.load('image/vl0.png'),
                     pygame.image.load('image/vl1.png'), pygame.image.load('image/vl2.png'),
                     pygame.image.load('image/vl3.png'),
                     pygame.image.load('image/vl4.png'), pygame.image.load('image/vl5.png'),
                     pygame.image.load('image/vl6.png'), pygame.image.load('image/vl7.png')],
    "bridge": [pygame.image.load('image/bridge.png')],
    "player_jump": 4 * [pygame.image.load('image/j3.png'),
                        pygame.image.load('image/j4.png'), pygame.image.load('image/j5.png'),
                        pygame.image.load('image/j6.png'), pygame.image.load('image/j7.png')],
    "arrow": [pygame.image.load('image/ar0.png'),
              pygame.image.load('image/ar1.png'), pygame.image.load('image/ar2.png'),
              pygame.image.load('image/ar3.png'), pygame.image.load('image/ar4.png'),
              pygame.image.load('image/ar5.png'), pygame.image.load('image/ar6.png'),
              pygame.image.load('image/ar7.png'), pygame.image.load('image/ar8.png'),
              pygame.image.load('image/ar9.png'), pygame.image.load('image/ar10.png'),
              pygame.image.load('image/ar11.png')]

}


def load_images_player():
    """
    Функция возвращает список изображений игрока.
    :return: - список изображений
    """

    return sprites["player"]


def load_images_mirrored():
    """
    Функция возвращает список изображений игрока повернутого налево.
    :return: - список изображений
    """

    return sprites["player_mirrored"]


def load_kick():
    """
    Функция возвращает список изображений игрока, когда он пинает коробку направо.
    :return: - список изображений
    """
    return sprites["kick_right"]


def load_kick_left():
    """
    Функция возвращает список изображений игрока, когда он пинает коробку налево.
    :return: - список изображений
    """
    return sprites["kick_left"]


def water_images():
    """
    Функция возвращает список изображений воды.
    :return: - список изображений
    """
    return sprites["water"]


def box_images():
    """
    Функция возвращает список изображений коробки.
    :return: - список изображений
    """

    return sprites["box"]


def grass():
    """
    Функция возвращает изображение трави.
    :return: - список изображений
    """
    return sprites["grass"]


def ladder():
    """
    Функция возвращает изображение лестницы.
    :return: - список изображений
    """

    return sprites["ladder"]


def wall():
    """
    Функция возвращает изображение стены.
    :return: - список изображений
    """
    return sprites["wall"]


def walking_right():
    """
    Функция возвращает список изображений игрока, когда он движется направо.
    :return: - список изображений
    """
    return sprites["walking_right"]


def walking_left():
    """
    Функция возвращает список изображений игрока, когда он движется налево.
    :return: - список изображений
    """

    return sprites["walking_left"]


def player_jump():
    """
    Функция возвращает список изображений игрока, когда он прыгает.
    :return:
    """
    return sprites["player_jump"]


def arrow():
    """
       Функция возвращает список изображений стрелки.
       :return:
       """
    return sprites["arrow"]
