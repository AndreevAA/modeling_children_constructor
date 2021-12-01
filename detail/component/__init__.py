# Объект детали Компонент
from math import radians

import config
import detail.light
import detail.pixel
import detail

class DeepFace:
    face = None
    z_index = None

    def __init__(self, face, z_index):
        self.z_index = z_index
        self.face = face

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
    def __draw_component_face(self, _component_face_vertexes, _light, _operation_axis):

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

        v_0_mid = detail.vertex.Vertex(
            (_polygon_pairs_of_vertexes_space[1][0] + _polygon_pairs_of_vertexes_space[2][0]) / 2,
            (_polygon_pairs_of_vertexes_space[1][1] + _polygon_pairs_of_vertexes_space[2][1]) / 2,
            (_polygon_pairs_of_vertexes_space[1][2] + _polygon_pairs_of_vertexes_space[2][2]) / 2
        )

        v_1_mid = detail.vertex.Vertex(
            (_polygon_pairs_of_vertexes_space[0][0] + _polygon_pairs_of_vertexes_space[2][0]) / 2,
            (_polygon_pairs_of_vertexes_space[0][1] + _polygon_pairs_of_vertexes_space[2][1]) / 2,
            (_polygon_pairs_of_vertexes_space[0][2] + _polygon_pairs_of_vertexes_space[2][2]) / 2
        )

        v_2_mid = detail.vertex.Vertex(
            (_polygon_pairs_of_vertexes_space[1][0] + _polygon_pairs_of_vertexes_space[0][0]) / 2,
            (_polygon_pairs_of_vertexes_space[1][1] + _polygon_pairs_of_vertexes_space[0][1]) / 2,
            (_polygon_pairs_of_vertexes_space[1][2] + _polygon_pairs_of_vertexes_space[0][2]) / 2
        )

        z_0_x = v_0_mid.x - _polygon_pairs_of_vertexes_space[0][0]
        z_0_y = v_0_mid.y - _polygon_pairs_of_vertexes_space[0][1]
        z_0_z = v_0_mid.z - _polygon_pairs_of_vertexes_space[0][2]

        z_1_x = v_1_mid.x - _polygon_pairs_of_vertexes_space[1][0]
        z_1_y = v_1_mid.y - _polygon_pairs_of_vertexes_space[1][1]

        I0x = _polygon_pairs_of_vertexes_space[0][0]
        I0y = _polygon_pairs_of_vertexes_space[0][1]
        I0z = _polygon_pairs_of_vertexes_space[0][2]

        I1x = _polygon_pairs_of_vertexes_space[1][0]
        I1y = _polygon_pairs_of_vertexes_space[1][1]

        x = 0

        if z_0_y * z_1_x - z_1_y * z_0_x != 0:
            x = (z_0_x * (I1y - I1x) + I0x * z_0_y * z_1_x - I1x * z_1_y * z_0_x) / \
                (z_0_y * z_1_x - z_1_y * z_0_x)

        y = I0y

        if z_0_x != 0:
            y = ((x - I0x) * z_0_y) / z_0_x + I0y

        # Текущая интенсивность плоскости
        _temp_face_light_intensive = detail.light.get_intensive(_light, detail.vertex.get_distance(
            detail.vertex.Vertex(
                int(x),
                int(y),
                int(_polygon_pairs_of_vertexes_space[0][2] + _polygon_pairs_of_vertexes_space[1][2] +
                    _polygon_pairs_of_vertexes_space[2][2] / 3)
            ),
            detail.vertex.Vertex(
                _light.x,
                _light.y,
                _light.z
            )
        ))

        r = 255
        g = 0
        b = 0

        rgb = (min(int(r * _temp_face_light_intensive), 255),
               min(int(g * _temp_face_light_intensive), 255),
               min(int(b * _temp_face_light_intensive), 255)
               )

        # # print("rgb:", rgb)

        # # print("_polygon_pairs_of_vertexes: ", _polygon_pairs_of_vertexes)

        # Отрисовка области
        # self._get_canvas().create_polygon(_polygon_pairs_of_vertexes, fill=self._get_component_style().get_color())
        self._get_canvas().create_polygon(_polygon_pairs_of_vertexes, fill=detail.pixel.rgb_to_hex( rgb ))

    # Сортировка по глубине поля
    def _sort_by_z_index(self):
        new_d_comp = self.faces

        i = 0
        for _face in self._component_faces:
            # Список пар координат вершин
            _polygon_pairs_of_vertexes = []
            _polygon_pairs_of_vertexes_space = []

            # y = k*x + b
            min_x = config.ABS_MAX
            max_x = config.ABS_MIN

            min_y = config.ABS_MAX
            max_y = config.ABS_MIN

            # Добавление в список пар координат вершин пар вершин
            for _number_of_vertex in _face:
                # Текущая вершина по позиции
                _vertex = self._component_vertexes[_number_of_vertex]

                min_x = min(min_x, _vertex.get_x_position())
                max_x = max(max_x, _vertex.get_x_position())

                min_y = min(min_y, _vertex.get_y_position())
                max_y = max(max_y, _vertex.get_y_position())

                # Добавление данных текущей вершины
                _polygon_pairs_of_vertexes.append([_vertex.get_x_position(),
                                                   _vertex.get_y_position()])
                _polygon_pairs_of_vertexes_space.append([_vertex.x, _vertex.y, _vertex.z])

            v_0_mid = detail.vertex.Vertex(
                (_polygon_pairs_of_vertexes_space[1][0] + _polygon_pairs_of_vertexes_space[2][0]) / 2,
                (_polygon_pairs_of_vertexes_space[1][1] + _polygon_pairs_of_vertexes_space[2][1]) / 2,
                (_polygon_pairs_of_vertexes_space[1][2] + _polygon_pairs_of_vertexes_space[2][2]) / 2
            )

            v_1_mid = detail.vertex.Vertex(
                (_polygon_pairs_of_vertexes_space[0][0] + _polygon_pairs_of_vertexes_space[2][0]) / 2,
                (_polygon_pairs_of_vertexes_space[0][1] + _polygon_pairs_of_vertexes_space[2][1]) / 2,
                (_polygon_pairs_of_vertexes_space[0][2] + _polygon_pairs_of_vertexes_space[2][2]) / 2
            )

            v_2_mid = detail.vertex.Vertex(
                (_polygon_pairs_of_vertexes_space[1][0] + _polygon_pairs_of_vertexes_space[0][0]) / 2,
                (_polygon_pairs_of_vertexes_space[1][1] + _polygon_pairs_of_vertexes_space[0][1]) / 2,
                (_polygon_pairs_of_vertexes_space[1][2] + _polygon_pairs_of_vertexes_space[0][2]) / 2
            )

            z_0_x = v_0_mid.x - _polygon_pairs_of_vertexes_space[0][0]
            z_0_y = v_0_mid.y - _polygon_pairs_of_vertexes_space[0][1]
            z_0_z = v_0_mid.z - _polygon_pairs_of_vertexes_space[0][2]

            z_1_x = v_1_mid.x - _polygon_pairs_of_vertexes_space[1][0]
            z_1_y = v_1_mid.y - _polygon_pairs_of_vertexes_space[1][1]

            I0x = _polygon_pairs_of_vertexes_space[0][0]
            I0z = _polygon_pairs_of_vertexes_space[0][2]

            I1x = _polygon_pairs_of_vertexes_space[1][0]
            I1y = _polygon_pairs_of_vertexes_space[1][1]

            x = 0

            if z_0_y * z_1_x - z_1_y * z_0_x != 0:
                x = (z_0_x * (I1y - I1x) + I0x * z_0_y * z_1_x - I1x * z_1_y * z_0_x) / \
                    (z_0_y * z_1_x - z_1_y * z_0_x)

            z = I0z

            if z_0_x != 0:
                z = ((x - I0x) * z_0_z) / z_0_x + I0z

            z_index = z

            new_d_comp[i] = DeepFace(new_d_comp[i], z_index)
            i += 1

        # print(new_d_comp)

        new_d_comp = sorted(new_d_comp, key=lambda d_face: d_face.z_index)

        # print("--")
        # print("len(new_d_comp)", len(new_d_comp))
        for i in range(len(new_d_comp)):
            # print("new_d_comp[i].z_index: ", new_d_comp[i].z_index)
            self._component_faces[i] = new_d_comp[i].face



    # Прототип функции отрисовки компоненты
    def draw(self, _canvas, _light, _operation_axis):

        self._sort_by_z_index()

        # Установка холста рисования
        self.set_component_canvas(_canvas)

        # Установка позиции на холсте рисования
        self.set_component_position(self._component_position)

        # Статус отрисовки компоненты
        _error_status = None

        # Проход по всем наборам граней
        for _component_face_vertexes in self.get_component_faces():
            self.__draw_component_face(_component_face_vertexes, _light, _operation_axis)

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

    @name.setter
    def name(self, value):
        self._component_name = value

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


class Cylinder(Component):

    _radius = None
    _number_of_steps = None

    _f_pos = None
    _height = None

    def __init__(self, _component_style, _component_vertexes, _component_faces,
                 _radius, _number_of_steps, _f_pos, height, _component_name):
        super().__init__(_component_style, _component_vertexes, _component_faces)

        # Позиция координат координаты
        self._f_pos = _f_pos
        self._height = height

        self._component_name = _component_name

        self._component_name = _component_name

        self._component_vertexes = []
        self._component_faces = []

        self._number_of_steps = _number_of_steps

        self._radius = _radius

        degree_step = 360 / _number_of_steps

        f_base_point = detail.vertex.Vertex(
            _f_pos.x,
            _f_pos.y,
            _f_pos.z
        )

        s_base_point = detail.vertex.Vertex(
            f_base_point.x,
            f_base_point.y,
            f_base_point.z + height
        )

        f_pivot_point = detail.vertex.Vertex(
            f_base_point.x + self._radius,
            f_base_point.y,
            f_base_point.z
        )

        s_pivot_point = detail.vertex.Vertex(
            s_base_point.x + self._radius,
            s_base_point.y,
            s_base_point.z
        )

        self._component_vertexes.append(f_base_point)
        self._component_vertexes.append(s_base_point)

        self._component_vertexes.append(f_pivot_point)
        self._component_vertexes.append(s_pivot_point)

        for _t_step in range(self._number_of_steps):

            rotation_degree = radians(float(_t_step * degree_step))

            f_new_vertex = detail.vertex.rotate_vertex_by_base_vertex(
                f_pivot_point, f_base_point, config.AXIS_Z, rotation_degree
            )

            s_new_vertex = detail.vertex.rotate_vertex_by_base_vertex(
                s_pivot_point, s_base_point, config.AXIS_Z, rotation_degree
            )

            self._component_vertexes.append(f_new_vertex)
            self._component_vertexes.append(s_new_vertex)

            self._component_faces.append([
                len(self._component_vertexes) - 1,
                len(self._component_vertexes) - 4,
                len(self._component_vertexes) - 2,
            ])

            self._component_faces.append([
                len(self._component_vertexes) - 2,
                len(self._component_vertexes) - 3,
                len(self._component_vertexes) - 4,
            ])

            self._component_faces.append([
                len(self._component_vertexes) - 3,
                len(self._component_vertexes) - 4,
                1
            ])

            self._component_faces.append([
                len(self._component_vertexes) - 1,
                len(self._component_vertexes) - 3,
                0
            ])

        self._component_faces.append([
            1,
            3,
            len(self._component_vertexes) - 2,
        ])

        self._component_faces.append([
            2,
            0,
            len(self._component_vertexes) - 1,
        ])

        self._component_faces.append([
            3,
            len(self._component_vertexes) - 1,
            2
        ])

        self._component_faces.append([
            2,
            len(self._component_vertexes) - 2,
            len(self._component_vertexes) - 1
        ])


        # # print("self._component_faces: ", self._component_faces)




