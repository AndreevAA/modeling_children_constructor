"""
    Когфигурационный файл
    сборки программы и ее выполнения
"""

# Статусы ошибок
import detail.element_style

SUCCESS_STATUS = 0
ERROR_STATUS = 1

# Данные программы
window_title = "Программа моделирования  движения объектов детского конструктора"

# Данные выбора фигуры
ERROR_STATUS_MORE_ONE_DETAIL_SELECTED = 10
ERROR_STATUS_LESS_ONE_DETAIL_SELECTED = 11

# Перемещенеи фигуры
STEP = 100

# Значения инициализации
EMPTY_LIST = []
ZERO_NUMBER = 0

# Транслирование ошибок
ERROR_STATUS_DETAIL_ERROR_DEGREE = "ERROR_STATUS_DETAIL_ERROR_DEGREE"
ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY = "ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY"
ERROR_STATUS_DETAIL_TO_DELETE_IS_NOT_SELECTED_IN_ENTRY = "ERROR_STATUS_DETAIL_TO_DELETE_IS_NOT_SELECTED_IN_ENTRY"

# Ошибки
MESSAGE_ERROR_TEXT = {
    "ERROR_STATUS_DETAIL_ERROR_DEGREE" : "Ошибка в углу поворота детали",
    "ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY": "Не выбрана деталь для добавления!",
    "ERROR_STATUS_DETAIL_TO_DELETE_IS_NOT_SELECTED_IN_ENTRY": "Не выбрана деталь для добавления!",
}

# Транслирование названий деталей
DETAILS_CUBE = "Куб"

# Стартовая позиция
START_POSITION = 0

# Расстояние сетки
DELTA_GRID_M = 15
DELTA_GRID_P = 15

GRID_LINE_COLOR = "gray"
GRID_LINE_WIDTH = 0.5

ABS_MIN = -1000
ABS_MAX = 1000

AXIS_X = "x"
AXIS_Y = "y"
AXIS_Z = "z"

