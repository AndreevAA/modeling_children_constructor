"""
    Базовый файл объекта детали,
    состоящей из
"""

# Объект детали
import config
import detail.element_style
from detail import vertex


class Detail:
    # Данные о детали
    _detail_name = None

    # Позиция детали в пространстве
    _detail_position = None

    # Массив компонентов детали
    _detail_components = None

    # Стиль детали
    _detail_style = None

    # Инициализация объекта Детали
    def __init__(self, _detail_name):
        # Установка имени детали
        self._detail_name = _detail_name

        # Установка базовой позиции детали
        self._set_basic_detail_position()

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


# Объект загрузки данных из файлов
class UploadingDetails:
    # Путь к загружаемым деталям
    _file_path = None

    # Количество загруженных деталей
    _number_of_uploaded_details = None

    # Статус ошибок во время загрузки


    # Все загруженные детали
    _uploaded_detail = None

    # Массив данных входящего файла
    _file_row_data = None

    # Инициализация объекта
    def __init__(self, _file_path):
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
        except config.ERROR_STATUS:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение из загруженных данных количества деталей
    def _get_number_of_details_form_row_file_data(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Виртуализация загрузки файла
        try:
            self.__set_row_file_data(int(self._get_file_row_data()[0]))
            _error_status = config.SUCCESS_STATUS
        except config.ERROR_STATUS:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение из загруженных данных количества компонентов
    def _get_number_of_detail_form_component(self, _file_string):

        # Количество компонентов
        _number_of_detail_form_component = None

        # Виртуализация получения
        try:
            _number_of_detail_form_component = int(self._get_file_row_data()[_file_string])
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
    def __read_detail_name(self, _file_string):
        return str(self.get_file_row_data()[_file_string])

    # Прочтение цвета детали
    def __read_detail_color(self, _file_string):
        return str(self.get_file_row_data()[_file_string])

    # Прочтение количества компонентов
    def __read_number_of_components(self, _file_string):
        return int(self.get_file_row_data()[_file_string])

    # Прочтение количества вершин
    def __read_number_of_vertexes(self, _file_string):
        return int(self.get_file_row_data()[_file_string])

    # Прочтение количества граней
    def __read_number_of_faces(self, _file_string):
        return int(self.get_file_row_data()[_file_string])

    # Прочтение списка вершин
    def __read_vertexes(self, _file_string, _number_of_vertexes):
        # Результирующий список граней
        _vertexes = config.EMPTY_LIST

        for _vertex_file_string in range(_file_string, _number_of_vertexes):
            _vertex_note = self.get_file_row_data()[_vertex_file_string]

            _vertexes.append(
                detail.vertex.Vertex(_vertex_note[0], _vertex_note[1], _vertex_note[2])
            )

        return _vertexes

    # Прочтение списка граней
    def __read_faces(self, _file_string, _number_of_faces):

        # Результирующий список граней
        _faces = config.EMPTY_LIST

        for _faces_file_string in range(_file_string, _number_of_faces):
            _vertex_note = self.get_file_row_data()[_faces_file_string]

            _faces.append(
                [_vertex_note[0], _vertex_note[1], _vertex_note[2]]
            )

        return _faces

    # Прочитать компоненты
    def __read_detail_components(self, _file_string, _number_of_components):

        # Результирующий набор компонентов
        _detail_components = config.EMPTY_LIST

        # Последовательное чтение компонентов
        for _reading_component in range(_number_of_components):
            _number_of_vertexes = self.__read_number_of_vertexes(_file_string + 0)
            _vertexes = self.__read_vertexes(_file_string + 1, _number_of_vertexes)
            _number_of_faces = self.__read_number_of_faces(_file_string + 1 + _number_of_vertexes)
            _faces = self.__read_faces(_file_string + 1 + _number_of_vertexes + 1, _number_of_faces)

            _file_string += 2 + _number_of_vertexes + _number_of_faces

            _detail_components.append(
                detail.component.Component()
            )

        return _detail_components

    # Получение списка загруженных деталей
    def _get_uploaded_details(self):

        # Статус ошибки при загрузке файла
        _error_status = None

        # Загруженные детали
        _uploaded_details = config.EMPTY_LIST

        # Виртуализация загрузки файла
        try:

            # Указатель строки считывания
            _file_string = 1

            while _file_string < len(self.get_file_row_data()):
                _detail_name = self.__read_detail_name(_file_string)
                _color = self.__read_detail_color(_file_string + 1)
                _number_of_components = self.__read_number_of_components(_file_string + 2)

                _detail_style = detail.element_style.ElementStyle(_color)

                _detail_components = self.__create_detail_components_list(_file_string, _number_of_components)

                _uploaded_details.append(
                    Detail(_detail_name, _detail_style, _detail_components)
                )

            _error_status = config.SUCCESS_STATUS
        except config.ERROR_STATUS:
            _error_status = config.ERROR_STATUS

        return _error_status

    # Получение информации о статусе загрузки файла
    def upload_details(self):

        # Получение массива данных файла
        _error_status = self._get_file_row_data()

        # Проверка на успешность загрузки файла
        if _error_status == config.SUCCESS_STATUS:
            _error_status = self._get_number_of_details_form_row_file_data()

        # Проверка на успешность получения количества деталей
        if _error_status == config.SUCCESS_STATUS:
            _error_status = self._get_uploaded_details()

        return _error_status
