"""
Задание 5.
Дан поток логов по количеству просмотренных страниц для каждого пользователя.
Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя.
Т.е. надо посчитать отношение суммы всех просмотров к количеству уникальных пользователей.
"""
stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]

pages = [int(i.split(',')[2]) for i in stream]
users = [i.split(',')[1] for i in stream]
users_unique = set(users)
print(f'Среднее количество просмотров на уникального пользователя: {sum(pages)/len(users_unique)}')