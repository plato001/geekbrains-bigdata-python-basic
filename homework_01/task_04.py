def find_biggest_digit(num):
    # самая большая цифра
    biggest_digit = 0

    while num > 0:
        # цифра
        digit = num % 10
        # максимальная цифра
        biggest_digit = max(biggest_digit, digit)
        # уменьшаем разряд числа
        num = num // 10

    return biggest_digit


if __name__ == '__main__':
    # запрос числа
    print("Введите целое число:")
    n = int(input())
    # самая большая цифра
    biggest_digit = find_biggest_digit(n)
    # выводим результат
    print(f"Наибольшая цифра в числе {n} это {biggest_digit}")
