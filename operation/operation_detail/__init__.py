# Объект операционных данных деталей
import config


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
