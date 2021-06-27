def calc_sum(n):
    # считаем сумму: n + nn + nnn
    result = n + int(str(n) * 2) + int(str(n) * 3)

    return result


if __name__ == '__main__':
    # запрос числа
    print("Введите целое число:")
    n = int(input())
    # сумма
    sum_ = calc_sum(n)
    # выводим результат
    print("Сумма: ", sum_)
