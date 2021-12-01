# Объект холста Canvas
from time import time
from tkinter import Canvas

import config
from detail import pixel


class CanvasField:
    # Данные работы
    _canvas_field = None

    # Рабочее окно
    _window = None

    # Инициализация окна
    def __init__(self, _window):
        self._window = _window

    # Запуск окна
    def setup(self, _operation_data, _operation_axis, _operation_light):

        # Создание холста
        _temp_canvas = Canvas(self._window, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT, bg="lightgrey",
                              cursor="pencil")

        # Переход от виртуального к реальному
        self._canvas_field = _temp_canvas

        # Обновление холста
        self.update(_operation_data, _operation_axis, _operation_light)

    # Обновление изображения на холсте
    def update(self, _operation_data, _operation_axis, _light):
        # Полная очистка холста
        self._canvas_field.delete("all")

        # Отрисовка фона
        self._canvas_field = Canvas(self._window, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT,
                                    bg="lightgrey",
                                    cursor="pencil")

        # Отрисовка осей координат
        _operation_axis.draw(self._canvas_field)

        # Отрисовка деталей
        for temp_detail in _operation_data.get_operation_details():
            # print("Рисуется ->")
            # start_time = time()
            temp_detail.draw(self._canvas_field, _light, _operation_axis)
            # print("Time: ", time() - start_time)

        self.canvas_field.create_oval(
            [_light.x - config.SUN_R, _light.y - config.SUN_R],
            [_light.x + config.SUN_R, _light.y + config.SUN_R],
            fill="yellow")

        # Получение таблицы цветов пикселей на канвасе
        # _pixels_table = _operation_data.get_pixels_table()

        # for y in range(len(_pixels_table)):
        #     for x in range(len(_pixels_table[0])):
        #         if _pixels_table[y][x] != None:
        #             self._canvas_field.create_line(x, y, x, y, fill=_pixels_table[y][x].color)

        # _pixels_table = _operation_data.get_pixels_table().table

        # print(_pixels_table)

        # self._canvas_field.create_line(10, 10, 11, 11, fill="red")

        # for y in range(config.CANVAS_HEIGHT):
        #     for x in range(config.CANVAS_WIDTH):
        #         if _pixels_table[y][x].color is not None:
        #             # print("_pixels_table[y][x].color is not None")
        #             self._canvas_field.create_line(x, y, x + 1, y + 1, fill=_pixels_table[y][x].color)

        # print("Таблица: \n", _pixels_table)

        # Упаковка
        self._canvas_field.grid(row=0, column=3, columnspan=10, rowspan=10)

    @property
    def canvas_field(self):
        return self._canvas_field

    @canvas_field.setter
    def canvas_field(self, value):
        self._canvas_field = value
