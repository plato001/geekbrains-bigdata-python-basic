def int_func(word):
    return word.capitalize()


if __name__ == '__main__':
    # входная строка
    print("Введите строку из слов с маленькой буквы, разделенных пробелами: ")
    input_text = input()

    # результирующая строка
    output_text = " ".join([int_func(w) for w in input_text.split()])
    print(output_text)
