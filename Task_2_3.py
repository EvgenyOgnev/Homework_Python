# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input('Введите число: '))
sum = 0
for i in range (1, n + 1):
    sum = sum + ((1+(1/i))**i)
#    print(((1+(1/i))**i), end=' ')
print(f'Для n = {n}: Сумма = {round(sum, 2)}')

