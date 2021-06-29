if __name__ == '__main__':
    # доход
    print("Ввиде значение выручки фирмы:")
    revenue = float(input())
    # издержки
    print("Ввиде значение издержек фирмы:")
    cost = float(input())

    if revenue < cost:
        print("Фирма работает в убыток!")
    elif revenue > cost:
        print("Фирма прибыльная!")
        # рентабельность
        profitability = (revenue - cost) / revenue
        # запрос кол-ва сотрудников
        print("Введи кол-во сотрудников:")
        employees_count = int(input())
        profit_per_employee = (revenue - cost) / employees_count
        # вывод
        print("Рентабельность: {:.2f}".format(profitability))
        print("Прибыль в расчете на одного сотрудника: {:.2f}".format(profit_per_employee))
    else:
        print("Фирма работает в ноль (прибыль = убыток)!")
