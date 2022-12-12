"""
Модуль хранит в себе классы верхних объектов.
"""
import images
import pygame
import time


class TopObj:
    """
    Класс верхних объектов. Знают, как себя нарисовать.
    """
    def draw(self, screen, x0, y0):
        pass


class Box(TopObj):
    """
    Класс коробки. Игрок может её двигать. Также коробка попадая
    на клетку с нижним объектом Water спускается вниз и образует мост, по которому можно ходить.
    """
    def __init__(self, _images):
        self.dx = 0
        self.dy = 0
        self.a = 1
        self.b = 0
        self.size = 1
        self.images = _images
        self.image = self.images[0]

    def draw(self, screen, x, y):
        """
        Функция рисует коробку.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return: 
        """
        temp_image = pygame.transform.rotozoom(self.image, 0, self.size)
        rect = temp_image.get_rect()
        rect.center = (x + 20 + self.dx, y + 20 + self.dy)
        screen.blit(temp_image, rect)
        self.keep_moving()

    def start_moving(self, dx, dy):
        """
        Начало анимации движения. Обязательно запускать, если хочется видеть движение коробки
        :param dx: смещение коорбинаты x коробки (координата связанная с уровнем)
        :param dy: смещение коорбинаты н коробки (координата связанная с уровнем)
        :return:
        """
        self.dx = -40 * dx
        self.dy = -40 * dy

    def start_flight(self, max_dx, max_dy):
        """
        Начало анимации полёта. Обязательно запускать, если хотчется увидеть анимацию полёта, когда
        коробка попадает на пружинку.
        :param max_dx: максимальное смещение коорбинаты x коробки (координата связанная с уровнем)
        :param max_dy: максимальное смещение коорбинаты y коробки (координата связанная с уровнем)
        :return:
        """
        self.size += 0.1
        if max_dy == 0:
            temp = max_dx * 40
        else:
            temp = max_dy * 40

        self.a = -2 / temp ** 2
        self.b = 2 / temp

    def keep_moving(self):
        """
        Метод меняет координаты коробки в зависимости от движения - простого перемещения
        по земле или полёта. Если коробка стоит, начего не делает.
        :return:
        """
        if 0 < abs(self.dx) or 0 < abs(self.dy):
            if self.dx != 0:
                self.dx += -self.dx / abs(self.dx) * 8
                time.sleep(0.01)
                if self.size > 1:
                    self.size = self.a * abs(self.dx) ** 2 + self.b * abs(self.dx) + 1
            if self.dy != 0:
                self.dy += -self.dy / abs(self.dy) * 8
                time.sleep(0.01)
                if self.size > 1:
                    self.size = self.a * abs(self.dy) ** 2 + self.b * abs(self.dy) + 1
                else:
                    self.size = 1


class Wall(Box):
    """
    Стена. Игрок не может её двигать.
    """
    def __init__(self, _images):
        super().__init__(_images)


class Player(TopObj):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, _images, x=0, y=0):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.a = 1
        self.b = 0
        self.size = 1

        self.sprites = _images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.side = 'R'
        self.check = 0

    def draw(self, screen, x, y):
        """
        Функция рисует игрока.
        :return:
        """
        if self.size == 1:
            rect = self.image.get_rect()
            rect.center = (x + 20 + self.dx, y + 20 + self.dy)
            screen.blit(self.image, rect)
            self.keep_moving()
        else:
            temp_image = pygame.transform.rotozoom(self.image, 0, self.size)
            rect = temp_image.get_rect()
            rect.center = (x + 20 + self.dx, y + 20 + self.dy)
            screen.blit(temp_image, rect)
            self.keep_moving()

        time.sleep(0.02)

    def change_sprites(self, _images):
        """
        Функция меняет картинки игрока.
        :return:
        """
        self.sprites = _images

    def to_left(self):
        """
        Функция меняет направление игрока налево.
        :return:
        """
        self.side = 'L'

    def to_right(self):
        """
        Функция меняет направление игрока направо.
        :return:
        """
        self.side = 'R'

    def update(self, speed):
        """
        Функция меняет изображения игрока с заданной скоростью.
        :param speed: - скорость.
        :return:
        """
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            if self.side == 'R':
                self.sprites = images.load_images_player()
            else:
                self.sprites = images.load_images_mirrored()
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def draw_kick(self, x):
        """
        Функция рисует игрока, когда он пинает коробку.
        :param x: - x
        :return:
        """

        if x > self.x:
            self.sprites = images.load_kick()
        else:
            self.sprites = images.load_kick_left()

    def start_moving(self, dx, dy):
        """
        Начало анимации движения. Обязательно запускать, если хочется видеть движение игрока.
        :param dx: смещение коорбинаты x коробки (координата связанная с уровнем)
        :param dy: смещение коорбинаты н коробки (координата связанная с уровнем)
        :return:
        """
        if dx > 0:
            self.change_sprites(images.walking_right())
        elif dx < 0:
            self.change_sprites(images.walking_left())
        elif self.side == 'R':
            self.change_sprites(images.walking_right())
        elif self.side == 'L':
            self.change_sprites(images.walking_left())

        self.dx = -40 * dx
        self.dy = -40 * dy

    def start_flight(self, max_dx, max_dy):
        """
        Функция рисует игрока, когда он летит.
        :param max_dx:
        :param max_dy:
        :return:
        """
        self.change_sprites(images.player_jump())
        self.size += 0.1
        if max_dy == 0:
            temp = max_dx * 40
        else:
            temp = max_dy * 40

        self.a = -2 / temp ** 2
        self.b = 2 / temp

    def keep_moving(self):
        """
        Функция движет игрока.
        :return:
        """
        if 0 < abs(self.dx) or 0 < abs(self.dy):
            if self.dx != 0:
                self.dx += -self.dx / abs(self.dx) * 8
                time.sleep(0.01)
                self.update(0.5)
                if self.size > 1:
                    self.size = self.a * abs(self.dx) ** 2 + self.b * abs(self.dx) + 1
            if self.dy != 0:
                self.dy += -self.dy / abs(self.dy) * 8
                time.sleep(0.01)
                self.update(0.5)
                if self.size > 1:
                    self.size = self.a * abs(self.dy) ** 2 + self.b * abs(self.dy) + 1
                else:
                    self.size = 1
