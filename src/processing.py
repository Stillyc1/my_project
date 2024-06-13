def filter_by_state(info_users: list[dict], state: str = 'EXECUTED') -> list[dict]:
    sort_info_users = []
    for info in info_users:
        if info['state'] == state:
            sort_info_users.append(info)

    return sort_info_users
