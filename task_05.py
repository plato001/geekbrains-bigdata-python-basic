def my_sum():
    sum = 0

    while True:
        print("Введите числа, разделенные пробелами. Для завершения ввода введите символ 'q': ")
        input_data = input().split()

        # просуммируем числа
        for num in input_data:
            if num == "q":
                return sum
            else:
                try:
                    sum += float(num)
                except ValueError:
                    print("Ошибка! Вводить нужно только числа. Если нужно завершить, то введите 'q'")

        print("Сумма = {}".format(sum))


if __name__ == '__main__':
    print(my_sum())
