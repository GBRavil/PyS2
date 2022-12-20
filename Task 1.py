# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = float(input('Введите число '))
sum = 0
if num.is_integer():
    while num > 0:
        n = num % 10
        sum += n
        num = num // 10
    print(round(sum)) 
else:
    s = str(num)
    z = (abs(s.find('.') - len(s)) - 1)
    num = num * (10**z)
    while num > 0:
        n = num % 10
        sum += n
        num = num // 10    
    print(round(sum)) 