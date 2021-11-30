# Объект детали Компонент
import config
import detail.light
import detail.pixel

class Component:

    # Название компонента
    _component_name = None

    # Стиль компонента
    _component_style = None

    # Позиция компоненты
    _component_position = None

    # Описание вершин компоненты
    _component_vertexes = None

    # Описание граней компоненты
    _component_faces = None

    # Холст для отрисовки
    _canvas = None

    # Инициализация объекта компоненты
    def __init__(self, _component_style,
                 _component_vertexes, _component_faces):

        # Передача стилистических особенностей компоненты
        self._component_style = _component_style

        # Передача вершин компоненты
        self._component_vertexes = _component_vertexes

        # Передача граней компоненты
        self._component_faces = _component_faces

    # Установка холста компоненты
    def set_component_canvas(self, _canvas):
        self._canvas = _canvas

    # Установка позиции компоненты на холсте
    def set_component_position(self, _component_position):
        self._component_position = _component_position

    # Получение списка вершин
    def get_component_vertexes(self):
        return self._component_vertexes

    # Получение списка граней
    def get_component_faces(self):
        return self._component_faces

    # Отрисовка грани компоненты
    def __draw_component_face(self, _component_face_vertexes, _light):

        # Список пар координат вершин
        _polygon_pairs_of_vertexes = []
        _polygon_pairs_of_vertexes_space = []

        # y = k*x + b
        min_x = config.ABS_MAX
        max_x = config.ABS_MIN

        min_y = config.ABS_MAX
        max_y = config.ABS_MIN

        # Добавление в список пар координат вершин пар вершин
        for _number_of_vertex in _component_face_vertexes:

            # Текущая вершина по позиции
            _vertex = self.get_component_vertexes()[int(_number_of_vertex)]

            min_x = min(min_x, _vertex.get_x_position())
            max_x = max(max_x, _vertex.get_x_position())

            min_y = min(min_y, _vertex.get_y_position())
            max_y = max(max_y, _vertex.get_y_position())

            # Добавление данных текущей вершины
            _polygon_pairs_of_vertexes.append([_vertex.get_x_position(),
                                               _vertex.get_y_position()])
            _polygon_pairs_of_vertexes_space.append([_vertex.x, _vertex.y, _vertex.z])

        print("_polygon_pairs_of_vertexes: ", _polygon_pairs_of_vertexes)

        # # pixels = []
        # #
        # # for i in range(config.ABS_MAX ** 2):
        # #     r_p = []
        # #     for j in range(config.ABS_MAX):
        # #         r_p.append(None)
        # #     pixels.append(r_p)
        # #
        # # for i in range(0, len(_polygon_pairs_of_vertexes) - 1):
        # #     y1 = int(_polygon_pairs_of_vertexes[i][1])
        # #     y2 = int(_polygon_pairs_of_vertexes[i + 1][1])
        # #     x1 = _polygon_pairs_of_vertexes[i][0]
        # #     x2 = _polygon_pairs_of_vertexes[i + 1][0]
        # #
        # #     if -y1 + y2 != 0 and (x1 - x2) != 0:
        # #         k = (-y1 + y2) / (x1 - x2)
        # #         b = k * x1 - y1
        # #
        # #         for y in range(y1, y2 + 1):
        # #             x = (y - b) / k
        # #
        # #             for t_x in range(int(x), int(max_x)):
        # #                 if pixels[y][t_x] is None:
        # #                     pixels[y][t_x] = self._get_component_style().get_color()
        # #                 else:
        # #                     pixels[y][t_x] = None
        # #             self._get_canvas().create_line(x, y, x, y, fill=self._get_component_style().get_color())
        #     # else:
        #     #     for y in range(y1, y2 + 1):
        #     #         x = (y - b) / k
        #     #
        #     #         for t_x in range(x, max_x):
        #     #             if pixels[y][t_x] is None:
        #     #                 pixels[y][t_x] = self._get_component_style().get_color()
        #     #             else:
        #     #                 pixels[y][t_x] = None
        #     #         self._get_canvas().create_line(x, y, x, y, fill=self._get_component_style().get_color())
        #
        # for y in range(int(min_y), int(max_y)):
        #     for x in range(int(min_x), int(max_x)):
        #         if pixels[y][x] is not None:
        #             self._get_canvas().create_line(x, y, x, y, fill=self._get_component_style().get_color())

        #
        # for x in range(min_x, max_x):

        # Текущая интенсивность плоскости
        _temp_face_light_intensive = detail.light.get_intensive(_light, detail.vertex.get_distance(
            detail.vertex.Vertex(
                int(_polygon_pairs_of_vertexes_space[0][0] + _polygon_pairs_of_vertexes_space[1][0] + _polygon_pairs_of_vertexes_space[2][0] / 3),
                int(_polygon_pairs_of_vertexes_space[0][1] + _polygon_pairs_of_vertexes_space[1][1] +
                    _polygon_pairs_of_vertexes_space[2][1] / 3),
                int(_polygon_pairs_of_vertexes_space[0][2] + _polygon_pairs_of_vertexes_space[1][2] +
                    _polygon_pairs_of_vertexes_space[2][2] / 3)
            ), _light.position
        ))

        # print("_temp_face_light_intensive = ", _temp_face_light_intensive)

        r = 255
        g = 0
        b = 0

        rgb = (min(int(r * _temp_face_light_intensive), 255),
               min(int(g * _temp_face_light_intensive), 255),
               min(int(b * _temp_face_light_intensive), 255)
               )

        print("rgb:", rgb)

        # Отрисовка области
        # self._get_canvas().create_polygon(_polygon_pairs_of_vertexes, fill=self._get_component_style().get_color())
        self._get_canvas().create_polygon(_polygon_pairs_of_vertexes, fill=detail.pixel.rgb_to_hex( rgb ))


    # Прототип функции отрисовки компоненты
    def draw(self, _canvas, _light):

        # Установка холста рисования
        self.set_component_canvas(_canvas)

        # Установка позиции на холсте рисования
        self.set_component_position(self._component_position)

        # Статус отрисовки компоненты
        _error_status = None

        # Проход по всем наборам граней
        for _component_face_vertexes in self.get_component_faces():
            self.__draw_component_face(_component_face_vertexes, _light)

        _error_status = config.SUCCESS_STATUS

        return config.ERROR_STATUS

    # Получение холста
    def _get_canvas(self):
        return self._canvas

    # Получение названия компоненты
    def _get_component_name(self):
        return self._component_name

    # Получение стиля компоненты
    def _get_component_style(self):
        return self._component_style

    # Получение позиции компоненты
    def _get_component_position(self):
        return self._component_position

    @property
    def name(self):
        return self._component_name

    @property
    def style(self):
        return self._component_style

    @property
    def faces(self):
        return self._component_faces

    @property
    def vertexes(self):
        return self._component_vertexes

    @property
    def position(self):
        return self._component_position

