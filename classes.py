"""
Модуль, в котором содержатся классы Level и Tile
"""

import classes_bottom_obj as bottom
import classes_top_obj as top
import images


class Level:
    """
    Создаёт игровой клеточный уровень, в котором будут находится объекты.
    Уровень состоит из клеток. Каждая клетка состоит из двух частей:
    back_obj(то, на чём стоят) и front_obj(то, что стоит на back_obj).
    Чтобы что-то извлечь из платформы, нужно указать координаты клетки - x и y, потом через точку указать часть клетки.
    Например Platform.squares[x][y].back_obj (извлечение нижней части клетки с координатами x и y)
    Уровень самостоятельно организовывает свой пол из класса Floor.
    """

    def __init__(self, screen, x0, y0, horizontal_side, vertical_side):
        """
        Создает уровень, заполняя каждую клекту объектом Floor
        :param horizontal_side: кол-во клеток по горизонтали
        :param vertical_side: кол-во клеток по вертикали
        :param screen: экран
        :param x0: x-координата верхнего левого угла уровн
        :param y0: y-координата верхнего левого угла уровня
        """
        self.screen = screen
        self.x0 = x0
        self.y0 = y0

        self.vertical_side = vertical_side
        self.horizontal_side = horizontal_side
        self.size = 40
        self.tiles = []

        self.player = None
        self.finish = None
        self.completed = False

        for i in range(horizontal_side):
            column = []
            for j in range(vertical_side):
                floor = bottom.Floor(images.grass())
                tile = Tile(None, floor)
                column.append(tile)
            self.tiles.append(column)

    def add_player(self, _player, x, y):
        """
        Добавляет игрока в уровень. Обязательно добавлять игрока именно этим методом.
        :param _player: объект игрока
        :param x: координата x игрока на поле
        :param y: координата y игрока на поле
        :return:
        """
        self.tiles[x][y].top_obj = _player
        self.player = _player
        _player.x = x
        _player.y = y

    def add_finish(self, _finish, x, y):
        """
        Добавляет плитку перехода на следующий уровень. Обязательно добавлять
        данную плитку именно этим методом.
        :param _finish: объект плитки перехода на следующий уровень
        :param x: координата x данной плитки
        :param y: координата y данной плитки
        :return:
        """
        self.tiles[x][y].bottom_obj = _finish
        self.finish = _finish
        _finish.x = x
        _finish.y = y

    def draw(self):
        """
        Рисует клетки на уровне - сначала все нижние, потом все верхние.
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].bottom_obj is not None:
                    self.tiles[i][j].bottom_obj.draw(self.screen, self.x0 + i * self.size, self.y0 + j * self.size)

        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].top_obj is not None:
                    self.tiles[i][j].top_obj.draw(self.screen, self.x0 + i * self.size, self.y0 + j * self.size)

    @staticmethod
    def is_moving(obj):
        """
        Метод проверят, движется ли передаваемый объект.
        :param obj: объект, который нужно проверить.
        :return:
        """
        return obj.dx == obj.dy

    def player_move(self, direction):
        """
        Движение игрока в зависимости от направления.
        Если клетка по направлению движения свободна(т.е верхний объект пуст), то игрок пробует сделать шаг.
        Но если данная клетка занята, то игрок пинает объект на этой клетке.
        :param direction: направление движения
        :return:
        """
        y = self.player.y
        x = self.player.x
        if direction == 'up':
            y -= 1
        if direction == 'down':
            y += 1
        if direction == 'left':
            x -= 1
        if direction == 'right':
            x += 1

        if 0 <= x < self.horizontal_side and 0 <= y < self.vertical_side:
            if self.tiles[x][y].top_obj is not None:
                self.player_kick(x, y)
            else:
                self.player_step(x, y)

    def player_kick(self, x, y):
        """
        Пинок объекта с координатами x и y.
        Если следующая за объектом клетка по направлению пинка свободна(т.е верхний объект пуст),
        то объект перемщается в данную клетку, иначе не перемещается.
        Игрок не может пинком перемещать стены(Wall).
        :param x: координата x объекта
        :param y: координата y объекта
        :return:
        """
        self.player.draw_kick(x)
        if not isinstance(self.tiles[x][y].top_obj, top.Wall) and self.is_moving(self.tiles[x][y].top_obj):
            _x = x + (x - self.player.x)
            _y = y + (y - self.player.y)

            if (0 <= _x < self.horizontal_side and
                    0 <= _y < self.vertical_side and
                    self.tiles[_x][_y].top_obj is None):
                self.tiles[_x][_y].top_obj = self.tiles[x][y].top_obj
                dx = _x - x
                dy = _y - y
                self.tiles[_x][_y].top_obj.start_moving(dx, dy)

                self.tiles[x][y].top_obj = None

    def player_step(self, x, y):
        """
        Перемещение игрока в клетку с координатами x и y.
        Если нижний объект клетки не вода(Water), то игрок перемещается в верхний объект клетки.
        :param x: координата x клетки
        :param y: координата y клетки
        :return:
        """
        if not isinstance(self.tiles[x][y].bottom_obj, bottom.Water) and self.is_moving(self.player):
            self.tiles[self.player.x][self.player.y].top_obj = None
            dx = x - self.player.x
            dy = y - self.player.y
            self.player.start_moving(dx, dy)

            self.player.x = x
            self.player.y = y
            self.tiles[self.player.x][self.player.y].top_obj = self.player

    def check_interaction(self):
        """
        Метод проверяет весь уровень на наличие взаимодействий между объектами.
        :return:
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.water_interaction(i, j):
                    pass
                elif self.next_level_tile_interaction(i, j):
                    pass
                elif self.spring_interaction(i, j):
                    pass

    def water_interaction(self, i, j):
        """
        Проверка и выполнение действий воды.
        Если нижний объект клетки с координатами i и j - вода(Water), то картинка воды обновляется,
        чтобы создать эффект бликов воды.
        Также если верхний объект - это коробка(Box), то коробка проваливается вниз, заменяя собой воду
        и создавая таким образом мост, по которому игрок может ходить.
        :param i: координата x проверяемой клетки
        :param j: координата y проверяемой клетки
        :return: bool - является ли нижний объект водой, а верхний - коробкой
        """
        if isinstance(self.tiles[i][j].bottom_obj, bottom.Water):
            self.tiles[i][j].bottom_obj.update(0.2)
            if (isinstance(self.tiles[i][j].top_obj, top.Box) and
                    self.tiles[i][j].top_obj.dx == self.tiles[i][j].top_obj.dy):
                self.tiles[i][j].bottom_obj = self.tiles[i][j].top_obj
                self.tiles[i][j].top_obj = None
                self.tiles[i][j].bottom_obj.image = self.tiles[i][j].bottom_obj.images[1]
                return True

    def spring_interaction(self, i, j):
        """
        Метод взаимодействия с пружинкой. Если сверху пружинки есть объект,
        то проверяется, есть ли верхний объект на клетке приземления. Если нет, то пружинка пуляет объект
        в данную клетку. Пружинка не пуляет игрока, если нижний объект клетки приземления - вода(Water).
        :param i: координата x проверяемой клетки
        :param j: координата y проверяемой клетки
        :return: bool - пульнула ли пружинка объект или нет
        """

        if isinstance(self.tiles[i][j].bottom_obj, bottom.Spring):
            self.tiles[i][j].bottom_obj.update(0.4)
            if (self.tiles[i][j].top_obj is not None and self.tiles[i][j].top_obj.dx == 0 and
                    self.tiles[i][j].top_obj.dy == 0):
                spring = self.tiles[i][j].bottom_obj
                x = i
                y = j
                if spring.direction == 'up':
                    y -= spring.power
                if spring.direction == 'down':
                    y += spring.power
                if spring.direction == 'left':
                    x -= spring.power
                if spring.direction == 'right':
                    x += spring.power

                if 0 <= x < self.horizontal_side and 0 <= y < self.vertical_side:
                    if self.tiles[x][y].top_obj is None:
                        if not isinstance(self.tiles[i][j].top_obj, top.Player):
                            temp = self.tiles[i][j].top_obj
                            self.tiles[i][j].top_obj = None
                            self.tiles[x][y].top_obj = temp
                            temp.start_moving(x - i, y - j)
                            temp.start_flight(abs(x - i), abs(y - j))
                            return True
                        elif not isinstance(self.tiles[x][y].bottom_obj, bottom.Water):
                            temp = self.tiles[i][j].top_obj
                            self.tiles[i][j].top_obj = None
                            self.tiles[x][y].top_obj = temp
                            self.tiles[x][y].top_obj.x = x
                            self.tiles[x][y].top_obj.y = y
                            temp.start_moving(x - i, y - j)
                            temp.start_flight(abs(x - i), abs(y - j))
                            return True

    def next_level_tile_interaction(self, i, j):
        """
        Проверяет, находится ли игрок на плитке перехода на следующий уровень.
        Если да, то уровень отмечается завершённым.
        :param i: координата x проверяемой клетки
        :param j: координата y проверяемой клетки
        :return: bool - находится ли игрок на плитке перехода на следующий уровень
        """
        if (isinstance(self.tiles[i][j].bottom_obj, bottom.NextLevelTile) and
                isinstance(self.tiles[i][j].top_obj, top.Player)):
            self.completed = True
            return True


class Tile:
    """
    Игровая единица площади, которая содержит задние объекты (BottomObj) и верхние (TopObj).
    """

    def __init__(self, top_obj, bottom_obj):
        """
        Создает клетку
        """
        self.bottom_obj = bottom_obj
        self.top_obj = top_obj
