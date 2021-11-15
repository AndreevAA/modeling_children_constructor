# Объект операционных данных деталей
from math import sin, cos

import config
import detail


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


class OperationAxis:

    x_axis = Axis()
    y_axis = Axis()
    z_axis = Axis()

    def __init__(self):

        # Установка дефолтных значений
        self.set_default_coordinates()

    def set_default_coordinates(self):
        self.x_axis.set_first_vertex(
            detail.vertex.Vertex(-10000, 0, 0)
        )
        self.x_axis.set_second_vertex(
            detail.vertex.Vertex(+10000, 0, 0)
        )

        self.y_axis.set_first_vertex(
            detail.vertex.Vertex(0, -10000, 0)
        )
        self.y_axis.set_second_vertex(
            detail.vertex.Vertex(0, +10000, 0)
        )

        self.z_axis.set_first_vertex(
            detail.vertex.Vertex(0, 0, -10000)
        )
        self.z_axis.set_second_vertex(
            detail.vertex.Vertex(0, 0, +10000)
        )

    def draw(self, _canvas_field):

        print(self.x_axis.get_first_vertex().get_x_position(),
                                  self.x_axis.get_first_vertex().get_y_position(),
                                    "  :  ",
                                  self.x_axis.get_second_vertex().get_x_position(),
                                  self.x_axis.get_second_vertex().get_y_position())

        _canvas_field.create_line(self.x_axis.get_first_vertex().get_x_position(),
                                  self.x_axis.get_first_vertex().get_y_position(),
                                  self.x_axis.get_second_vertex().get_x_position(),
                                  self.x_axis.get_second_vertex().get_y_position()
                                  )

        _canvas_field.create_line(self.y_axis.get_first_vertex().get_x_position(),
                                  self.y_axis.get_first_vertex().get_y_position(),
                                  self.y_axis.get_second_vertex().get_x_position(),
                                  self.y_axis.get_second_vertex().get_y_position()
                                  )
        #
        # _canvas_field.create_line(self.x_axis.get_first_vertex().get_x_position(),
        #                           self.x_axis.get_first_vertex().get_y_position(),
        #                           self.x_axis.get_second_vertex().get_x_position(),
        #                           self.x_axis.get_second_vertex().get_y_position()
        #                           )


    def move(self, x, y, z):
        self.x_axis.move(x, y, z)
        self.y_axis.move(x, y, z)
        self.z_axis.move(x, y, z)

