if __name__ == '__main__':
    # предложение
    print("Введи строку (слова разделяются пробелами):")
    str_ = input()

    for i, token in enumerate(str_.split()):
        print("слово номер {}: {}".format(i + 1, token[:10]))
