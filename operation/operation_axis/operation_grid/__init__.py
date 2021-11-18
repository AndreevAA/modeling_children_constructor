import config


# Объект delta между линиями
import detail.vertex


class DeltaGrid:
    __delta_grid_m = None  # Математический численный шаг между линиями
    __delta_grid_p = None  # Шаг на экране

    def __init__(self, __delta_grid_m, __delta_grid_p):
        self.__delta_grid_m = __delta_grid_m
        self.__delta_grid_p = __delta_grid_p

    @property
    def delta_grid_m(self):
        return self.__delta_grid_m

    @delta_grid_m.setter
    def delta_grid_m(self, value):
        self.__delta_grid_m = value

    @delta_grid_m.deleter
    def delta_grid_m(self):
        del self.__delta_grid_m

    @property
    def delta_grid_p(self):
        return self.__delta_grid_p

    @delta_grid_p.setter
    def delta_grid_p(self, value):
        self.__delta_grid_p = value

    @delta_grid_p.deleter
    def delta_grid_p(self):
        del self.__delta_grid_p


# Объект линии сетки
class Line:
    # Координаты концов линии
    __first_vertex = None
    __second_vertex = None

    # Цвет линии
    __color = None
    __width = None

    def __init__(self, _color, _width):
        self.__color = _color
        self.__width = _width

    def move(self, x, y, z):
        self.__first_vertex = detail.vertex.Vertex(
            self.__first_vertex.get_x_position() + x,
            self.__first_vertex.get_y_position() + y,
            self.__first_vertex.get_z_position() + z
        )

        self.__second_vertex = detail.vertex.Vertex(
            self.__second_vertex.get_x_position() + x,
            self.__second_vertex.get_y_position() + y,
            self.__second_vertex.get_z_position() + z
        )

    @property
    def first_vertex(self):
        return self.__first_vertex

    @first_vertex.setter
    def first_vertex(self, value):
        self.__first_vertex = value

    @property
    def second_vertex(self):
        return self.__second_vertex

    @second_vertex.setter
    def second_vertex(self, value):
        self.__second_vertex = value

    @property
    def color(self):
        return self.__color

    @property
    def width(self):
        return self.__width

    def draw(self, canvas_field):
        print()
        print(self.first_vertex.x,
                                 self.first_vertex.y,
                                 self.second_vertex.x,
                                 self.second_vertex.y)
        canvas_field.create_line(self.first_vertex.get_x_position(),
                                 self.first_vertex.get_y_position(),
                                 self.second_vertex.get_x_position(),
                                 self.second_vertex.get_y_position(),
                                 fill=self.color,
                                 width=self.width
                                 )


# Объект линий сетки
class LinesGrid:
    # Настройки отображений
    __delta_grid = None

    # Массив линий сетки
    __lines_grid = None

    # Цвет линии
    __color = None
    __width = None

    # Axis / Ось
    __axis = None

    def __init__(self, axis, delta_grid, _color, _width):
        self.__axis = axis
        self.__delta_grid = delta_grid
        self.__color = _color
        self.__width = _width

        self.initialize_lines_grid()

    def initialize_lines_grid(self):
        lines_grid = []

        number_of_lines_grid = (config.ABS_MAX - config.ABS_MIN) // self.delta_grid.delta_grid_m

        first_vertex = None
        second_vertex = None

        if self.axis == config.AXIS_X:
            first_vertex = detail.vertex.Vertex(0, config.ABS_MIN, config.ABS_MIN)
            second_vertex = detail.vertex.Vertex(0, config.ABS_MIN, config.ABS_MAX)
        elif self.axis == config.AXIS_Y:
            first_vertex = detail.vertex.Vertex(config.ABS_MIN, 0, config.ABS_MIN)
            second_vertex = detail.vertex.Vertex(config.ABS_MIN, 0, config.ABS_MAX)
        elif self.axis == config.AXIS_Z:
            first_vertex = detail.vertex.Vertex(config.ABS_MIN, config.ABS_MIN, 0)
            second_vertex = detail.vertex.Vertex(config.ABS_MIN, config.ABS_MAX, 0)

        for number_of_line in range(number_of_lines_grid):

            # Инициализируется виртуальная линия
            line = Line(self.color, self.width)

            # Выставляются координаты концов лини
            line.first_vertex = detail.vertex.Vertex(first_vertex.x, first_vertex.y, second_vertex.z)
            line.second_vertex = detail.vertex.Vertex(second_vertex.x, second_vertex.y, second_vertex.z)

            # Линия добавляется в виртуальный список линий
            lines_grid.append(line)

            # Плоскость линий перпендикулярна X, Z неизменно, меняется Y
            if self.axis == config.AXIS_X:
                first_vertex.y = first_vertex.y + self.delta_grid.delta_grid_m
                second_vertex.y = second_vertex.y + self.delta_grid.delta_grid_m

            # Плоскость линий перпендикулярна Y, Z неизменно, меняется X
            elif self.axis == config.AXIS_Y:
                first_vertex.x = first_vertex.x + self.delta_grid.delta_grid_m
                second_vertex.x = second_vertex.x + self.delta_grid.delta_grid_m

            # Плоскость линий перпендикулярна Z, Y неизменно, меняется X
            elif self.axis == config.AXIS_Z:
                first_vertex.x = first_vertex.x + self.delta_grid.delta_grid_m
                second_vertex.x = second_vertex.x + self.delta_grid.delta_grid_m

        self.__lines_grid = lines_grid

    def move(self, x, y, z):
        for line in self.__lines_grid:
            line.move(x, y, z)

    @property
    def color(self):
        return self.__color

    @property
    def width(self):
        return self.__width

    @property
    def axis(self):
        return self.__axis

    @property
    def delta_grid(self):
        return self.__delta_grid

    @property
    def lines_grid(self):
        return self.__lines_grid

    @lines_grid.setter
    def lines_grid(self, value):
        self.__lines_grid = value

    def draw(self, canvas_field):
        for line in self.__lines_grid:
            line.draw(canvas_field)


# Объект операционной сетки
class OperationGrid:
    # Delta сетки
    __delta_grid = None

    # Линии сетки
    __lines_grid = None

    # Axis / Ось
    __axis = None

    def __init__(self, axis):
        self.__axis = axis

        # Инициализация объекта delta сетки с настройками по умолчанию
        self.__delta_grid = DeltaGrid(config.DELTA_GRID_M, config.DELTA_GRID_P)

        # Инициализация объекта линий сетки
        self.__lines_grid = LinesGrid(self.axis, self.delta_grid, config.GRID_LINE_COLOR, config.GRID_LINE_WIDTH)

    @property
    def axis(self):
        return self.__axis

    @property
    def delta_grid(self):
        return self.__delta_grid

    @property
    def lines_grid(self):
        return self.__lines_grid

    def move(self, x, y, z):
        self.__lines_grid.move(x, y, z)

    # Отрисовка сетки
    def draw(self, canvas_field):
        self.__lines_grid.draw(canvas_field)

    def zoom(self, base_vertex, zoom_coefficient):
        self.delta_grid.delta_grid_m = self.delta_grid.delta_grid_m * zoom_coefficient
