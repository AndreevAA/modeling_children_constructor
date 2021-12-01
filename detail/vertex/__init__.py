# Зуммирование точки относительно точки
import math
from math import cos, sin

import config
import detail


# Определение расстояния между точками
def get_distance(_f_vertex, _s_vertex):
    return math.sqrt((_s_vertex.x - _f_vertex.x) ** 2 +
                     (_s_vertex.y - _f_vertex.y) ** 2 +
                     (_s_vertex.z - _f_vertex.z) ** 2) ** 2


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


# Поворот точки относительно точки
def rotate_vertex_by_base_vertex(pivot_point, base_point, rotation_way, rotation_degree):

    # print("\n-->")
    # print("base_point: ", base_point.x, base_point.y, base_point.z)
    # print("rotation_way = ", rotation_way)
    # print("HERE")
    # print(rotation_degree)
    # print("rotation_degree = ", rotation_degree, "sin(rotation_degree) = ", sin(rotation_degree),
    #       "cos(rotation_degree)", cos(rotation_degree))

    # print("pivot_point: ", pivot_point.x, pivot_point.y, pivot_point.z)

    # Смещение оси поворота
    result_point = detail.vertex.Vertex(pivot_point.x - base_point.x,
                                        pivot_point.y - base_point.y,
                                        pivot_point.z - base_point.z)

    # Координату повернутой точки
    x_rotated_result_point = None
    y_rotated_result_point = None
    z_rotated_result_point = None

    # Выявление оси и смена значений
    if rotation_way == config.AXIS_X:
        x_rotated_result_point = result_point.x
        y_rotated_result_point = result_point.y * cos(rotation_degree) - \
                                 result_point.z * sin(rotation_degree)
        z_rotated_result_point = result_point.y * sin(rotation_degree) + \
                                 result_point.z * cos(rotation_degree)

    elif rotation_way == config.AXIS_Y:
        x_rotated_result_point = result_point.x * cos(rotation_degree) + \
                                 result_point.z * sin(rotation_degree)
        y_rotated_result_point = result_point.y
        z_rotated_result_point = - result_point.x * sin(rotation_degree) + \
                                 result_point.z * cos(rotation_degree)
        # result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)

    elif rotation_way == config.AXIS_Z:
        x_rotated_result_point = result_point.x * cos(rotation_degree) - \
                                 result_point.y * sin(rotation_degree)
        y_rotated_result_point = result_point.x * sin(rotation_degree) + \
                                 result_point.y * cos(rotation_degree)
        z_rotated_result_point = result_point.z
        # result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)

    # print("x_rotated_result_point, y_rotated_result_point, z_rotated_result_point: ", x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)

    # Обновление координат в виртуальной точке
    # result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)

    # Возврат оси поворота
    result_point = detail.vertex.Vertex(x_rotated_result_point + base_point.x,
                                        y_rotated_result_point + base_point.y,
                                        z_rotated_result_point + base_point.z)

    # print("result_point: ", result_point.x, result_point.y, result_point.z)
    # print("<--\n")

    return result_point


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
