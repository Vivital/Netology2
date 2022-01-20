"""
Задание 4.
У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах
за произвольный период по странам (структура данных в примере).
Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!)
для каждой страны.
"""
countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
thailand = countries_temperature[0][1]
thailand_avg = sum(thailand) / len(thailand)
thailand_avg_cels = (thailand_avg - 32) * (5/9)

germany = countries_temperature[1][1]
germany_avg = sum(germany) / len(germany)
germany_avg_cels = (germany_avg - 32) * (5/9)

russia = countries_temperature[2][1]
russia_avg = sum(russia) / len(russia)
russia_avg_cels = (russia_avg - 32) * (5/9)

poland = countries_temperature[3][1]
poland_avg = sum(poland) / len(poland)
poland_avg_cels = (poland_avg - 32) * (5/9)

print('Средняя температура в странах:')
print(f'{countries_temperature[0][0]} - {thailand_avg_cels:.1f} C')
print(f'{countries_temperature[1][0]} - {germany_avg_cels:.1f} C')
print(f'{countries_temperature[2][0]} - {russia_avg_cels:.1f} C')
print(f'{countries_temperature[3][0]} - {poland_avg_cels:.1f} C')