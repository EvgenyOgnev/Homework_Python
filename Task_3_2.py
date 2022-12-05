# 3.2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите длину списка: '))
list_a = []
for _ in range(n):
    list_a.append(random.randint(-9, 10))
# print(list_a)


list_b = []
for i in range((len(list_a) + 1)//2):
    s = list_a[i]*list_a[-1 - i]
    list_b.append(s)

print(list_a, '=>>', list_b)
