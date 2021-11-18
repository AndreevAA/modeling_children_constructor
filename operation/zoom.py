import config


class CanvasMiddle:

    # Координаты позиции середины холста
    _x_position = None
    _y_position = None

    def __init__(self):
        

    @property
    def x(self):
        return self._x_position

    @property
    def y(self):
        return self._y_position


# Объект зуммирования
class Zoom:
    # Операционные данные
    _operation_objects = None

    # Середина холста
    _canvas_middle = None

    def __init__(self, _operation_objects):
        self.operation_objects = _operation_objects
        self._canvas_middle =

    @property
    def operation_objects(self):
        return self._operation_objects

    @operation_objects.setter
    def operation_objects(self, value):
        self.operation_objects = value

    def zoom_operation_axis(self):
        print()

    def zoom_operation_detail(self):
        print()
