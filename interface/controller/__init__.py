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

    _x_entry = None
    _y_entry = None
    _z_entry = None
    _power = None

    _controller_frame = None

    _operation_data = None
    _operation_axis = None
    _operation_light = None

    _window = None

    _canvas_field = None

    _degree_entry = None

    # Инициализация объекта панели управления интерфейсом
    def __init__(self, _operation_data, _operation_axis, _operation_light, _window, _canvas_field):

        # Добавление операционных данных
        self._operation_data = _operation_data
        self._operation_axis = _operation_axis
        self._operation_light = _operation_light

        self._window = _window
        self._canvas_field = _canvas_field

        # self._x_entry = self._operation_light.x
        # self._y_entry = self._operation_light.y
        # self._z_entry = self._operation_light.z
        #
        # self._power = self._operation_light.power

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
        m_d_l = Label(text="Перемещение фигура", justify=LEFT)
        m_d_l.config(font=("Courier", 16, "bold"))
        m_d_l.grid(row=5, column=0, columnspan=2, pady=(20, 10), sticky=W)

        # Ярлык поворота детали
        r_d_l = Label(text="Поворот детали", justify=LEFT)
        r_d_l.config(font=("Courier", 16, "bold"))
        r_d_l.grid(row=9, column=0, columnspan=2, pady=(20, 10), sticky=W)

        l_dge = Label(text="Ось поворота", justify=LEFT)
        l_dge.config(font=("Courier", 9))
        l_dge.grid(row=10, column=0, columnspan=2, pady=(2, 2), sticky=W)

        l_dge = Label(text="Угол поворота", justify=LEFT)
        l_dge.config(font=("Courier", 9))
        l_dge.grid(row=12, column=0, columnspan=2, pady=(2, 2), sticky=W)

        # Ярлык поворота сцены
        r_d_l = Label(text="Перемещение сцены", justify=LEFT)
        r_d_l.config(font=("Courier", 16, "bold"))
        r_d_l.grid(row=0, column=15, columnspan=2, pady=(20, 10), sticky=W)

        r_i_l = Label(text="Источник света", justify=LEFT)
        r_i_l.config(font=("Courier", 16, "bold"))
        r_i_l.grid(row=9, column=15, columnspan=2, pady=(20, 10), sticky=W)

        l_x_i = Label(text="X:", justify=LEFT)
        l_x_i.config(font=("Courier", 9))
        l_x_i.grid(row=10, column=15, columnspan=2, pady=(2, 2), sticky=W)

        l_y_i = Label(text="Y:", justify=LEFT)
        l_y_i.config(font=("Courier", 9))
        l_y_i.grid(row=12, column=15, columnspan=2, pady=(2, 2), sticky=W)

        l_z_i = Label(text="Z:", justify=LEFT)
        l_z_i.config(font=("Courier", 9))
        l_z_i.grid(row=14, column=15, columnspan=2, pady=(2, 2), sticky=W)

        l_i = Label(text="I:", justify=LEFT)
        l_i.config(font=("Courier", 9))
        l_i.grid(row=16, column=15, columnspan=2, pady=(2, 2), sticky=W)

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

    # Размещение блока перемещения сцены
    def _set_buttons_move_scene(self):
        Button(text="Вверх", command=self.move_scene_top).grid(row=1, column=15, columnspan=2)
        Button(text="Влево", command=self.move_scene_left).grid(row=2, column=15, columnspan=1)
        Button(text="Вправо", command=self.move_scene_right).grid(row=2, column=16, columnspan=1)
        Button(text="Вниз", command=self.move_scene_bottom).grid(row=3, column=15, columnspan=2)

    # Размещение блока перемещения сцены
    def _set_buttons_zoom_scene(self):
        Button(text="  +  ", command=self.zoom_scene_in).grid(row=5, column=15, columnspan=1)
        Button(text="  -  ", command=self.zoom_scene_out).grid(row=5, column=16, columnspan=1)

    # Размещение блока кнопок поворота детали
    def _set_button_rotate(self):
        Button(text="Повернуть", command=self.rotate_detail).grid(row=14, column=0, columnspan=2)

    # Размещение блока кнопок поворота детали
    def _set_button_rotate_scene(self):
        Button(text="Повернуть", command=self.rotate_scene).grid(row=8, column=16, columnspan=2)

    # Размещение блока кнопок поворота детали
    def _set_button_move_set_light(self):
        Button(text="Изменить источник света", command=self.change_light).grid(row=18, column=15, columnspan=2)

    # Размещение вводимых данных для поворота детали
    def _set_inputting_form_data_for_rotation(self):
        # Блок параллельных параметров поворота
        self._axis = Combobox(self._controller_frame, values=[config.AXIS_X, config.AXIS_Y, config.AXIS_Z])
        self._axis.grid(row=11, column=0, columnspan=2)

        self._degree_entry = Entry(textvariable=self._degree)
        self._degree_entry.grid(row=13, column=0, columnspan=2)

    # Размещение вводимых данных для перемещения ИС
    def _set_inputting_form_data_for_light(self):
        self._x_entry = Entry(textvariable=self._x_entry)
        self._x_entry.grid(row=11, column=15, columnspan=2)

        self._y_entry = Entry(textvariable=self._y_entry)
        self._y_entry.grid(row=13, column=15, columnspan=2)

        self._z_entry = Entry(textvariable=self._y_entry)
        self._z_entry.grid(row=15, column=15, columnspan=2)

        self._power = Entry(textvariable=self._power)
        self._power.grid(row=17, column=15, columnspan=2)

        self._x_entry.insert(0, self._operation_light.x)
        self._y_entry.insert(0, self._operation_light.y)
        self._z_entry.insert(0, self._operation_light.z)
        self._power.insert(0, self._operation_light.power)

    # Размещение вводимых данных для поворота сцены
    def _set_inputting_form_data_for_rotation_scene(self):
        # Блок параллельных параметров поворота
        self._axis_scene = Combobox(self._controller_frame, values=[config.AXIS_X, config.AXIS_Y, config.AXIS_Z])
        self._axis_scene.grid(row=6, column=15, columnspan=2)

        self._degree_entry_scene = Entry(textvariable=self._degree)
        self._degree_entry_scene.grid(row=7, column=15, columnspan=2)

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

        # Размещение блока перемещения сцены
        self._set_buttons_move_scene()

        # Размещение блока зуммирования сцены
        self._set_buttons_zoom_scene()

        # Размещение вводимых данных для поворота
        self._set_inputting_form_data_for_rotation()

        # Размещение вводимых данных для поворота сцены
        self._set_inputting_form_data_for_rotation_scene()

        # Размещение ввода для ИС
        self._set_inputting_form_data_for_light()

        # Размещение кнопки поворота
        self._set_button_rotate()

        # Размещение кнопки поворота сцены
        self._set_button_rotate_scene()

        # Размещение кнопки изменение источника света
        self._set_button_move_set_light()

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

        # Нахождение выбранной детали
        for _temp_detail in self._operation_data.get_uploaded_details():
            if _temp_detail.get_detail_name() == _entry_detail_name:
                return _temp_detail

    # Получение направления поворота детали
    def _get_detail_rotation_way(self):
        return self._axis.get()

    # Получение напрвления поворота сцены
    def _get_scene_rotation_way(self):
        return self._axis_scene.get()

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

            # В памяти
            _detail = detail.Detail(_temp_entry_detail.name)

            # Генерация UID
            _detail.generate_uid()

            _detail.position = _temp_entry_detail.position
            _detail.components = _temp_entry_detail.components
            _detail.style = _temp_entry_detail.style
            # _detail = _temp_detail

            print("_detail.name, _detail.uid: ", _detail.name, _detail.uid)

            # Добавление выбранной детали в операцинные данные
            self._operation_data.add_detail(_detail)

            # Добавление в бокс названия добавленного элемента
            self._box.insert(END, self._entry.get() + " " + str(_detail.get_detail_uid()))

            # Очистка поля выбора
            self._entry.delete(0, END)
            #
            # print(self._canvas_field())

            print(len(self._operation_data.get_operation_details()))

            # Обновление канваса
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

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
                self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
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
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
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
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
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
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Перемещение сцены
    def move_scene_top(self):
        self._operation_data.move_details(0, +10, 0)
        self._operation_axis.move(0, +10, 0)

        # Обновление канваса
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

    # Перемещение сцены
    def move_scene_bottom(self):
        self._operation_data.move_details(0, -10, 0)
        self._operation_axis.move(0, -10, 0)

        # Обновление канваса
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

    # Перемещение сцены
    def move_scene_left(self):
        self._operation_data.move_details(-10, 0, 0)
        self._operation_axis.move(-10, 0, 0)

        # Обновление канваса
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

    # Перемещение сцены
    def move_scene_right(self):
        self._operation_data.move_details(+10, 0, 0)
        self._operation_axis.move(+10, 0, 0)

        # Обновление канваса
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

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
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    # Поворот сцены
    def rotate_scene(self):

        # Получение оси поворота
        _rotation_way_axis = self._get_scene_rotation_way()

        # Угол поворота детали
        _scene_degree = None

        # Получение угла поворота фигуры
        try:
            _scene_degree = radians(float(self._degree_entry_scene.get()))
        except Exception:
            interface.message.Message(config.ERROR_STATUS_DETAIL_ERROR_DEGREE)

        _base_vertex = self._operation_axis.axes_intersection.intersection_vertex

        # print("_base_vertex: ", _base_vertex.x, _base_vertex.y, _base_vertex.z)

        if _scene_degree is not None:
            self._operation_axis.rotate(
                _base_vertex, _rotation_way_axis, _scene_degree
            )
            self._operation_data.rotate_details(_base_vertex, _rotation_way_axis, _scene_degree)

        # Обновление Canvas
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

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
            self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)
        else:
            interface.message.Message(config.ERROR_STATUS_DETAIL_TO_ADD_IS_NOT_SELECTED_IN_ENTRY)

    def zoom_scene_in(self):
        _base_vertex = self._operation_axis.axes_intersection.intersection_vertex
        _zoom_coefficient = config.ZOOM_COEFFICIENT

        self._operation_data.zoom_by_base_vertex(_base_vertex, _zoom_coefficient)
        self._operation_axis.zoom(_base_vertex, _zoom_coefficient)

        # Обновление Canvas
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

    def zoom_scene_out(self):
        _base_vertex = self._operation_axis.axes_intersection.intersection_vertex
        _zoom_coefficient = 1 / config.ZOOM_COEFFICIENT

        self._operation_data.zoom_by_base_vertex(_base_vertex, _zoom_coefficient)
        self._operation_axis.zoom(_base_vertex, _zoom_coefficient)

        # Обновление Canvas
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)

    def _free_light_settings_fields(self):
        self._x_entry.delete(0, "end")
        self._y_entry.delete(0, "end")
        self._z_entry.delete(0, "end")
        self._power.delete(0, "end")

    def change_light(self):

        _x_entry = None
        _y_entry = None
        _z_entry = None
        _power = None

        # Получение угла поворота фигуры
        try:
            _x_entry = int(self._x_entry.get())
            _y_entry = int(self._y_entry.get())
            _z_entry = int(self._z_entry.get())
            _power = int(self._power.get())
        except Exception:
            interface.message.Message(config.ERROR_STATUS_DETAIL_ERROR_DEGREE)

        if _x_entry is not None and \
            _y_entry is not None and \
            _z_entry is not None and \
            _power is not None:

            self._operation_light.x = _x_entry
            self._operation_light.y = _y_entry
            self._operation_light.z = _z_entry
            self._operation_light.power = _power

            self._free_light_settings_fields()

            self._x_entry.insert(0, _x_entry)
            self._y_entry.insert(0, _y_entry)
            self._z_entry.insert(0, _z_entry)
            self._power.insert(0, _power)

        # Обновление Canvas
        self._canvas_field.update(self._operation_data, self._operation_axis, self._operation_light)