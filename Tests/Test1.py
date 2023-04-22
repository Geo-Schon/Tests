geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def filter_the_list(obj: list) -> list:
    filter = []
    for el in obj:
        for country in el.values():
            if 'Россия' in country:
                filter.append(el)
    return filter


if __name__ == '__main__':

    for el in filter_the_list(geo_logs):
        print(el)
