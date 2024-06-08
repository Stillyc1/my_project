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
