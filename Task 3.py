# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
from msilib import sequence
n = int(input('Введите число n '))
num = [round((1+1/i)**i,2) for i in range (1, n+1)]
print(num)
print(round(sum(num),2))