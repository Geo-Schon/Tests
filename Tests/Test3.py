queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сводить детей в новый зоопарк',
    'пригласить мою жену на свидание',
    'где мне можно поспать',
    'заявление на'
]


def count_words_search(obj: list) -> dict:
    dict = {}
    one_percent = round(100 / len(obj), 2)

    for el in obj:
        count = len(el.split())
        string = f'Строка состоит из {count} слов'
        if string in dict:
            dict[string] += one_percent
        else:
            dict[string] = one_percent

    for key, value in dict.items():
        if int(value) - value == 0:
            dict[key] = int(value)
    return dict


if __name__ == '__main__':
    obj = count_words_search(queries)

    for key, value in obj.items():
        print(f'{key}: {value} %')

