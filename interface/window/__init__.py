from tkinter import Tk

import interface


# Объет окна Windows
import config


class Window:

    # Данные работы
    _window = None

    # Инициализация окна
    def __init__(self):
        super(Window, self).__init__()

    # Запуск окна
    def setup(self):
        # Создание окна
        _temp_window = Tk()

        # Установка параметров окна
        _temp_window.title(config.window_title)

        # Переход от виртуального к реальному
        self._window = _temp_window

    # Получение окна
    def get_window(self):
        return self._window

    # Физическое создание приложения
    def loop(self):
        self._window.mainloop()
