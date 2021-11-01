# Объект точки в пространстве
class Vertex:

    # Приватные поля координаты точки
    _x_position = None
    _y_position = None
    _z_position = None

    # Инициализация объекта точки
    def __init__(self, _x_position, _y_position, _z_position):
        self._x_position = _x_position
        self._y_position = _y_position
        self._z_position = _z_position

    # Получение значения координаты точки по оси Х
    def get_x_position(self):
        return self._x_position

    # Получение значения координаты по оси Y
    def get_y_position(self):
        return self._y_position

    # Получение значения координаты по оси Z
    def get_z_position(self):
        return self._z_position

    # Общее обновление позиции по осям
    def update(self, _x_position, _y_position, _z_position):
        self._update_x_position(_x_position)
        self._update_y_position(_y_position)
        self._update_z_position(_z_position)

    # Обновление позиции по координаты X
    def _update_x_position(self, _x_position):
        self._x_position = _x_position

    # Обновление позиции по координаты X
    def _update_y_position(self, _y_position):
        self._y_position = _y_position

    # Обновление позиции по координаты X
    def _update_z_position(self, _z_position):
        self._z_position = _z_position
