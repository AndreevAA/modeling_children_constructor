# Объект показа ошибки
from tkinter import messagebox

import config


class Message:

    # Инициализация объекта вывода сообщений об ошибках
    def __init__(self, _error_status):

        messagebox.showerror("Ошибка",
                             config.MESSAGE_ERROR_TEXT[_error_status])