# Объект операционных данных деталей
from math import sin, cos

import config
import detail
import operation.operation_axis
import detail.pixel

# first second
# third fourth
from detail import pixel


def count_determinant_two_size(first, second, third, fourth):
    return first * fourth - third * second

class OperationDetails:
    # Количество деталей
    _number_of_operation_details = None

    # Операционные данные деталей
    _operation_details = None

    # Загруженные детали
    _uploaded_details = None

    # Инициализация операционных деталей
    def __init__(self):
        self._operation_details = config.EMPTY_LIST
        self._number_of_operation_details = config.ZERO_NUMBER

    # Получение таблицы пикселей цветов изображения
    def get_pixels_table(self):

        # Инициализируем пиксели в наборе экрана
        all_details_pixels_table = pixel.PixelsTable(config.CANVAS_WIDTH, config.CANVAS_HEIGHT, 0, 0)
        #
        # print("len(pixels_table) = ", len(pixels_table), config.CANVAS_HEIGHT)
        # print("len(pixels_table[0]) = ", len(pixels_table[0]), config.CANVAS_WIDTH)

        used = []

        for temp_detail in self.operation_details:
            for temp_component in temp_detail.components:

                x_min, x_max, y_min, y_max = config.ABS_MAX, config.ABS_MIN, config.ABS_MAX, config.ABS_MIN

                vertexes = temp_component.vertexes
                faces = temp_component.faces

                for temp_vertex in vertexes:
                    x_min = min(x_min, temp_vertex.x)
                    x_max = max(x_max, temp_vertex.x)
                    y_min = min(y_min, temp_vertex.y)
                    y_max = max(y_max, temp_vertex.y)

                print("x_max - x_min, y_max - y_min, x_min, y_min: ", min(config.CANVAS_WIDTH, x_max) - max(0, x_min), min(config.CANVAS_HEIGHT, y_max) - max(0, y_min), max(0, x_min), max(y_min, 0))

                component_pixels_table = pixel.PixelsTable(min(config.CANVAS_WIDTH, x_max) - max(0, x_min), min(config.CANVAS_HEIGHT, y_max) - max(0, y_min), max(0, x_min), max(y_min, 0))

                for temp_face in faces:
                    # A = count_determinant_two_size(vertexes[temp_face[1]].y - vertexes[temp_face[0]].y, vertexes[temp_face[2]].y - vertexes[temp_face[0]].y,
                    #                                vertexes[temp_face[1]].z - vertexes[temp_face[0]].z, vertexes[temp_face[2]].z - vertexes[temp_face[0]].z)
                    # B = -count_determinant_two_size(vertexes[temp_face[1]].x - vertexes[temp_face[0]].x, vertexes[temp_face[2]].x - vertexes[temp_face[0]].x,
                    #                                vertexes[temp_face[1]].z - vertexes[temp_face[0]].z, vertexes[temp_face[2]].z - vertexes[temp_face[0]].z)
                    # C = count_determinant_two_size(vertexes[temp_face[1]].x - vertexes[temp_face[0]].x, vertexes[temp_face[2]].x - vertexes[temp_face[0]].x,
                    #                                vertexes[temp_face[1]].y - vertexes[temp_face[0]].y, vertexes[temp_face[2]].y - vertexes[temp_face[0]].y)
                    # D = -vertexes[temp_face[0]].x * A + vertexes[temp_face[0]].y * B - vertexes[temp_face[0]].z * C
                    #
                    # print("A, B, C, D: ", A, B, C, D)

                    for i in range(len(temp_face)):

                        f_v = None
                        s_v = None

                        if i < len(temp_face) - 1:
                            f_v = vertexes[temp_face[i]]
                            s_v = vertexes[temp_face[i + 1]]
                        elif i == len(temp_face) - 1:
                            f_v = vertexes[temp_face[0]]
                            s_v = vertexes[temp_face[i]]

                        is_used = False

                        for c_used in used:
                            if (c_used[0] == f_v and c_used[1] == s_v) or \
                                    (c_used[0] == s_v and c_used[1] == f_v):
                                is_used = True
                                break

                        if not is_used:


                            # Наклонная
                            if f_v.y != s_v.y and f_v.x != s_v.x:

                                print()
                                print("Рассматривается: ")

                                if i < len(temp_face) - 1:
                                    print(temp_face[i], temp_face[i + 1])
                                elif i == len(temp_face) - 1:
                                    print(temp_face[i], temp_face[0])

                                for y in range(max(0, int(min(f_v.y, s_v.y))), max(0, int(max(f_v.y, s_v.y)))):

                                    k = (f_v.y - s_v.y) / (f_v.x - s_v.x)
                                    b = k * f_v.x - f_v.y
                                    # b = (k * (f_v.x + s_v.x) - (f_v.y + s_v.y)) / 2

                                    left_x = int((y - b) / k)

                                    # print("left_x: , y", left_x, y, k, b)

                                    for x in range(left_x, int(component_pixels_table.width)):
                                        if x > 0 and y > 0:
                                            # print(x, y, k, b)
                                            _pixel = pixel.Pixel(x, y, 0)
                                            _pixel.color = temp_component.style.color
                                            component_pixels_table.xor_pixel(x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), pixel.Pixel(x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), _pixel))

                            # Вертикальная
                            if f_v.x == s_v.x:
                                print("f_v.x == s_v.x: ", f_v.x == s_v.x, f_v.x, f_v.y, s_v.x, s_v.y)

                                for y in range(int(min(f_v.y, s_v.y)), int(max(f_v.y, s_v.y))):
                                    for x in range(int(f_v.x), int(component_pixels_table.width)):

                                        if x > 0 and y > 0:
                                            print(
                                                "x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), 0",
                                                x - int(component_pixels_table.s_x),
                                                y - int(component_pixels_table.s_y), 0)

                                            _pixel = pixel.Pixel(x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), 0)
                                            _pixel.color = temp_component.style.color
                                            component_pixels_table.xor_pixel(x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), _pixel)
                            # Горизонтальная
                            if f_v.y == s_v.y:

                                for x in range(int(min(f_v.x, s_v.x)), int(component_pixels_table.width)):

                                    if x > 0 and f_v.y > 0:
                                        print(
                                            "x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), 0",
                                            x - int(component_pixels_table.s_x),
                                            int(f_v.y) - int(component_pixels_table.s_y), 0)

                                        _pixel = pixel.Pixel(x - int(component_pixels_table.s_x), int(f_v.y) - int(component_pixels_table.s_y), 0)
                                        _pixel.color = temp_component.style.color
                                        component_pixels_table.xor_pixel(x - int(component_pixels_table.s_x), int(f_v.y) - int(component_pixels_table.s_y), _pixel)
                                for x in range(int(max(f_v.x, s_v.x)), int(component_pixels_table.width)):

                                    if x > 0 and f_v.y > 0:
                                        print(
                                            "x - int(component_pixels_table.s_x), y - int(component_pixels_table.s_y), 0",
                                            x - int(component_pixels_table.s_x),
                                            int(f_v.y) - int(component_pixels_table.s_y), 0)

                                        _pixel = pixel.Pixel(x - int(component_pixels_table.s_x), int(f_v.y) - int(component_pixels_table.s_y), 0)
                                        _pixel.color = temp_component.style.color
                                        component_pixels_table.xor_pixel(x - int(component_pixels_table.s_x), int(f_v.y) - int(component_pixels_table.s_y), _pixel)

                            # f_v = vertexes[temp_face[0]]
                            # s_v = vertexes[temp_face[len(temp_face) - 1]]
                            #
                            # if f_v.x == s_v.x:
                            #     print("f_v.x == s_v.x: ", f_v.x == s_v.x)
                            #     for y in range(int(min(f_v.y, s_v.y)), int(max(f_v.y, s_v.y))):
                            #         for x in range(int(f_v.x), config.CANVAS_WIDTH):
                            #             _pixel = pixel.Pixel(x, y, 0)
                            #             _pixel.color = temp_component.style.color
                            #             pixels_table.xor_pixel(x, y, _pixel)

                            # print("temp_component.name: ", temp_component.name)
                            # print("temp_component.style: ", temp_component.style.color)
                            # print("temp_component.name: ", temp_component.name)

                            used.append([f_v, s_v])

                for y in range(int(component_pixels_table.height)):
                    for x in range(int(component_pixels_table.width)):
                        t_table = all_details_pixels_table.table

                        t_x = int(x + component_pixels_table.s_x)
                        t_y = int(y + component_pixels_table.s_y)

                        # print(t_table.table)

                        if t_table[t_x][t_y].color is None and component_pixels_table.table[y][x].color is not None:
                            t_table[t_x][t_y].color = component_pixels_table.table[y][x].color

                        all_details_pixels_table.table = t_table

        return all_details_pixels_table

    @property
    def operation_details(self):
        return self._operation_details

    # Получение количества деталей
    def get_number_of_operation_details(self):
        self._number_of_operation_details = len(self._operation_details)
        return self._number_of_operation_details

    # Получение массива операционных деталей
    def get_operation_details(self):
        return self._operation_details

    # Добавление детали
    def add_detail(self, _detail):
        print("ДОБАВЛЕНИЕ ДЕТАЛИ!")
        print(self._operation_details)
        self._operation_details.append(_detail)
        print(self._operation_details)

    # Очистка списка деталей
    def delete_all_details(self):
        self._operation_details = config.EMPTY_LIST
        self._number_of_operation_details = config.ZERO_NUMBER

    # Удаление детали по uid
    def delete_detail_by_uid(self, uid):

        # Статус ошибки
        _error_status = config.ERROR_STATUS

        # Позиция удаляемого элемента
        _deleting_element_position = self._get_detail_position_by_uid(uid)

        # Проверка на наличие элемента в списке
        if _deleting_element_position is not None:
            if self._operation_details.pop(_deleting_element_position) is not None:
                _error_status = config.SUCCESS_STATUS

        return _error_status

    # Обновление списка деталей
    def update_operation_details(self, _number_of_operation_details, _operation_details):
        self._number_of_operation_details = _number_of_operation_details
        self._operation_details = _operation_details

    # Обновление загруженных деталей
    def update_uploaded_details(self, _uploaded_details):
        self._uploaded_details = _uploaded_details

    # Получение загруженных деталей
    def get_uploaded_details(self):
        return self._uploaded_details

    # Удаление детали по позиции
    def delete_detail_by_position(self, _position):

        # Статус ошибки
        _error_status = None

        try:
            # Виртуальное преобразование
            _operation_details = self.get_operation_details()[:_position] + \
                                 self.get_operation_details()[_position + 1:]

            _error_status = config.SUCCESS_STATUS
        except config.ZERO_NUMBER:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение позиции элемента
    def _get_detail_position_by_uid(self, uid):

        # Позиция элемента
        _detail_position = None

        # Определение позиции детали
        for _operation_detail_number in range(self.get_number_of_operation_details()):
            print("UID: ", uid, self.get_operation_details()[_operation_detail_number].get_detail_uid())
            if self.get_operation_details()[_operation_detail_number].get_detail_uid() == uid:
                _detail_position = _operation_detail_number
                break

        return _detail_position

    # Получение списка всех деталей
    def get_list_of_all_uploaded_details_name(self):
        list_of_all_uploaded_details_name = []

        for _temp_detail in self._uploaded_details:
            list_of_all_uploaded_details_name.append(_temp_detail.get_detail_name())

        return list_of_all_uploaded_details_name

    # Перемещение в пространстве
    def move_details(self, x_move, y_move, z_move):
        # Статус ошибки
        _error_status = config.ERROR_STATUS

        for _moving_detail in self.get_operation_details():
            for _moving_component in _moving_detail.get_detail_components():
                for _moving_vertex in _moving_component.get_component_vertexes():
                    _moving_vertex.update(_moving_vertex.get_x_position() + x_move,
                                          _moving_vertex.get_y_position() + y_move,
                                          _moving_vertex.get_z_position() + z_move)
                    print(_moving_vertex.get_x_position(),
                          _moving_vertex.get_y_position(),
                          _moving_vertex.get_z_position())
                _error_status = config.SUCCESS_STATUS

        return _error_status

    # Перемещение в пространстве
    def move_detail_by_uid(self, x_move, y_move, z_move, uid):
        # Статус ошибки
        _error_status = config.ERROR_STATUS

        # Позиция удаляемого элемента
        _moving_element_position = self._get_detail_position_by_uid(uid)

        # Проверка на наличие элемента в списке
        if _moving_element_position is not None:
            for _moving_component in self.get_operation_details()[_moving_element_position].get_detail_components():
                for _moving_vertex in _moving_component.get_component_vertexes():
                    _moving_vertex.update(_moving_vertex.get_x_position() + x_move,
                                          _moving_vertex.get_y_position() + y_move,
                                          _moving_vertex.get_z_position() + z_move)
                _error_status = config.SUCCESS_STATUS

        return _error_status

    # Получение базовой точкиъ
    def _get_base_point(self, _detail):

        _number_of_vertexes = 0

        _base_point_x_coordinate = 0
        _base_point_y_coordinate = 0
        _base_point_z_coordinate = 0

        for _moving_component in _detail.get_detail_components():
            for _moving_vertex in _moving_component.get_component_vertexes():
                _base_point_x_coordinate += _moving_vertex.get_x_position()
                _base_point_y_coordinate += _moving_vertex.get_y_position()
                _base_point_z_coordinate += _moving_vertex.get_z_position()

                _number_of_vertexes += 1

        return detail.vertex.Vertex(_base_point_x_coordinate / _number_of_vertexes,
                                    _base_point_y_coordinate / _number_of_vertexes,
                                    _base_point_z_coordinate / _number_of_vertexes)

    # Поворот детали
    def rotate_detail(self, uid, _detail_degree, _detail_rotation_way):
        # Статус ошибки
        _error_status = config.ERROR_STATUS

        # Позиция поворачиваемого элемента
        _rotating_element_position = self._get_detail_position_by_uid(uid)

        # Базовая точка
        _base_point = self._get_base_point(self.get_operation_details()[_rotating_element_position])

        # Проверка на наличие элемента в списке
        if _rotating_element_position is not None:
            for _moving_component in self.get_operation_details()[_rotating_element_position].get_detail_components():
                for _moving_vertex in _moving_component.get_component_vertexes():
                    # result_point = self._rotate_vertex(_moving_vertex, _base_point, _detail_rotation_way, -_detail_degree)
                    result_point = detail.vertex.rotate_vertex_by_base_vertex(_moving_vertex, _base_point,
                                                                              _detail_rotation_way, _detail_degree)
                    _moving_vertex.update(result_point.get_x_position(),
                                          result_point.get_y_position(),
                                          result_point.get_z_position())
                _error_status = config.SUCCESS_STATUS

        return _error_status

    # Поворот всех деталей
    def rotate_details(self, _base_vertex, _rotation_way_axis, _scene_degree):
        for _moving_details in self.get_operation_details():
            for _moving_component in _moving_details.get_detail_components():
                for _moving_vertex in _moving_component.get_component_vertexes():
                    result_point = detail.vertex.rotate_vertex_by_base_vertex(_moving_vertex, _base_vertex,
                                                                              _rotation_way_axis, _scene_degree)
                    _moving_vertex.update(result_point.get_x_position(),
                                          result_point.get_y_position(),
                                          result_point.get_z_position())

    # Зуммирование изображения относительно точки
    def zoom_by_base_vertex(self, base_vertex, zoom_coefficient):

        # Получение текущей детали из списка деталей
        for _detail in self._operation_details:

            # Получение текущей компоненты из списка компонентов текущей детали
            for _component in _detail.get_detail_components():

                # Проход по вершинам компоненты
                for _vertex in _component.get_component_vertexes():
                    # Зуммирование каждой точки относительно базовой точки на коэфф.
                    _vertex = detail.vertex.zoom_vertex_by_base_vertex(_vertex,
                                                                       base_vertex,
                                                                       zoom_coefficient)
