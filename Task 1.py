# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = float(input('Введите число '))
sum = 0
def get_sum(num, sum):
    while num > 0:
        n = num % 10
        sum += n
        num = num // 10
    return sum

if num.is_integer():
    print(round(get_sum(num, sum)))
else:
    s = str(num)
    z = (abs(s.find('.') - len(s)) - 1)
    num = num * (10**z)
    print(round(get_sum(num, sum)))


