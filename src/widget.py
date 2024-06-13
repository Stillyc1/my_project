from src.masks import get_mask_account, get_mask_card_number

"""Импортируем функции из модуля masks.py"""


def mask_account_card(account_information: str) -> str:
    """
    Функция принимает номер карты\\счета (в формате "карта\\счет (номер карты\\счета)
    и возвращает строку с замаскированным номером карты\\счета
    """
    masks_account_information = ""
    account_number = ""

    for slice_info in account_information.split():
        if slice_info.isalpha() is True:
            masks_account_information += slice_info + " "
        elif slice_info.isdigit() is True:
            account_number += slice_info

    if masks_account_information == "Счет ":
        masks_account_information += get_mask_account(account_number)
    else:
        masks_account_information += get_mask_card_number(account_number)

    return masks_account_information


def get_data(info_data: str) -> str:
    """Функция принимает дату и преобразует в формат дд.мм.гггг"""
    data_day = info_data.split("T")[0]

    return f"{data_day.split('-')[-1]}.{data_day.split('-')[-2]}.{data_day.split('-')[-3]}"


def formatting_the_list(a_list_of_lines: list[str]) -> list:
    """
    Функция принимает на вход список строк
    и возвращает список строк, в которых первая и последняя буквы совпадают
    """
    new_list = []
    for line in a_list_of_lines:
        if line == "" or line[0] == line[-1]:
            new_list.append(line)

    return new_list


def multiply_the_numbers(list_of_numbers: list[int]) -> int:
    """
    Функция принимает на вход список целых чисел
    и возвращает максимальное произведение двух чисел из списка.
    """
    new_list = list()
    for num in list_of_numbers:
        num_str = str(num).replace("-", "")
        new_list.append(int(num_str))

    sort_list = sorted(new_list)

    if len(sort_list) < 2:
        return 0
    else:
        return int(sort_list[-1] * sort_list[-2])
