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
