from typing import Any
from src.decorators import log


@log("logs/work_func.txt")
def filter_by_currency(transaction: list, currency: str) -> Any:
    """
    Функция итерирует и возвращает операции из списка словарей transaction по параметру currency
    """
    for trans in transaction:
        if trans.get("operationAmount", "")["currency"]["code"] == currency:
            yield trans


@log("logs/work_func.txt")
def transaction_descriptions(transaction: list) -> Any:
    """
    генератор принимает список словарей и возвращает описание каждой операции по очереди
    """
    for trans in transaction:
        yield trans["description"]


@log("logs/work_func.txt")
def card_number_generator(first: int, last: int) -> Any:
    """
    генератор итерирует и возвращает номера карт в заданном диапазоне
    """
    for card in range(first, last + 1):
        card_numbers = str(card)
        while len(card_numbers) < 16:
            card_numbers = "0" + card_numbers
        formatted_card_number = f"{card_numbers[0:4]} {card_numbers[4:8]} {card_numbers[8:12]} {card_numbers[-4:]}"
        yield formatted_card_number
