ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def dictionary_filter(obj: dict) -> list:
    obj_set = set()
    for el in obj.values():
        for item in el:
            obj_set.add(item)
    return list(obj_set)


if __name__ == '__main__':
    lst = dictionary_filter(ids)
    print(lst)
