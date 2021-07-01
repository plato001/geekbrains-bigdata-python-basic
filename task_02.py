def make_swap_in_list(lst):
    # результат
    res = []
    # последний индекс для swap
    last_swap_index = len(lst) if len(lst) % 2 == 0 else len(lst) - 1

    # заполняем swap-список
    for i in range(0, last_swap_index, 2):
        res += [lst[i+1], lst[i]]

    # добавляем оставшиеся элементы
    res += lst[last_swap_index:]

    return res


if __name__ == '__main__':
    # список
    print("Введите элементы списка через пробел:")
    input_lst = input().split()

    # обмен соседних элементов
    swap_lst = make_swap_in_list(input_lst)

    print("Исходные список: ", " ".join(input_lst))
    print("Список с перестановками соседних: ", " ".join(swap_lst))
