import os
from typing import Any

""" Импортируем библиотеку os """


def find_to_directory(folder_path: str = os.getcwd(), recursive_counting: Any = None) -> dict:
    """
    Функция принимает путь до директории и возвращает кол-во файлов и папок в директории
    """
    directory_count_files = {"files": 0, "folders": 0}

    if os.path.isdir(folder_path) is True:
        find_dir = os.scandir(folder_path)

        for file in find_dir:
            if os.path.isfile(file) is True:
                directory_count_files["files"] += 1
            elif os.path.isdir(file) is True:
                directory_count_files["folders"] += 1

    if recursive_counting is not None:
        for root, dirs, files in os.walk(folder_path):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))

    return directory_count_files
