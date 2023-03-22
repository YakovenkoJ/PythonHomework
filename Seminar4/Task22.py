'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества, 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
array_1 = [int(input(i)) for i in range(n)]
print(array_1)

array_2 = [int(input(j)) for j in range(m)] 
print(array_2)

repeated_numbers = set()
for i in array_1:
    for j in array_2:
        if i == j:
            repeated_numbers.add(i)
print(repeated_numbers)