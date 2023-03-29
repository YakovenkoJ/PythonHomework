"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
"""

import random
array = [random.randint(1, 30) for _ in range(10)]
# print(array)
min_value = 1
max_value = 10
new_array = []

for i in range(len(array)):
    if min_value < array[i] < max_value:
        new_array.append(i)

print(*new_array, sep=", ", end=" ")
