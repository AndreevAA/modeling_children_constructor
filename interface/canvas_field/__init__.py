# Объект холста Canvas
from tkinter import Canvas

import config


class CanvasField:

    # Данные работы
    _canvas_field = None

    # Рабочее окно
    _window = None

    # Инициализация окна
    def __init__(self, _window):
        self._window = _window

    # Запуск окна
    def setup(self, _operation_data, _operation_axis):

        # Создание холста
        _temp_canvas = Canvas(self._window, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT, bg="lightgrey",
                             cursor="pencil")

        # Переход от виртуального к реальному
        self._canvas_field = _temp_canvas

        # Обновление холста
        self.update(_operation_data, _operation_axis)

    # Обновление изображения на холсте
    def update(self, _operation_data, _operation_axis):
        # Полная очистка холста
        self._canvas_field.delete("all")

        # Отрисовка фона
        self._canvas_field = Canvas(self._window, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT, bg="lightgrey",
                             cursor="pencil")

        # Отрисовка осей координат
        _operation_axis.draw(self._canvas_field)

        # Отрисовка деталей
        for temp_detail in _operation_data.get_operation_details():
            print("Рисуется ->")
            temp_detail.draw(self._canvas_field)

        # Упаковка
        self._canvas_field.grid(row=0, column=3, columnspan=10, rowspan=10)

