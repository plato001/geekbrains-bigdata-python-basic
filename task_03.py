def find_season_with_list(m):
    # список времен года
    seasons = 2 * ["зима"] + 3 * ["весна"] + 3 * ["лето"] + 3 * ["осень"] + ["зима"]

    return seasons[m - 1]


def find_season_with_dict(m):
    # словарь времен года
    seasons = {
        1: "зима",
        2: "зима",
        3: "весна",
        4: "весна",
        5: "весна",
        6: "лето",
        7: "лето",
        8: "лето",
        9: "осень",
        10: "осень",
        11: "осень",
        12: "зима"
    }

    return seasons[m]


if __name__ == '__main__':
    print("Введите месяц в виде целого числа от 1 до 12:")
    month = int(input())

    # время года
    season_list = find_season_with_list(month)
    season_dict = find_season_with_dict(month)

    print("Время год через list: ", season_list)
    print("Время год через dict: ", season_dict)
