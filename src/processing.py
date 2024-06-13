from typing import Any


def filter_by_state(info_users: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция возвращает список словарей, по параметру 'state' """
    sort_info_users = []
    for info in info_users:
        if info["state"] == state:
            sort_info_users.append(info)

    return sort_info_users


def sort_by_date(info_dicts: list[dict], sorting_parameter: Any = None) -> list[dict]:
    """Функция сортирует список словарей по параметру 'date' """
    if sorting_parameter is not None:
        return sorted(info_dicts, key=lambda date: date["date"])
    else:
        return sorted(info_dicts, key=lambda date: date["date"], reverse=True)
