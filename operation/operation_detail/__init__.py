# Объект операционных данных деталей
import config


class OperationDetails:
    # Количество деталей
    _number_of_operation_details = None

    # Операционные данные деталей
    _operation_details = None

    # Инициализация операционных деталей
    def __init__(self):
        self._operation_details = config.EMPTY_LIST
        self._number_of_operation_details = config.ZERO_NUMBER

    # Получение количества деталей
    def get_number_of_operation_details(self):
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

            # Удаление элемента по позиции
            _error_status = self.delete_detail_by_position(_deleting_element_position)

        return _error_status

    # Обновление списка деталей
    def _update_operation_details(self, _number_of_operation_details, _operation_details):
        self._number_of_operation_details = _number_of_operation_details
        self._operation_details = _operation_details

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
            if self.get_operation_details()[_operation_detail_number].get_uid() == uid:
                _detail_position = _operation_detail_number
                break

        return _detail_position
