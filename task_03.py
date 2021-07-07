def my_func(x, y, z):
    return sum((x, y, z)) - min(x, y, z)


if __name__ == '__main__':
    print(my_func(1, 2, 3))
    print(my_func(12.4, -2.2, 3.5))
