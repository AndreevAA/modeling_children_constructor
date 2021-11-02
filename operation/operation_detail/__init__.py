# Объект операционных данных деталей
from math import sin, cos

import config
import detail


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

    # Получение количества деталей
    def get_number_of_operation_details(self):
        self._number_of_operation_details = len(self._operation_details)
        return self._number_of_operation_details

    # Получение массива операционных деталей
    def get_operation_details(self):
        return self._operation_details

    # Добавление детали
    def add_detail(self, _detail):
        self._operation_details.append(_detail)

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

    # Поворот точки
    def _rotate_vertex(self, pivot_point, base_point, rotation_way, degree):

        # Смещение оси поворота
        result_point = detail.vertex.Vertex(pivot_point.get_x_position() - base_point.get_x_position(),
                                            pivot_point.get_y_position() - base_point.get_y_position(),
                                            pivot_point.get_y_position() - base_point.get_y_position())

        # Выявление оси и смена значений
        if rotation_way == "Ось X":
            x_rotated_result_point = result_point.get_x_position()
            y_rotated_result_point = result_point.get_y_position() * cos(degree) + \
                                     result_point.get_z_position() * sin(degree)
            z_rotated_result_point = - result_point.get_y_position() * sin(degree) + \
                                     result_point.get_z_position() * cos(degree)
            result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)
        elif rotation_way == "Ось Y":
            x_rotated_result_point = result_point.get_x_position() * cos(degree) + \
                                     result_point.get_z_position() * sin(degree)
            y_rotated_result_point = result_point.get_y_position()
            z_rotated_result_point = - result_point.get_x_position() * sin(degree) + \
                                     result_point.get_z_position() * cos(degree)
            result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)
        elif rotation_way == "Ось Z":
            x_rotated_result_point = result_point.get_x_position() * cos(degree) - \
                                     result_point.get_y_position() * sin(degree)
            y_rotated_result_point = result_point.get_x_position() * sin(degree) + \
                                     result_point.get_y_position() * cos(degree)
            z_rotated_result_point = result_point.get_z_position()
            result_point.update(x_rotated_result_point, y_rotated_result_point, z_rotated_result_point)

        # Возврат оси поворота
        result_point = detail.vertex.Vertex(result_point.get_x_position() + base_point.get_x_position(),
                                            result_point.get_y_position() + base_point.get_y_position(),
                                            result_point.get_y_position() + base_point.get_y_position())

        return result_point

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
                    result_point = self._rotate_vertex(_moving_vertex, _base_point, _detail_rotation_way, -_detail_degree)
                    _moving_vertex.update(result_point.get_x_position(),
                                          result_point.get_y_position(),
                                          result_point.get_z_position())
                _error_status = config.SUCCESS_STATUS

        return _error_status
