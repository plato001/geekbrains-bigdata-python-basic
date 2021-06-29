if __name__ == '__main__':
    # входные данные
    print("Введите кол-во км в 1-й день:")
    a = float(input())
    print("Введи конечный результат в км:")
    b = float(input())

    # кол-во дней для достижения результата b
    if a >= b:
        print("Результат в {} км уже достигнут в 1-й день!".format(b))
    else:
        days_count = 1

        while a < b:
            a *= 1.1
            days_count += 1

        print(
            "на {}-й день спортсмен достиг результата — не менее {} км.".format(days_count, b)
        )
