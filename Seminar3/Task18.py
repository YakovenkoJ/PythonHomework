'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

*Пример:*

5
1 2 3 4 5
6
-> 5
'''

n = int(input("Input N: "))

import random
array = [random.randint(1, 100) for _ in range(n)]
print(*array, sep=", ", end="")
print()

x = int(input("Input X: "))

new_array = []
for num in range(len(array)):
    k = abs(x - array[num])
    new_array.append(k)
#print(new_array)

from operator import itemgetter
index = min(enumerate(new_array), key=itemgetter(1))[0]

print(array[index])