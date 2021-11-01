from tkinter import LEFT, Button, Listbox, EXTENDED, Scrollbar, Entry, W
from tkinter.ttk import Combobox, Label


# Объект управления интерфейсом
import config
import detail
import interface.message
import operation


class Controller:

    # Данные работы
    _controller = None

    # Блок добавления деталей
    _addingDetails = None

    _entry = None  # Выбранная деталь
    _box = None  # Область списка деталей
    _axis = None  # Выбранная ось
    _degree = None  # Угол поворота

    _controller_frame = None

    _operation_data = None

    # Инициализация объекта панели управления интерфейсом
    def __init__(self):
        super().__init__()

        # Добавление операционных данных
        self._operation_data = operation.Operation()

    # Размещение блока параллельных кнопок добавления и удаления детали
    def _set_button_choosing_for_adding_details(self):
        # Блок выбора детали для добавления
        self._entry = Combobox(self._controller_frame, values=["Куб"])
        self._entry.grid(row=1, column=0, columnspan=2)

    # Размещение блока параллельных кнопок добавления и удаления детали
    def _set_button_choosing_and_adding_details(self):
        Button(text="Добавить", command=self._add_detail).grid(row=2, column=0, columnspan=1)
        Button(text="Удалить", command=self._delete_detail).grid(row=2, column=1, columnspan=1)

    # Размещение ярлыков
    def _set_all_labels(self):

        # Ярлык Деталь
        i_d_l = Label(text="Деталь", justify=LEFT)
        i_d_l.config(font=("Courier", 16, "bold"))
        i_d_l.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky=W)

        # Ярлык добавленных деталей
        add_d_l = Label(text="Добавленные", justify=LEFT)
        add_d_l.config(font=("Courier", 16, "bold"))
        add_d_l.grid(row=3, column=0, columnspan=2, pady=(20, 10), sticky=W)

        # Ярлык перемещения детали
        m_d_l = Label(text="Перемещение", justify=LEFT)
        m_d_l.config(font=("Courier", 16, "bold"))
        m_d_l.grid(row=5, column=0, columnspan=2, pady=(20, 10), sticky=W)

        # Ярлык поворота детали
        r_d_l = Label(text="Поворот", justify=LEFT)
        r_d_l.config(font=("Courier", 16, "bold"))
        r_d_l.grid(row=9, column=0, columnspan=2, pady=(20, 10), sticky=W)

        l_dge = Label(text="Ось поворота", justify=LEFT)
        l_dge.config(font=("Courier", 9))
        l_dge.grid(row=10, column=0, columnspan=2, pady=(2, 2), sticky=W)

        l_dge = Label(text="Угол поворота", justify=LEFT)
        l_dge.config(font=("Courier", 9))
        l_dge.grid(row=12, column=0, columnspan=2, pady=(2, 2), sticky=W)

    # Размещение списка добавленных деталей
    def _set_box(self):
        # Список добавленных деталей
        self._box = Listbox(selectmode=EXTENDED, width=17)
        self._box.grid(row=4, column=0, columnspan=2)
        scroll = Scrollbar(command=self._box.yview)
        scroll.grid(row=4, column=0, columnspan=2)
        self._box.config(yscrollcommand=scroll.set)

    # Размещение блока перемещения детали
    def _set_buttons_move_details(self):
        Button(text="Вверх").grid(row=6, column=0, columnspan=2)
        Button(text="Влево").grid(row=7, column=0, columnspan=1)
        Button(text="Вправо").grid(row=7, column=1, columnspan=1)
        Button(text="Вниз").grid(row=8, column=0, columnspan=2)

    # Размещение блока кнопок поворота детали
    def _set_button_rotate(self):
        Button(text="Повернуть").grid(row=14, column=0, columnspan=2)

    # Размещение вводимых данных для поворота
    def _set_inputting_form_data_for_rotation(self):
        # Блок параллельных параметров поворота
        self._axis = Combobox(self._controller_frame, values=["Ось X", "Ось Y", "Ось Z"])
        self._axis.grid(row=11, column=0, columnspan=2)

        Entry(textvariable=self._degree).grid(row=13, column=0, columnspan=2)

    # Запуск панели управления
    def setup(self):
        # Виртуальная панель управления
        _temp_controller = None

        # Размещение всех ярлыков
        self._set_all_labels()

        # Размещение блока выбора для добавления деталей
        self._set_button_choosing_for_adding_details()

        # Размещение блока параллельных кнопок добавления и удаления детали
        self._set_button_choosing_and_adding_details()

        # Размещение списка добавленных деталей
        self._set_box()

        # Размещение блока перемещения детали
        self._set_buttons_move_details()

        # Размещение вводимых данных для поворота
        self._set_inputting_form_data_for_rotation()

        # Размещение кнопки поворота
        self._set_button_rotate()

        # Переход от реального к виртуальному
        self._controller = _temp_controller

    # Проверка на выбор детали для загрузки
    def _is_selected_detail_in_entry(self):

        # Статус ошибки
        _error_status = config.ERROR_STATUS

        # Проверка на наличие выбора и его пустоту
        if self._entry.get() is not None and len(self._entry.get()) > 0:
            _error_status = config.SUCCESS_STATUS

        return _error_status

    # Получение выбранной для загрузки детали
    def _get_entry_detail(self):

        # Название полученного объекта детали
        _entry_detail_name = self._entry.get()

        # Полученный объект детали
        _detail = detail.Detail(_entry_detail_name)

        return _detail

    # Обработка нажатия на добавление детали
    def _add_detail(self):

        # Статус ошибки
        _error_status = self._is_selected_detail_in_entry()

        # Вывод сообщения об ошибке, если деталь не выбрана
        if _error_status == config.ERROR_STATUS:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

        elif _error_status == config.SUCCESS_STATUS:
            self._operation_data.add_detail(self._get_entry_detail())

    # Обработка нажатие на удаление детали
    def _delete_detail(self):
        print(1)