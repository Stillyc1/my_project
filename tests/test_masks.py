from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(num_account):
    assert get_mask_account(num_account) == "**7890"


def test_get_mask_card_number(number_card):
    assert get_mask_card_number(number_card) == "1234 56** **** 3456"
