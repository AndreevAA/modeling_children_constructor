from math import radians
from tkinter import LEFT, Button, Listbox, EXTENDED, Scrollbar, Entry, W, END
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

    _window = None

    _canvas_field = None

    _degree_entry = None

    # Инициализация объекта панели управления интерфейсом
    def __init__(self, _operation_data, _window, _canvas_field):

        # Добавление операционных данных
        self._operation_data = _operation_data

        self._window = _window
        self._canvas_field = _canvas_field

    # Размещение блока параллельных кнопок добавления и удаления детали
    def _set_button_choosing_for_adding_details(self):
        # Блок выбора детали для добавления
        self._entry = Combobox(self._controller_frame,
                               values=self._operation_data.get_list_of_all_uploaded_details_name())
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
        Button(text="Вверх", command=self.move_detail_top).grid(row=6, column=0, columnspan=2)
        Button(text="Влево", command=self.move_detail_left).grid(row=7, column=0, columnspan=1)
        Button(text="Вправо", command=self.move_detail_right).grid(row=7, column=1, columnspan=1)
        Button(text="Вниз", command=self.move_detail_bottom).grid(row=8, column=0, columnspan=2)

    # Размещение блока кнопок поворота детали
    def _set_button_rotate(self):
        Button(text="Повернуть", command=self.rotate_detail).grid(row=14, column=0, columnspan=2)

    # Размещение вводимых данных для поворота
    def _set_inputting_form_data_for_rotation(self):
        # Блок параллельных параметров поворота
        self._axis = Combobox(self._controller_frame, values=["Ось X", "Ось Y", "Ось Z"])
        self._axis.grid(row=11, column=0, columnspan=2)

        self._degree_entry = Entry(textvariable=self._degree)
        self._degree_entry.grid(row=13, column=0, columnspan=2)

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
        _detail = detail.Detail("")

        # Нахождение выбранной детали
        for _temp_detail in self._operation_data.get_uploaded_details():
            if _temp_detail.get_detail_name() == _entry_detail_name:
                _detail = _temp_detail

        return _detail

    # Получение направления поворота детали
    def _get_detail_rotation_way(self):
        return self._axis.get()

    # Обработка нажатия на добавление детали
    def _add_detail(self):

        # Статус ошибки
        _error_status = self._is_selected_detail_in_entry()

        # Вывод сообщения об ошибке, если деталь не выбрана
        if _error_status == config.ERROR_STATUS:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

        elif _error_status == config.SUCCESS_STATUS:
            # Получение объекта выбраной детали
            _temp_entry_detail = self._get_entry_detail()

            # Генерация UID
            _temp_entry_detail.generate_uid()

            # Добавление выбранной детали в операцинные данные
            self._operation_data.add_detail(_temp_entry_detail)

            # Добавление в бокс названия добавленного элемента
            self._box.insert(END, self._entry.get() + " " + str(_temp_entry_detail.get_detail_uid()))

            # Очистка поля выбора
            self._entry.delete(0, END)
            #
            # print(self._canvas_field())

            print(len(self._operation_data.get_operation_details()))

            # Обновление канваса
            self._canvas_field.update(self._operation_data)

    # Обработка нажатие на удаление детали
    def _delete_detail(self):

        select = list(self._box.curselection())

        if len(select) > 0:
            select.reverse()
            for temp_number in select:
                # Информация о выбранной кликом детали
                element_information = self._box.get(temp_number).split()

                # Удаление из массива деталей
                self._operation_data.delete_detail_by_uid(int(element_information[1]))

                # Удаление детали из бокса
                self._box.delete(temp_number)

                print("SIZE: ", len(self._operation_data.get_operation_details()))

                # Обновление канваса
                self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Перемещение детали вправо
    def move_detail_right(self):
        select = list(self._box.curselection())

        if len(select) == 1:
            # Информация о выбранной кликом детали
            element_information = self._box.get(select[0]).split()

            # Движение детали вправо в операционных данных
            self._operation_data.move_detail_by_uid(10, 0, 0, int(element_information[1]))

            print(element_information)
            # Обновление канваса
            self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Перемещение детали влево
    def move_detail_left(self):
        select = list(self._box.curselection())

        if len(select) == 1:
            # Информация о выбранной кликом детали
            element_information = self._box.get(select[0]).split()

            # Движение детали вправо в операционных данных
            self._operation_data.move_detail_by_uid(-10, 0, 0, int(element_information[1]))

            print(element_information)
            # Обновление канваса
            self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Перемещение детали вверх
    def move_detail_top(self):
        select = list(self._box.curselection())

        if len(select) == 1:
            # Информация о выбранной кликом детали
            element_information = self._box.get(select[0]).split()

            # Движение детали вправо в операционных данных
            self._operation_data.move_detail_by_uid(0, -10, 0, int(element_information[1]))

            print(element_information)
            # Обновление канваса
            self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Перемещение детали вниз
    def move_detail_bottom(self):
        select = list(self._box.curselection())

        if len(select) == 1:
            # Информация о выбранной кликом детали
            element_information = self._box.get(select[0]).split()

            # Движение детали вправо в операционных данных
            self._operation_data.move_detail_by_uid(0, +10, 0, int(element_information[1]))

            print(element_information)
            # Обновление канваса
            self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Поворот детали
    def rotate_detail(self):
        # Выбранная деталь для поворота
        selected_detail_to_rotate = list(self._box.curselection())

        # Проверка на количество выбранных деталей
        if len(selected_detail_to_rotate) == 1:
            # Информация о выбранной кликом детали
            element_information = self._box.get(selected_detail_to_rotate[0]).split()

            # Получение оси поворота
            _detail_rotation_way = self._get_detail_rotation_way()

            # Угол поворота детали
            _detail_degree = None

            # Получение угла поворота фигуры
            try:
                _detail_degree = radians(float(self._degree_entry.get()))
            except Exception:
                interface.message.Message(config.ERROR_STATUS_DETAIL_ERROR_DEGREE)

            if _detail_degree is not None:
                self._operation_data.rotate_detail(int(element_information[1]), _detail_degree, _detail_rotation_way)

            # Обновление Canvas
            self._canvas_field.update(self._operation_data)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)
