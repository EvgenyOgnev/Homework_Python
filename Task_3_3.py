# 3.3 Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

import random
n = int(input('Введите длину списка: '))
list_a = []
for _ in range(n):
    list_a.append((random.randint(0, 10000))/100)
print(list_a)

for i in range(len(list_a)):
    g = (str(list_a[i])).split('.')[1]
    list_a[i] = int(g)/(10**(len(g)))

max_j = list_a[0]
min_j = list_a[0]
for j in range(1, len(list_a)):
    if list_a[j] > max_j:
        max_j = list_a[j]
    elif list_a[j] < min_j:
        min_j = list_a[j]

print(f' =>> max(дробной части) - min(дробной части) = {max_j - min_j}')
