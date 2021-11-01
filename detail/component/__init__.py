# Объект детали Компонент
import config


class Component:

    # Название компонента
    _component_name = None

    # Стиль компонента
    _component_style = None

    # Позиция компоненты
    _component_position = None

    # Описание вершин компоненты
    _component_vertexes = None

    # Описание граней компоненты
    _component_faces = None

    # Холст для отрисовки
    _canvas = None

    # Инициализация объекта компоненты
    def __init__(self, _component_style,
                 _component_vertexes, _component_faces):

        # Передача стилистических особенностей компоненты
        self._component_style = _component_style

        # Передача вершин компоненты
        self._component_vertexes = _component_vertexes

        # Передача граней компоненты
        self._component_faces = _component_faces

    # Установка холста компоненты
    def set_component_canvas(self, _canvas):
        self._canvas = _canvas

    # Установка позиции компоненты на холсте
    def set_component_position(self, _component_position):
        self._component_position = _component_position

    # Получение списка вершин
    def get_component_vertexes(self):
        return self._component_vertexes

    # Получение списка граней
    def get_component_faces(self):
        return self._component_faces

    # Отрисовка грани компоненты
    def __draw_component_face(self, _component_face_vertexes):

        # Список пар координат вершин
        _polygon_pairs_of_vertexes = []

        # Добавление в список пар координат вершин пар вершин
        for _number_of_vertex in _component_face_vertexes:

            # Текущая вершина по позиции
            _vertex = self.get_component_vertexes()[int(_number_of_vertex)]

            # Добавление данных текущей вершины
            _polygon_pairs_of_vertexes.append([_vertex.get_x_position(),
                                               _vertex.get_y_position()])

        print(_polygon_pairs_of_vertexes)

        # Отрисовка области
        self._get_canvas().create_polygon(_polygon_pairs_of_vertexes, fill=self._get_component_style().get_color())

    # Прототип функции отрисовки компоненты
    def draw(self, _canvas):

        # Установка холста рисования
        self.set_component_canvas(_canvas)

        # Установка позиции на холсте рисования
        self.set_component_position(self._component_position)

        # Статус отрисовки компоненты
        _error_status = None

        # Проход по всем наборам граней
        for _component_face_vertexes in self.get_component_faces():
            self.__draw_component_face(_component_face_vertexes)

        _error_status = config.SUCCESS_STATUS

        # # Виртуализация отрисовки компоненты
        # try:
        #     # Проход по всем наборам граней
        #     for _component_face_vertexes in self.get_component_faces():
        #         self.__draw_component_face(_component_face_vertexes)
        #
        #     _error_status = config.SUCCESS_STATUS
        # except Exception:
        #     _error_status = config.ERROR_STATUS

        return config.ERROR_STATUS

    # Получение холста
    def _get_canvas(self):
        return self._canvas

    # Получение названия компоненты
    def _get_component_name(self):
        return self._component_name

    # Получение стиля компоненты
    def _get_component_style(self):
        return self._component_style

    # Получение позиции компоненты
    def _get_component_position(self):
        return self._component_position

