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
    _operation_axis = None
    _operation_light = None

    # Инициализация интерфейса
    def __init__(self, _operation_data, _operation_axis, _operation_light):
        # Передача данных работы
        self._operation_data = _operation_data
        self._operation_axis = _operation_axis
        self._operation_light = _operation_light

        # Инициализация окна, холста и панели управления
        self._window = interface.window.Window()
        self._canvas_field = interface.canvas_field.CanvasField(self._window.get_window())

        self._controller = interface.controller.Controller(self._operation_data, self._operation_axis,
                                                           self._operation_light,
                                                           self._window, self._canvas_field)

        # Развертывание элементов
        self._window.setup()
        self._canvas_field.setup(self._operation_data, self._operation_axis, self._operation_light)
        self._controller.setup()

        # Запуск окна
        self._window.loop()
