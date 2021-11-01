"""
    Объект операционных данных
"""

# Объект операционных данных
import config
import operation.operation_detail


# Композиция объектов операции
class Operation:

    # Приватные поля
    _operation_details = None

    # Инициализация объект
    def __init__(self):

        # Связка объектов операционных деталей
        self._operation_details = operation.operation_detail.OperationDetails()

    # Получение операционных деталей
    def _get_operation_details(self):
        return self._operation_details

    # Обновление данных операционных деталей
    def _update_operation_details(self, _operation_details):
        self._operation_details = _operation_details

    # Добавление элемента операционных деталей
    def add_detail(self, _detail):
        if self._get_operation_details() is None:
            self._operation_details = operation.operation_detail.OperationDetails()

        _operation_details = self._get_operation_details().add_detail(_detail)
        self._update_operation_details(_operation_details)

    # Удаление элементов операционных деталей
    def delete_all_details(self):
        _operation_details = self._get_operation_details().delete_all_details()
        self._update_operation_details(_operation_details)

    # Удаление детали по uid
    def delete_detail_by_uid(self, _uid):
        _operation_details = self._get_operation_details().delete_detail_by_uid(_uid)
        self._update_operation_details(_operation_details)

