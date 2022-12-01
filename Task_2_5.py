# 5. Реализуйте алгоритм перемешивания списка.

n = int(input('Введите число: '))

b = []
for _ in range(-n, n + 1, 2):
    b.append(_)
print(b)

import random
random.shuffle(b)
print(b)
