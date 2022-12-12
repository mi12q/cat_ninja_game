"""
Модуль хранит в себе классы нижних объектов.
"""
import pygame
import pygame.draw as dr


class BottomObj:
    """
    Класс нижнего объекта, по нему передвигаются верхний объекты.
    Или не передвигаются, в зависимости от самого объекта.
    """
    def __init__(self, _images):
        self.current = 0
        self.images = _images
        self.image = self.images[self.current]

    def draw(self, screen, x, y):
        """
        Функция рисует воду.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:
        """
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def update(self, speed):
        """
        Обновление картинки для создания анимации.
        :param speed: скорость, с которой нужно менять картинки.
        :return:
        """
        self.current += speed
        if int(self.current) >= len(self.images):
            self.current = 0
        self.image = self.images[int(self.current)]


class Floor(BottomObj):
    """
    Пол. По полу может двигаться любой объект.
    """
    def __init__(self, _images):
        super().__init__(_images)


class Water(BottomObj):
    """
    Вода. Игрок не может двигаться по воде, коробка попадая в воду заменят воду собой,
    создавая мост.
    """
    def __init__(self, _images):
        super().__init__(_images)


class NextLevelTile(BottomObj):
    """
    Плитка перемещения на следующий уровень.
    Может называться "finish" или финишной клеткой.
    """
    def __init__(self, _images, x=0, y=0):
        super().__init__(_images)
        self.x = x
        self.y = y
        self.image = _images[0]


class Spring(BottomObj):
    """
    Пружинка. Пуляет объект в к другую клетку в зависимость от направления
    и силы пружинки. Пружинка умная: она не пуляет объект, если клетка приземления занята.
    Также не пуляет игрока - кота в воду.
    """
    def __init__(self, direction, power, _images):
        super().__init__(_images)
        self.direction = direction
        self.power = power
        angle = 0
        if direction == 'up':
            angle = 0
        if direction == 'down':
            angle = 180
        if direction == 'left':
            angle = 90
        if direction == 'right':
            angle = 270

        self.images = []
        for image in _images:
            self.images.append(pygame.transform.rotozoom(image, angle, 1))
        self.image = pygame.transform.rotozoom(_images[self.current], angle, 1)

    def draw(self, screen, x, y):
        """
        Функция рисует пружину.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:
        """
        dr.rect(screen, 'yellow', (x, y, 40, 40))
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)
