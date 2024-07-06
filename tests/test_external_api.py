from src.external_api import converting_amount_transactions
from unittest.mock import patch


@patch('requests.get')
def test_converting_amount_transaction(mock_get, info_transaction):
    mock_get.return_value.json.return_value = 31957.58
    assert converting_amount_transactions(info_transaction) == 31957.58
