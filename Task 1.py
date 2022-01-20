"""
Задание 1.
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
- среднюю букву, если число букв в слове нечетное;
- две средних буквы, если число букв четное.
"""
word = "child"

if len(word) % 2 != 0:
    ind_odd = ind_odd = len(word) // 2
    print(f'{word[ind_odd]}')
else:
    ind_even1 = len(word) // 2
    ind_even2 = len(word) // 2 + 1
    print(f'{word[ind_even1]}{word[ind_even2]}')