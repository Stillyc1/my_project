def sorting_contents_file(name_file: str) -> list:
    """ Функция читает исходный файл и преобразует его
    в список с правильно оформленными именами, без символов и пробелов"""
    with open(name_file, "r", encoding="utf-8") as file:
        content = file.readlines()

    new_file = []
    for values in content:
        sort_values = "".join(c for c in values if c.isalpha())
        new_file.append(sort_values)

    for file in new_file:
        if file == "":
            new_file.remove(file)

    return new_file
