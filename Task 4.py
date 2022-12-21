# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке/
from random import randint
num = []
n = int(input('Введите число N '))
for i in range(n):
    num.append(randint(-n,n))
print('Список элементов',num)

x = int(input('Введите номер позиция первого числа '))
y = int(input('Введите номер позиция второго числа '))
if x < n and y < n and x >= 0 and y >= 0:
    count = [x,y]
else: 
    print('Введена некорректная позиция, укажите от 0 до',n)
print('Список позиций',count)

mult = num[x] * num[y]
print(f'Произведение элементов: {num[x]} * {num[y]} = {mult}')