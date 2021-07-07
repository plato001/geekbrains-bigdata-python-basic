def user_data(first_name, last_name, birth_year, city, email, phone):
    return "имя: {}, фамилия: {}, год рождения: {}, город проживания: {}, почта : {}, телефон: {} "\
            .format(first_name, last_name, birth_year, city, email, phone)


if __name__ == '__main__':
    print(
        user_data(
            "Темирлан",
            "Смаил",
            "1992",
            "Алматы",
            "smile314@yandex.ru",
            "+7(776)392-9227"
        )
    )
