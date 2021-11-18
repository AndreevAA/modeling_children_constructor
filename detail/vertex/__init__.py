# Зуммирование точки относительно точки
def zoom_vertex_by_base_vertex(vertex, base_vertex, zoom_coefficient):

    # Результирующая точка после зуммирования
    result_vertex = vertex

    # Определение разницы
    x_delta = vertex.x - base_vertex.x
    y_delta = vertex.y - base_vertex.y
    z_delta = vertex.z - base_vertex.z

    # Непосредственная операция зуммирования
    result_vertex.x = base_vertex.x + x_delta * zoom_coefficient
    result_vertex.y = base_vertex.y + y_delta * zoom_coefficient
    result_vertex.z = base_vertex.z + z_delta * zoom_coefficient

    return result_vertex

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

    @property
    def x(self):
        return self._x_position

    @property
    def y(self):
        return self._y_position

    @property
    def z(self):
        return self._z_position

    @x.setter
    def x(self, value):
        self._x_position = value

    @y.setter
    def y(self, value):
        self._y_position = value

    @z.setter
    def z(self, value):
        self._z_position = value

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
        self.update_x_position(_x_position)
        self.update_y_position(_y_position)
        self.update_z_position(_z_position)

    # Обновление позиции по координаты X
    def update_x_position(self, _x_position):
        self._x_position = _x_position

    # Обновление позиции по координаты X
    def update_y_position(self, _y_position):
        self._y_position = _y_position

    # Обновление позиции по координаты X
    def update_z_position(self, _z_position):
        self._z_position = _z_position
