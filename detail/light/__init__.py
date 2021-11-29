
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
        self._power = value
