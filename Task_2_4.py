# 	4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите число: '))
i_n = input(f'Введите индексы, через пробел: ')

b = []
for k in range(-n, n + 1):
    b.append(k)
print(b)

i_n = i_n.split()
val = 1
for i in range(len(i_n)):
    q = int(i_n[i])
    val = val*b[q]
print(f'произведение элементов на указанных индексах = {val}')
