# Подключение конфигурации

# Основной блок программы
import config
import detail
from interface import Interface
from operation import Operation
from operation.operation_detail import OperationDetails

import operation.operation_axis

def main():
    # Подгрузка данных
    _uploaded_details = detail.UploadingDetails("/Applications/modeling_children_constructor/input_details/cube.txt")

    # Непосредственная загрузка данных
    _error_status = _uploaded_details.upload_details()

    # Проверка на отсуствие ошибок при загрузка данных
    if _error_status != config.ERROR_STATUS:
        # Инициализация объекта операционных данных
        _operation = OperationDetails()

        # Передача операционных данных
        _operation.update_uploaded_details(_uploaded_details.get_uploaded_details())

        # Запуск интерефейса
        Interface(_operation_data=_operation, _operation_axis=operation.operation_axis.OperationAxis())


# Старт программы
if __name__ == '__main__':
    main()


