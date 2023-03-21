'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

*Пример:*

5
1 2 3 4 5
3
-> 1
'''

n = int(input("Input N: "))
import random
array = [random.randint(1, 10) for _ in range(n)]
print(*array, sep=", ", end="")
print()
x = int(input("Input X: "))
count = 0
for i in array:
    if i == x:
        count += 1
print(count)