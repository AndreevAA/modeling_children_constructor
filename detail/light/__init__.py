
# Определение интенсивности
import detail


def get_intensive(_light, _distance):
    return _light.power / (_distance ** 2)


# Объект источника света
class Light:
    # Позиция света
    _position = None

    # Мощность света
    _power = None

    def __init__(self, _position, _power):
        self._power = _power
        self._position = _position

    @property
    def x(self):
        return self._position.x

    @property
    def y(self):
        return self._position.y

    @property
    def z(self):
        return self._position.z

    @x.setter
    def x(self, value):
        self._position.x = value

    @y.setter
    def y(self, value):
        self._position.y = value

    @z.setter
    def z(self, value):
        self._position.z = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def move(self, x, y, z):
        self.position.x += x
        self.position.y += y
        self.position.z += z

        print("LIGHT: ", self.position.x, self.position.y, self.position.z)
        print("POWER: ", self.power)

    def zoom(self, _base_vertex, _zoom_coefficient):
        self._position = detail.vertex.zoom_vertex_by_base_vertex(self._position,
                                                           _base_vertex,
                                                           _zoom_coefficient)

    def rotate(self, _base_vertex, _rotation_way_axis, _scene_degree):
        result_point = detail.vertex.rotate_vertex_by_base_vertex(self._position, _base_vertex,
                                                                  _rotation_way_axis, _scene_degree)
        self._position.update(result_point.get_x_position(),
                              result_point.get_y_position(),
                              result_point.get_z_position())
