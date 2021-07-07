def my_div(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ValueError:
        return "Ошибка! Вводить нужно только числа."
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль."


if __name__ == '__main__':
    a = input("введите первое число: ")
    b = input("введите второе число: ")

    print(my_div(a, b))
