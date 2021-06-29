def to_timeformat(seconds):
    # кол-во часов
    h = seconds // 3600
    # кол-во минут
    m = (seconds - h * 3600) // 60
    # кол-во секунд
    s = seconds - h * 3600 - m * 60
    # результат
    result = f"{h:02d}:{m:02d}:{s:02d}"

    return result


if __name__ == '__main__':
    # запрос секунд
    print("Введите кол-во секунд:")
    seconds = int(input())
    # переводим в нужный формат
    timeformat = to_timeformat(seconds)
    # выводим результат
    print("Часовой формат: ", timeformat)
