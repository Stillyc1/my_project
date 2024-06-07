import os


def sorting_contents_file(name_file: str):
    with open(name_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    new_file = []
    for values in content:
        sort_values = "".join(c for c in values if c.isalpha())
        new_file.append(sort_values)

    for file in new_file:
        if file is "":
            new_file.remove(file)

    for name in new_file:
        print(name)


sorting_contents_file('../data/names.txt')
