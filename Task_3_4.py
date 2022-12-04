# 3.4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# double b = 0;
# double num = 0;
# double c = 1;
# for (int i = 0; a > 0; i++)
# {
#     b = a % 2;
#     a = a / 2;
#     c = c * 10;
#     num = num + b * c;
# }
# Console.WriteLine($"число: {num / 10}");

# int [] result = new int [(int)(Math.Log(num, 2) + 1)];
# int count = 0

# while(num > 0)
# {
#     result[result.Length-1-count] = num %2;
#     num=num/2;
#     count ++;
# }
# for(int i = 0; i < result.Length; i++)
# {
#     Console.Write($"{result[i]} ");
# }

