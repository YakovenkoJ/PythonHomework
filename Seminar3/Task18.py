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

N = int(input("Input N: "))
A = list(range(1, N + 1))
print(*A, sep=", ", end="")
print()
X = int(input("Input X: "))
if X <= A[0]:
    print(A[0])
elif X >= A[- 1]:
    print(A[- 1])
else:
    print(X)