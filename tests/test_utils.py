from src.utils import get_info_transactions


def test_get_info_transactions(info_transaction):
    assert get_info_transactions(1) == []
    assert get_info_transactions("") == []

    assert get_info_transactions("../data/test.operations.json") == info_transaction
