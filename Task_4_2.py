# 4.2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# добавил разложения на простые множители числа N.

n = int(input('Введите число: '))

def list_prime_factors(n):
    list_prime = [2, ]
    for i in range(3, n + 1):
        for j in list_prime:
            if i % j == 0:
                break
        else:
            list_prime.append(i)
    return list_prime


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:  # перебираем простой делитель
        while n % i == 0:  # пока 'n' на него делится
            n //= i  # делим 'n' на этот делитель
            factors.append(i)
        i += 1
    if n > 1: # в конце 'n' стало большим простым числом, у которого мы дошли до корня и поняли, что оно простое. Eго тоже нужно добавить...
        factors.append(n)
    return factors

print(list_prime_factors(n))
factorize_ = factorize(n)
print(factorize_)
print(n, '=', ' x '.join(str(y) for y in factorize_))
