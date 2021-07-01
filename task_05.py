def add_rating(lst, r):
    # если r нет в списке
    if r not in lst:
        lst.append(r)
        lst = sorted(lst, reverse=True)
        return lst

    # первый индекс вхождения r в lst
    first_ind = lst.index(r)
    # кол-во вхождений
    count = lst.count(r)
    # конечный индекс
    last_ind = first_ind + count

    # строим результирующий список
    res = lst[:last_ind] + [r] + lst[last_ind:]

    return res


if __name__ == '__main__':
    # набор натуральных чисел
    my_list = [7, 5, 3, 3, 2]

    # рейтинг
    print("Введите рейтинг (натуральное число):")
    rating = int(input())

    # добавим рейтинг в список
    my_list = add_rating(my_list, rating)
    print(my_list)
