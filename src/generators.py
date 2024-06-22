def filter_by_currency(transaction, currency):
    for trans in transaction:
        if trans["operationAmount"]["currency"]["code"] == currency:
            yield trans


def transaction_descriptions(transaction):
    for trans in transaction:
        yield trans["description"]


def card_number_generator(first, last):
    for card in range(first, last+1):
        card_numbers = str(card)
        while len(card_numbers) < 16:
            card_numbers = '0' + card_numbers
        formatted_card_number = f'{card_numbers[0:4]} {card_numbers[4:8]} {card_numbers[8:12]} {card_numbers[-4:]}'
        yield formatted_card_number
