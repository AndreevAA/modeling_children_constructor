# Объект операционных данных деталей
from math import sin, cos

import config
import detail
import operation.operation_axis.operation_grid


class Axis:
    _first_vertex = None
    _second_vertex = None

    def __init__(self):
        self._first_vertex = detail.vertex.Vertex(0, 0, 0)
        self._second_vertex = detail.vertex.Vertex(0, 0, 0)

    def set_vertexes(self, _first_vertex, _second_vertex):
        self.set_first_vertex(_first_vertex)
        self.set_second_vertex(_second_vertex)

    def set_first_vertex(self, _first_vertex):
        self._first_vertex = _first_vertex

    def set_second_vertex(self, _second_vertex):
        self._second_vertex = _second_vertex

    def get_first_vertex(self):
        return self._first_vertex

    def get_second_vertex(self):
        return self._second_vertex

    def move(self, x, y, z):
        _first_vertex = detail.vertex.Vertex(
            self._first_vertex.get_x_position() + x,
            self._first_vertex.get_y_position() + y,
            self._first_vertex.get_z_position() + z
        )

        _second_vertex = detail.vertex.Vertex(
            self._second_vertex.get_x_position() + x,
            self._second_vertex.get_y_position() + y,
            self._second_vertex.get_z_position() + z
        )

        self.set_first_vertex(_first_vertex)
        self.set_second_vertex(_second_vertex)

    @property
    def first_vertex(self):
        return self._first_vertex

    @property
    def second_vertex(self):
        return self.second_vertex

    def draw(self, _canvas_field):
        _canvas_field.create_line(self._first_vertex.get_x_position(),
                                  self._first_vertex.get_y_position(),
                                  self._second_vertex.get_x_position(),
                                  self._second_vertex.get_y_position()
                                  )


class OperationAxes:
    _x_axis = Axis()
    _y_axis = Axis()
    _z_axis = Axis()

    def __init__(self):
        # Установка дефолтных значений
        self.set_default_coordinates()

    @property
    def x(self):
        return self._x_axis

    @property
    def y(self):
        return self._y_axis

    @property
    def z(self):
        return self._z_axis

    def set_default_coordinates(self):
        self._x_axis.set_first_vertex(
            detail.vertex.Vertex(config.ABS_MIN, 0, 0)
        )
        self._x_axis.set_second_vertex(
            detail.vertex.Vertex(config.ABS_MAX, 0, 0)
        )

        self._y_axis.set_first_vertex(
            detail.vertex.Vertex(0, config.ABS_MIN, 0)
        )
        self._y_axis.set_second_vertex(
            detail.vertex.Vertex(0, config.ABS_MAX, 0)
        )

        self._z_axis.set_first_vertex(
            detail.vertex.Vertex(0, 0, config.ABS_MIN)
        )
        self._z_axis.set_second_vertex(
            detail.vertex.Vertex(0, 0, config.ABS_MAX)
        )

    def move(self, x, y, z):
        self._x_axis.move(x, y, z)
        self._y_axis.move(x, y, z)
        self._z_axis.move(x, y, z)

    def draw(self, canvas_field):
        self._x_axis.draw(canvas_field)
        self._y_axis.draw(canvas_field)
        self._z_axis.draw(canvas_field)

    def zoom(self, base_vertex, zoom_coefficient, _axes_intersection):
        if base_vertex == _axes_intersection:
            pass


class OperationGrids:
    _x_grid = operation_grid.OperationGrid(config.AXIS_X)
    _y_grid = operation_grid.OperationGrid(config.AXIS_Y)
    _z_grid = operation_grid.OperationGrid(config.AXIS_Z)

    def draw(self, canvas_field):
        print("X: ")
        self._x_grid.draw(canvas_field)
        print("---\nY: ")
        self._y_grid.draw(canvas_field)
        print("---\nZ: ")
        self._z_grid.draw(canvas_field)

    def move(self, x, y, z):
        self._x_grid.move(x, y, z)
        self._y_grid.move(x, y, z)
        self._z_grid.move(x, y, z)

    def zoom(self, base_vertex, zoom_coefficient):
        self._x_grid.zoom(base_vertex, zoom_coefficient)
        self._y_grid.zoom(base_vertex, zoom_coefficient)
        self._z_grid.zoom(base_vertex, zoom_coefficient)


class AxesIntersection:
    __intersection_vertex = None

    def __init__(self):
        self.set_default_intersection_vertex()

    def set_default_intersection_vertex(self):
        self.intersection_vertex = detail.vertex.Vertex(
            0, 0, 0
        )

    @property
    def intersection_vertex(self):
        return self.__intersection_vertex

    @intersection_vertex.setter
    def intersection_vertex(self, value):
        self.__intersection_vertex = value

    def move(self, x, y, z):
        self.intersection_vertex = detail.vertex.Vertex(
            self.intersection_vertex.x + x,
            self.intersection_vertex.y + y,
            self.intersection_vertex.z + z
        )


class OperationAxis:
    _operation_axes = OperationAxes()
    _axes_intersection = AxesIntersection()
    _operation_grids = OperationGrids()

    @property
    def axes_intersection(self):
        return self._axes_intersection

    def draw(self, _canvas_field):
        self._operation_axes.draw(_canvas_field)
        self._operation_grids.draw(_canvas_field)

    def move(self, x, y, z):
        self._operation_axes.move(x, y, z)
        self._axes_intersection.move(x, y, z)
        self._operation_grids.move(x, y, z)

    def zoom(self, base_vertex, zoom_coefficient):
        self._operation_axes.zoom(base_vertex, zoom_coefficient, self._axes_intersection)
        self._operation_grids.zoom(base_vertex, zoom_coefficient)
