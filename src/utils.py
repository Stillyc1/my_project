import json


def get_info_transactions(path_file: str) -> list[dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        with open(path_file, encoding="UTF-8") as file:
            try:
                file_dict = json.load(file)
                if type(file_dict) is not list:
                    return []
                return file_dict

            except json.JSONDecodeError:
                return []

    except FileNotFoundError:
        return []
