import json
import re
from collections import Counter
from src.decorators import log


@log("logs/work_func.txt")
def find_transactions(operations: list[dict], enter_user: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    return [operation for operation in operations if re.search(enter_user, operation.get("description", ""))]


@log("logs/work_func.txt")
def filtering_operations(operations: list[dict], list_of_categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    filter_ = [operation["description"] for operation in operations if operation.get("description", "") in list_of_categories]

    return dict(Counter(filter_))


# if __name__ == "__main__":
#     with open("../data/operations.json", encoding="UTF-8") as f:
#         operationss = json.load(f)
#
#     print(find_transactions(operationss, "Перевод"))
