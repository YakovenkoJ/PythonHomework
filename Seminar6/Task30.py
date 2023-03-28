"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

first = int(input('Input the first element of the arithsetical progression: '))
d = int(input('Input the difference of the arithsetical progression: '))
q = int(input('Input the quantity of the arithsetical progression: '))

progression = list()

for num in range(q):
    progression.append(first + num * d)

print(progression) 