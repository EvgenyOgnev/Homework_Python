# 3.4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a_a = int(input('Enter a number: '))  # V_1 математический
a = a_a
b = 0
num = 0
c = 1/10
count = 0

while a > 0:
    b = a % 2
    a = a // 2
    c = c * 10
    num = num + b * c
    count += 1
print(f'V_1: {a_a} --> {round(num)}')


result = []  # V_2 с помощью списка
i = 0
a1 = a_a
while a1 > 0:
    s = a1 % 2
    result.append(s)
    a1 = a1 // 2
    i += 1
# print(result)

print('V_2:', a_a, '-->', end=' ')
for j in range(len(result)):
    print(result[(-1-j)], end='')

