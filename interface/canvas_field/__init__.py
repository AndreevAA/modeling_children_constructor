# Объект холста Canvas
from tkinter import Canvas


class CanvasField:

    # Данные работы
    _canvas_field = None

    # Рабочее окно
    _window = None

    # Инициализация окна
    def __init__(self, _window):
        self._window = _window

    # Запуск окна
    def setup(self):

        # Создание холста
        _temp_canvas = Canvas(self._window, width=400, height=400, bg="lightgrey",
                             cursor="pencil")

        # Переход от виртуального к реальному
        self._canvas_field = _temp_canvas

        # Обновление холста
        self.update()

    # Обновление изображения на холсте
    def update(self):
        # Полная очистка холста
        self._canvas_field.delete("all")

        # Отрисовка фона
        self._canvas_field = Canvas(self._window, width=400, height=400, bg="lightgrey",
                             cursor="pencil")

        # # Отрисовка деталей
        # for temp_detail in self.operation_data.details:
        #     print("Рисуется ->")
        #     temp_detail.draw(self.canvas)

        # Упаковка
        self._canvas_field.grid(row=0, column=3, columnspan=10, rowspan=10)

