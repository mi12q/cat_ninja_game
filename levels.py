"""
Данный файл хранит в себе функции, который могут построить уровень, если им передать
скрин, на котором уровень будет рисоваться.
"""
import classes
import classes_top_obj as front
import classes_bottom_obj as back
import images


def level1(screen):
    level_1 = classes.Level(screen, 100, 100, 5, 5)
    level_1.add_player(front.Player(images.load_images_player()), 0, 0)
    level_1.add_finish(back.NextLevelTile(images.ladder()), 4, 0)
    level_1.tiles[2][1].top_obj = front.Box(images.box_images())
    level_1.tiles[1][2].top_obj = front.Box(images.box_images())

    level_1.tiles[0][1].top_obj = front.Wall(images.wall())
    level_1.tiles[1][1].top_obj = front.Wall(images.wall())
    level_1.tiles[3][0].top_obj = front.Wall(images.wall())
    level_1.tiles[3][1].top_obj = front.Wall(images.wall())
    level_1.tiles[1][3].top_obj = front.Wall(images.wall())

    level_1.tiles[4][1].bottom_obj = back.Water(images.water_images())
    level_1.tiles[4][2].bottom_obj = back.Water(images.water_images())
    return level_1


def level2(screen):
    level_2 = classes.Level(screen, 100, 100, 6, 8)
    level_2.add_player(front.Player(images.load_images_player()), 0, 7)
    level_2.add_finish(back.NextLevelTile(images.ladder()), 5, 7)

    level_2.tiles[4][2].top_obj = front.Wall(images.wall())
    level_2.tiles[5][2].top_obj = front.Wall(images.wall())
    level_2.tiles[3][5].top_obj = front.Wall(images.wall())
    level_2.tiles[3][6].top_obj = front.Wall(images.wall())
    level_2.tiles[3][7].top_obj = front.Wall(images.wall())

    level_2.tiles[0][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[1][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[2][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[3][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[4][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[5][3].bottom_obj = back.Water(images.water_images())
    level_2.tiles[0][4].bottom_obj = back.Water(images.water_images())
    level_2.tiles[1][4].bottom_obj = back.Water(images.water_images())
    level_2.tiles[2][4].bottom_obj = back.Water(images.water_images())
    level_2.tiles[3][4].bottom_obj = back.Water(images.water_images())
    level_2.tiles[4][4].bottom_obj = back.Water(images.water_images())
    level_2.tiles[5][4].bottom_obj = back.Water(images.water_images())

    level_2.tiles[1][2].top_obj = front.Box(images.box_images())
    level_2.tiles[4][1].top_obj = front.Box(images.box_images())
    level_2.tiles[1][5].top_obj = front.Box(images.box_images())
    level_2.tiles[1][6].top_obj = front.Box(images.box_images())
    level_2.tiles[2][5].top_obj = front.Box(images.box_images())
    return level_2


def level3(screen):
    level_3 = classes.Level(screen, 100, 100, 7, 7)
    level_3.add_player(front.Player(images.load_images_player()), 4, 6)
    level_3.add_finish(back.NextLevelTile(images.ladder()), 0, 0)

    level_3.tiles[1][1].top_obj = front.Wall(images.wall())
    level_3.tiles[1][2].top_obj = front.Wall(images.wall())
    level_3.tiles[1][0].top_obj = front.Wall(images.wall())
    level_3.tiles[1][4].top_obj = front.Wall(images.wall())
    level_3.tiles[2][4].top_obj = front.Wall(images.wall())
    level_3.tiles[2][4].top_obj = front.Wall(images.wall())
    level_3.tiles[3][2].top_obj = front.Wall(images.wall())
    level_3.tiles[3][3].top_obj = front.Wall(images.wall())
    level_3.tiles[3][4].top_obj = front.Wall(images.wall())
    level_3.tiles[3][5].top_obj = front.Wall(images.wall())
    level_3.tiles[3][6].top_obj = front.Wall(images.wall())

    level_3.tiles[3][0].bottom_obj = back.Water(images.water_images())
    level_3.tiles[3][1].bottom_obj = back.Water(images.water_images())
    level_3.tiles[0][2].bottom_obj = back.Water(images.water_images())
    level_3.tiles[2][2].bottom_obj = back.Water(images.water_images())

    level_3.tiles[0][4].top_obj = front.Box(images.box_images())
    level_3.tiles[4][3].top_obj = front.Box(images.box_images())
    level_3.tiles[4][5].top_obj = front.Box(images.box_images())
    level_3.tiles[5][4].top_obj = front.Box(images.box_images())
    level_3.tiles[6][0].top_obj = front.Box(images.box_images())
    level_3.tiles[6][2].top_obj = front.Box(images.box_images())
    level_3.tiles[6][5].top_obj = front.Box(images.box_images())

    level_3.tiles[0][6].bottom_obj = back.Spring('up', 4, images.arrow())
    return level_3


def level4(screen):
    level_4 = classes.Level(screen, 100, 100, 7, 7)
    level_4.add_player(front.Player(images.load_images_player()), 0, 0)
    level_4.add_finish(back.NextLevelTile(images.ladder()), 6, 0)

    level_4.tiles[3][0].top_obj = front.Wall(images.wall())
    level_4.tiles[3][1].top_obj = front.Wall(images.wall())
    level_4.tiles[3][2].top_obj = front.Wall(images.wall())
    level_4.tiles[3][3].top_obj = front.Wall(images.wall())
    level_4.tiles[3][4].top_obj = front.Wall(images.wall())

    level_4.tiles[4][1].bottom_obj = back.Water(images.water_images())
    level_4.tiles[4][2].bottom_obj = back.Water(images.water_images())
    level_4.tiles[4][3].bottom_obj = back.Water(images.water_images())
    level_4.tiles[4][4].bottom_obj = back.Water(images.water_images())
    level_4.tiles[5][1].bottom_obj = back.Water(images.water_images())
    level_4.tiles[5][2].bottom_obj = back.Water(images.water_images())
    level_4.tiles[5][3].bottom_obj = back.Water(images.water_images())
    level_4.tiles[5][4].bottom_obj = back.Water(images.water_images())
    level_4.tiles[6][1].bottom_obj = back.Water(images.water_images())
    level_4.tiles[6][2].bottom_obj = back.Water(images.water_images())
    level_4.tiles[6][3].bottom_obj = back.Water(images.water_images())
    level_4.tiles[6][4].bottom_obj = back.Water(images.water_images())

    level_4.tiles[1][1].top_obj = front.Box(images.box_images())
    level_4.tiles[2][2].top_obj = front.Box(images.box_images())
    level_4.tiles[0][2].top_obj = front.Box(images.box_images())
    level_4.tiles[0][4].top_obj = front.Box(images.box_images())
    level_4.tiles[2][4].top_obj = front.Box(images.box_images())
    level_4.tiles[1][5].top_obj = front.Box(images.box_images())
    level_4.tiles[2][6].top_obj = front.Box(images.box_images())

    level_4.tiles[2][3].bottom_obj = back.Spring('right', 2, images.arrow())
    level_4.tiles[4][5].bottom_obj = back.Spring('up', 3, images.arrow())

    return level_4




LIST_OF_LEVELS = (level1, level2, level3, level4)
