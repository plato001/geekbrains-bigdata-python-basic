def my_func(x, y):
    # степень числа
    power = 1.0

    while y > 0:
        power *= x
        y -= 1

    return power


if __name__ == '__main__':
    print(my_func(2.0, 3))
    print(my_func(2.0, 1))
    print(my_func(2.0, 0))
