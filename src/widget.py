from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_information: str) -> str:
    masks_account_information = ''
    account_number = ''

    for slice_info in account_information.split():
        if slice_info.isalpha() is True:
            masks_account_information += slice_info + ' '
        elif slice_info.isdigit() is True:
            account_number += slice_info

    if masks_account_information == 'Счет ':
        masks_account_information += get_mask_account(account_number)
    else:
        masks_account_information += get_mask_card_number(account_number)

    return masks_account_information
