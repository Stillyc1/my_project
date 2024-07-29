from src.utils import get_info_transactions, get_info_transactions_csv, get_info_transactions_xlsx
from unittest.mock import patch, mock_open, Mock
import pandas as pd


def test_get_info_transactions(info_transaction):
    assert get_info_transactions(1) == []
    assert get_info_transactions("") == []

    assert get_info_transactions("../data/test.operations.json") == info_transaction


def test_get_info_transaction(test_info_csv, test_info_xlcx):
    info_csv = list(get_info_transactions_csv("../data/transactions.csv"))
    assert info_csv[0] == test_info_csv

    info_xlsx = list(get_info_transactions_xlsx("../data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("tests.test_utils.pd.read_csv")
def test_get_info_transactions_csv(test_info_csv, test_info_xlcx):
    Mock.return_value = pd.DataFrame()
    assert get_info_transactions_csv('foo') == []

    info_xlsx = list(get_info_transactions_xlsx("../data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_info_transactions_csv_xlsx(mock_file):
    assert open("../Data/test_transactions.csv").read() == "data"
    mock_file.assert_called_with("../Data/test_transactions.csv")

    assert open("../Data/transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../Data/transactions_excel.xlsx")
