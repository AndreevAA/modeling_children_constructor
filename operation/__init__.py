"""
    Объект операционных данных
"""

# Объект операционных данных
import config
import operation.operation_detail
import operation.operation_axis


# Композиция объектов операции
class Operation:

    # Данные осей
    _operation_axis = None

    # Приватные поля
    _operation_details = None

    # Инициализация объект
    def __init__(self):

        # Связка объектов операционных деталей
        self._operation_details = operation.operation_detail.OperationDetails()

        self._operation_axis = operation.operation_axis.OperationAxis()

    # Получение операционных осей координат
    def get_operation_axis(self):
        return self._operation_axis

    # Получение операционных деталей
    def _get_operation_details(self):
        return self._operation_details

    # Обновление данных операционных деталей
    def update_operation_details(self, _operation_details):
        self._operation_details = _operation_details

    # Добавление элемента операционных деталей
    def add_detail(self, _detail):
        if self._get_operation_details() is None:
            self._operation_details = operation.operation_detail.OperationDetails()

        _operation_details = self._get_operation_details().add_detail(_detail)
        self.update_operation_details(_operation_details)

    # Удаление элементов операционных деталей
    def delete_all_details(self):
        _operation_details = self._get_operation_details().delete_all_details()
        self.update_operation_details(_operation_details)

    # Удаление детали по uid
    def delete_detail_by_uid(self, _uid):
        _operation_details = self._get_operation_details().delete_detail_by_uid(_uid)
        self.update_operation_details(_operation_details)
    #
    # # Получение списка всех деталей
    # def get_list_of_all_details_name(self):
    #     list_of_all_details_name = []
    #
    #     for _temp_detail in self._operation_details:
    #         list_of_all_details_name.append(_temp_detail.get_detail_name())
    #
    #     return list_of_all_details_name
