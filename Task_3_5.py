# 3.5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(k))

list = []
for i in range(-k, k + 1):
    if i < 0:
        s = ((-1)**(i*(-1)+1))*(fib(i*(-1)))
        list.append(s)
    else:
        list.append(fib(i))

print(list)
