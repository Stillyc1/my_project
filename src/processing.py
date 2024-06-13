

def filter_by_state(info_users: list[dict], state: str = 'EXECUTED') -> list[dict]:
    sort_info_users = []
    for info in info_users:
        if info['state'] == state:
            sort_info_users.append(info)

    return sort_info_users


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))
