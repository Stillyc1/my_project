import os
import requests
from dotenv import load_dotenv


# импортируем данные из файла .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
URL_CONVERT = os.getenv("URL_CONVERT")


def converting_amount_transactions(transaction: list[dict]) -> float:
    """
    Функция принимает транзакцию вида dict и возвращает сумму транзакции,
    в случае валюты EUR или USD конвертирует сумму в RUB по актуальному курсу
    """
    for trans in transaction:
        if trans["operationAmount"]["currency"]["code"] == "RUB":
            return round(float(trans["operationAmount"]["amount"]), 2)

        else:
            url = URL_CONVERT
            payload = {
                "amount": trans["operationAmount"]["amount"],
                "from": trans["operationAmount"]["currency"]["code"],
                "to": "RUB",
            }

            headers = {"apikey": API_KEY}

            response = requests.get(str(url), headers=headers, params=payload)
            return round(float(response.json()["result"]), 2)
