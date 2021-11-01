"""
    Файл с реализацией объект Interface -
    взимодействие пользователя с программой
"""

# Подключение конфигурации


# Подключение наследуемых модулей
import interface.canvas_field
import interface.controller
import interface.window


# Объект взаимодействия пользователя с программой
class Interface:
    # Данные интерфейса
    _window, _canvas_field, _controller = None, None, None

    # Операционные данные работы пользователя
    _operation_data = None

    # Инициализация интерфейса
    def __init__(self):
        # Инициализация окна, холста и панели управления
        self._window = interface.window.Window()
        self._canvas_field = interface.canvas_field.CanvasField(self._window.get_window())
        self._controller = interface.controller.Controller()

        # Развертывание элементов
        self._window.setup()
        self._canvas_field.setup()
        self._controller.setup()

        # Запуск окна
        self._window.loop()
