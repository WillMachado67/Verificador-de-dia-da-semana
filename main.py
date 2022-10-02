def calc_week(day, month, age):
    week = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

    if month == 11 or month == 12:
        age -= 1

    # Algoritimo para saber o dia da semana
    left4 = (age % 4) * 5
    left100 = (age % 100) * 4
    left400 = (age % 400) * 6
    calc_month = int(2.6 * month - 0.2)
    derived = left4 + left100 + left400 + calc_month + day
    number_week = derived % 7

    return week[number_week]


print(calc_week(2, 8, 2022))
