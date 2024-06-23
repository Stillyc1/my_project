from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, currency_test):
    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        assert next(usd_transactions)["id"]


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)

    for _ in range(5):
        assert next(descriptions)


def test_card_number_generator():
    for card_number in card_number_generator(1, 5):
        assert card_number
