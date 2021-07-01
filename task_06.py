def add_item(goods, item_name, item_price, item_count, item_unit):
    # номер товара
    n = len(goods) + 1

    goods.append(
        (
            n,
            {
                "название": item_name,
                "цена": item_price,
                "количество": item_count,
                "ед": item_unit
            }
        )
    )

    return goods


def make_analytics(goods):
    # результат
    res = dict()

    for n, item in goods:
        for k, v in item.items():
            # читаем текущее значение для res
            buf = res.get(k)

            if buf is None:
                res[k] = [v]
            else:
                # добавляем к нему новое значение
                if v not in buf:
                    buf.append(v)
                # обновляем значение в res
                res[k] = buf

    return res


if __name__ == '__main__':
    # структура Товары
    goods = []

    # запрос товаров у пользователя
    for _ in range(3):
        name = input()
        price = int(input())
        count = int(input())
        unit = input()
        goods = add_item(goods, name, price, count, unit)

    # аналитика
    analytics = make_analytics(goods)
    print(analytics)
