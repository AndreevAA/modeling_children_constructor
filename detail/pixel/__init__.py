# Объект пикселя
import math

import config


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


class Pixel:
    # Свои непосредственные координаты
    _x, _y, _z = None, None, None
    _color = None

    # Инициализация пикселя
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


# Объект таблицы пикселей
class PixelsTable:
    _table = []
    _start_x, _start_y = None, None
    _width, _height = None, None

    def __init__(self, _width, _height, _start_x, _start_y):
        self._start_x, self._start_y = _start_x, _start_y
        self._width, self._height = _width, _height

        self._table = [[Pixel(x, y, None) for x in range(int(_width * 1.2))]
                       for y in range(int(_height * 1.2))]

    def xor_pixel(self, x, y, pixel):
        self._table[y][x] = pixel
        # if self._table[y][x].color != pixel.color:
        #     # print("x : y, color -> color", x, y, self._table[y][x].color, pixel.color)
        #     self._table[y][x] = pixel
        # else:
        #     self._table[y][x].color = None

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        self._table = value

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def s_x(self):
        return self._start_x

    @property
    def s_y(self):
        return self._start_y

    @property
    def start_y(self):
        return self._start_y

# # Объект таблицы набора PixelsList
# class PixelListsTable:
