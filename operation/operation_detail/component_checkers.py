import config, detail.light


# Проверка: Компонента в тени
def is_component_in_shadow(checking_component, _operation_details, _light):
    is_component_in_shadow_status = config.ERROR_STATUS

    for _detail in _operation_details.operation_detail:
        for _component in _detail.components:
            _component_vertexes = _component.get_component_vertexes()
            _component_faces = _component.get_component_faces()

            # Проход по всем наборам граней
            for _component_face_vertexes in _component_faces:

                # Список пар координат вершин
                _polygon_pairs_of_vertexes = []

                # Добавление в список пар координат вершин пар вершин
                for _number_of_vertex in _component_face_vertexes:
                    # Текущая вершина по позиции
                    _vertex = _component_vertexes[int(_number_of_vertex)]

                    # Добавление данных текущей вершины
                    _polygon_pairs_of_vertexes.append([_vertex.get_x_position(),
                                                       _vertex.get_y_position()])



            if not is_the_same_object(checking_component, _component):

                # for _moving_vertex in _component.get_component_vertexes():
                #     _moving_vertex.update(_moving_vertex.get_x_position() + x_move,
                #                           _moving_vertex.get_y_position() + y_move,
                #                           _moving_vertex.get_z_position() + z_move)

    return is_component_in_shadow_status


# Проверка одной и той же
def is_the_same_object(_first, _second):
    return _first == _second
