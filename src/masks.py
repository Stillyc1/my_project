import logging
from src.decorators import log


""" создаем логгер для логирования функций и пишем логи в директорию logs"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("masks.py")


@log("logs/work_func.txt")
def get_mask_card_number(number_card: int | str) -> str:
    """
    Функция принимает номер карты и возвращает
    номер карты с маскировкой 6ти цифр (с 7 - 12)

    p.s. вход преобразуем в строку, заменяем цифры с 7-12,
    по индексу делим номер карты на 4 блока,
    возвращаем, разделяем пробелом
    """

    number_card_string = str(number_card)
    mask_card = number_card_string.replace(number_card_string[6:12], "******")
    number_card_divide = mask_card[:4], mask_card[4:8], mask_card[8:12], mask_card[12:]
    mask_number_card = " ".join(number_card_divide)

    logger.info("Маскировка карты клиента")

    return mask_number_card


@log("logs/work_func.txt")
def get_mask_account(account_number: int | str) -> str:
    """
    Функция принимает номер счёта и возвращает маскировку счета
    в формате: "** 4цифры счета"
    """

    account_number_string = str(account_number)

    logger.info("Маскировка номера счёта клиента")

    return f"**{account_number_string[-4:]}"
