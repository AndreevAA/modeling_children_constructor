"""
    Базовый файл объекта детали,
    состоящей из
"""

# Объект детали
from random import randint

import config
import detail.element_style
from detail import vertex
from detail.component import Component


class Deep:
    component = None
    z_index = None

    def __init__(self, _component, _z_index):
        self.z_index = _z_index
        self.component = _component


class Detail:
    # Данные о детали
    _detail_name = None

    # Позиция детали в пространстве
    _detail_position = None

    # Массив компонентов детали
    _detail_components = None

    # Стиль детали
    _detail_style = None

    # Адрес детали
    _detail_uid = None

    # Инициализация объекта Детали
    def __init__(self, _detail_name):
        # Установка имени детали
        self._detail_name = _detail_name

        # Установка базовой позиции детали
        self._set_basic_detail_position()

    @property
    def name(self):
        return self._detail_name

    @name.setter
    def name(self, value):
        self._detail_name = value

    @property
    def position(self):
        return self._detail_position

    @position.setter
    def position(self, value):
        self._detail_position = value

    @property
    def components(self):
        return self._detail_components

    @components.setter
    def components(self, value):
        self._detail_components = value

    @property
    def style(self):
        return self._detail_style

    @style.setter
    def style(self, value):
        self._detail_style = value

    @property
    def uid(self):
        return self._detail_uid

    @uid.setter
    def uid(self, value):
        self._detail_uid = value

    # Получение компоенентов детали
    def get_detail_components(self):
        return self._detail_components

    # Установка компонентов детали
    def set_detail_components(self, _detail_components):
        self._detail_components = _detail_components

    # Установка стиля детали
    def set_detail_style(self, _detail_style):
        self._detail_style = _detail_style

    # Обновление позиции детали
    def update_detail_position(self, _detail_position):
        self._detail_position = _detail_position

    # Получить базовую позицию детали
    def _set_basic_detail_position(self):
        self.update_detail_position(vertex.Vertex(config.ZERO_NUMBER, config.ZERO_NUMBER, config.ZERO_NUMBER))

    # Получение названия детали
    def get_detail_name(self):
        return self._detail_name

    def _sort_by_z_index(self):
        new_d_comp = self._detail_components

        for i in range(len(new_d_comp)):
            z_index = -config.ABS_MIN

            for _component_face_vertexes in new_d_comp[i].get_component_faces():
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
                    _vertex = new_d_comp[i].get_component_vertexes()[int(_number_of_vertex)]

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

            new_d_comp[i] = Deep(new_d_comp[i], z_index)

        sorted(new_d_comp, key=lambda Deep: Deep.z_index)

        for i in range(len(new_d_comp)):
            self._detail_components[i] = new_d_comp[i].component

    # Отрисовка детали
    def draw(self, _canvas_field, _light, _operation_axis):

        self._sort_by_z_index()

        for _component in self._detail_components:
            _component.draw(_canvas_field, _light, _operation_axis)

    # Установка uid
    def generate_uid(self):
        self._detail_uid = randint(1000000, 100000000)

    # Получение значения адреса
    def get_detail_uid(self):
        return self._detail_uid


# Объект загрузки данных из файлов
class UploadingDetails:
    # Путь к загружаемым деталям
    _file_path = None

    # Количество загруженных деталей
    _number_of_uploaded_details = None

    # Все загруженные детали
    _uploaded_details = None

    # Массив данных входящего файла
    _file_row_data = None

    # Считывающая строка
    _file_string = 0

    # Инициализация объекта
    def __init__(self, _file_path):
        self._uploaded_details = config.EMPTY_LIST
        self._file_path = _file_path

    # Получение пути к файлу
    def get_file_path(self):
        return self._file_path

    # Получение данных файла
    def get_file_row_data(self):
        return self._file_row_data

    # Установка значения загруженных данных
    def __set_row_file_data(self, _file_row_data):
        self._file_row_data = _file_row_data

    # Установка значения количества загруженных деталей
    def __set_number_of_uploaded_details(self, _number_of_uploaded_details):
        self._number_of_uploaded_details = _number_of_uploaded_details

    # Получение массива данных файла
    def _get_file_row_data(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Виртуализация загрузки файла
        try:
            self.__set_row_file_data(str(open(str(self.get_file_path()), "r").read()).split("\n"))
            _error_status = config.SUCCESS_STATUS
        except Exception:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение из загруженных данных количества деталей
    def _get_number_of_details_form_row_file_data(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Виртуализация загрузки файла
        try:
            self.__set_number_of_uploaded_details(int(self._file_row_data[0]))
            _error_status = config.SUCCESS_STATUS
        except Exception:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение из загруженных данных количества компонентов
    def _get_number_of_detail_form_component(self):

        # Количество компонентов
        _number_of_detail_form_component = None

        # Виртуализация получения
        try:
            _number_of_detail_form_component = int(self._get_file_row_data()[self._file_string])
            _error_status = config.SUCCESS_STATUS
        except config.ERROR_STATUS:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Установка значения имени детали
    def __set_detail_name_file_data(self, _detail_name_file_data):
        self._detail_name_file_data = _detail_name_file_data

    # Получение данных цвета детали
    def _get_detail_color(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Виртуализация загрузки файла
        try:
            self.__set_detail_name_file_data(int(self._get_file_row_data()[2]))
            _error_status = config.SUCCESS_STATUS
        except config.ERROR_STATUS:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Прочтение названия детали
    def __read_detail_name(self):
        return str(self.get_file_row_data()[self._file_string])

    # Прочтение цвета детали
    def __read_detail_color(self):
        return str(self.get_file_row_data()[self._file_string])

    # Прочтение количества компонентов
    def __read_number_of_components(self):
        return int(self.get_file_row_data()[self._file_string])

    # Прочтение количества вершин
    def __read_number_of_vertexes(self):
        return int(self.get_file_row_data()[self._file_string])

    # Прочтение количества граней
    def __read_number_of_faces(self):
        return int(self.get_file_row_data()[self._file_string])

    # Прочтение списка вершин
    def __read_vertexes(self, _number_of_vertexes):
        # Результирующий список граней
        _vertexes = []

        for _vertex_file_string in range(self._file_string, self._file_string + _number_of_vertexes):
            _vertex_note = list(map(float, self.get_file_row_data()[_vertex_file_string].split()))

            print(_vertex_note[0], _vertex_note[1], _vertex_note[2])

            _vertexes.append(
                detail.vertex.Vertex(_vertex_note[0], _vertex_note[1], _vertex_note[2])
            )
        #
        # for i in _vertexes:
        #     print("YY", i.get_x_position(), i.get_y_position(), i.get_z_position())

        return _vertexes

    # Прочтение списка граней
    def __read_faces(self, _number_of_faces):

        # Результирующий список граней
        _faces = []

        for _faces_file_string in range(self._file_string, self._file_string + _number_of_faces):
            _vertex_note = list(map(float, self.get_file_row_data()[_faces_file_string].split()))

            print(_vertex_note[0], _vertex_note[1], _vertex_note[2])

            _faces.append(
                [int(_vertex_note[0]), int(_vertex_note[1]), int(_vertex_note[2])]
            )

        return _faces

    def __read_cylinder(self, _component_name, _detail_style):
        cylinder_f = list(map(int, self.get_file_row_data()[self._file_string].split()))
        f_pos = vertex.Vertex(
            cylinder_f[0],
            cylinder_f[1],
            cylinder_f[2]
        )
        self._file_string += 1

        height = int(self.get_file_row_data()[self._file_string])
        self._file_string += 1

        radius = int(self.get_file_row_data()[self._file_string])
        self._file_string += 1

        number_of_steps = int(self.get_file_row_data()[self._file_string])
        self._file_string += 1

        print(cylinder_f[0],
            cylinder_f[1],
            cylinder_f[2])
        print(height)
        print(radius)
        print(number_of_steps)

        return detail.component.Cylinder(
            _component_name=_component_name,
            _component_style=_detail_style,
            _f_pos=f_pos,
            _number_of_steps=number_of_steps,
            _radius=radius,
            height=height,
            _component_vertexes=[],
            _component_faces=[]
        )

    # Прочитать компоненты
    def __read_detail_components(self, _number_of_components, _detail_style):

        # Результирующий набор компонентов
        _detail_components = []

        # Последовательное чтение компонентов
        for _reading_component in range(_number_of_components):
            _component_name = str(self.get_file_row_data()[self._file_string])
            self._file_string += 1
            print(_component_name)

            if _component_name == "Цилиндр":
                _detail_components.append(
                    self.__read_cylinder(_component_name=_component_name,
                                         _detail_style=_detail_style)
                )
            else:
                _number_of_vertexes = self.__read_number_of_vertexes()
                self._file_string += 1
                print(_number_of_vertexes)

                _vertexes = self.__read_vertexes(_number_of_vertexes)
                self._file_string += _number_of_vertexes

                _number_of_faces = self.__read_number_of_faces()
                self._file_string += 1

                print(_number_of_faces)
                _faces = self.__read_faces(_number_of_faces)
                self._file_string += _number_of_faces

                _detail_components.append(
                    Component(_detail_style,
                              _vertexes, _faces)
                )

        return _detail_components

    # Получение списка загруженных деталей
    def _get_uploaded_details(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Загруженные детали
        self._uploaded_details = []

        # Указатель строки считывания
        self._file_string = 1

        # Виртуализация загрузки файла
        try:
            while self._file_string < len(self.get_file_row_data()):
                _detail_name = self.__read_detail_name()
                self._file_string += 1
                # print("Название детали:", _detail_name)

                _color = self.__read_detail_color()
                self._file_string += 1
                # print("Цвет детали:", _color)

                _number_of_components = self.__read_number_of_components()
                self._file_string += 1
                # print("Количество компонентов:", _number_of_components)

                _detail_style = detail.element_style.ElementStyle(_color)

                _detail_components = self.__read_detail_components(_number_of_components, _detail_style)

                # print(Detail(_detail_name))

                _temp_uploaded_detail = Detail(_detail_name)
                # print(_temp_uploaded_detail)
                # print(_temp_uploaded_detail.get_detail_name())

                _temp_uploaded_detail.set_detail_style(_detail_style)
                _temp_uploaded_detail.set_detail_components(_detail_components)
                # print(_temp_uploaded_detail)

                # print(len(self._uploaded_details))
                self._uploaded_details.append(_temp_uploaded_detail)

                # print(self._uploaded_details[0].get_detail_name())

            _error_status = config.SUCCESS_STATUS
        except Exception:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение информации о статусе загрузки файла
    def upload_details(self):

        # Получение массива данных файла
        _error_status = self._get_file_row_data()

        # Проверка на успешность загрузки файла
        if _error_status == config.SUCCESS_STATUS:
            _error_status = self._get_number_of_details_form_row_file_data()
        #
        # print("Количество деталей:", self._number_of_uploaded_details)

        # Проверка на успешность получения количества деталей
        if _error_status == config.SUCCESS_STATUS:
            _error_status = self._get_uploaded_details()

        # for _detail in self._uploaded_details:
        #     print(_detail._color)

        return _error_status

    # Получить загруженную деталь
    def get_uploaded_details(self):
        return self._uploaded_details

    # Вывести загруженных данных
    def out_uploading_details_information(self):
        for _detail in self._uploaded_details:
            print(_detail.get_detail_name())
            for _component in _detail.get_detail_components():
                vertexes = _component.get_component_vertexes()

                for i in vertexes:
                    print(i.get_x_position(), i.get_y_position(), i.get_z_position())

                faces = _component.get_component_faces()

                for i in faces:
                    print(i[0], i[1], i[2])
