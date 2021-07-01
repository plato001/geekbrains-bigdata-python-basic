if __name__ == '__main__':
    # список
    lst = [1, 2.0, "string", [1, 2, 3], {"a", "b", "c"}, None, True]

    # проверим тип
    for el in lst:
        print("элемент списка - {}, его тип - {}".format(el, type(el)))
