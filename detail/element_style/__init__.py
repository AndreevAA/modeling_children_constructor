# Объект стиля элемента
class ElementStyle:

    # Цвет элемента
    _color = None

    # Инициализация объекта
    def __init__(self, _color):
        self._color = _color

    # Получение цвета элемента
    def get_color(self):
        return self._color

    # Обновление цвета элемента
    def update_color(self, _color):
        self._color = _color

    @property
    def color(self):
        return self._color
