# Объект позиции
class Position:

    # Начальная точка позиции
    _start_vertex_position = None

    # Конечная точка позиции
    _end_vertex_position = None

    # Инициализация объекта
    def __init__(self, _start_vertex_position, _end_vertex_position):
        self._start_vertex_position = _start_vertex_position
        self._end_vertex_position = _end_vertex_position

    # Получение начальной позиции
    def get_start_vertex_position(self):
        return self._start_vertex_position

    # Получение конечной позиции
    def get_end_vertex_position(self):
        return self._end_vertex_position

    # Установка начальной позиции
    def _set_start_vertex_position(self, _start_vertex_position):
        self._start_vertex_position = _start_vertex_position

    # Установка конечной позиции
    def _set_end_vertex_position(self, _end_vertex_position):
        self._end_vertex_position = _end_vertex_position

    # Обновление позиции
    def set_vertex_position(self, self_start_vertex_position, _end_vertex_position):
        self._set_start_vertex_position(self_start_vertex_position)
        self._set_end_vertex_position(_end_vertex_position)
