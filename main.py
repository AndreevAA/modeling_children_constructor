# Подключение конфигурации

# Основной блок программы
import config
import detail
from detail.light import Light
from detail.vertex import Vertex
from interface import Interface
from operation import Operation
from operation.operation_detail import OperationDetails

import operation.operation_axis


def main():
    # Подгрузка данных
    _uploaded_details = detail.UploadingDetails("input_details/real_details.txt")

    # Непосредственная загрузка данных
    _error_status = _uploaded_details.upload_details()

    # Проверка на отсуствие ошибок при загрузка данных
    if _error_status != config.ERROR_STATUS:
        # Инициализация объекта операционных данных
        _operation = OperationDetails()

        # Передача операционных данных
        _operation.update_uploaded_details(_uploaded_details.get_uploaded_details())

        # Инициализация источника света
        _light = Light(_position=Vertex(700, 400, 300),
                       _power=100000000000)

        # Запуск интерефейса
        Interface(_operation_data=_operation, _operation_axis=operation.operation_axis.OperationAxis(),
                  _operation_light=_light)


# Старт программы
if __name__ == '__main__':
    main()
