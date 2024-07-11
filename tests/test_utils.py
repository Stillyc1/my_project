from src.utils import get_info_transactions, get_info_transactions_csv, get_info_transactions_xlsx


def test_get_info_transactions(info_transaction):
    assert get_info_transactions(1) == []
    assert get_info_transactions("") == []

    assert get_info_transactions("../data/test.operations.json") == info_transaction


def test_get_info_transactions_csv(test_info_csv, test_info_xlcx):
    info_csv = list(get_info_transactions_csv("../data/transactions.csv"))
    assert info_csv == test_info_csv

    info_xlsx = list(get_info_transactions_xlsx("../data/transactions_excel.xlsx"))
    assert info_xlsx == test_info_xlcx
