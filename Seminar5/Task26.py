'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
'''

def exponentation(a, b):
    if b == 0:
        return 1
    return a*exponentation(a, b - 1)

number = int(input("Введите число: "))
power = int(input("Введите степень: "))

res = exponentation(number, power)
print(f"Число {number} в степени {power} = {res}")