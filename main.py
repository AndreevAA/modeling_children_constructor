# Подключение конфигурации

# Основной блок программы
import detail
from interface import Interface


def main():
    detail.UploadingDetails("/input_files/1.txt")
    Interface()


# Старт программы
if __name__ == '__main__':
    main()


