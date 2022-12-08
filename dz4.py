# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x*1 + 5*x*0 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x*1 + 5 = 0 
# from random import randint
# from sympy import symbols
# from math import prod
 
# max_val = 100
# k = int(input('Введите натуральную степень k:'))
# # коэфф. при старшей степени не должен быть равен 0
# koeff = [randint(-max_val, max_val) for i in range(k)]+[randint(1, max_val)]
# x = symbols('x')
# print(sum(map(prod, zip(koeff, [x**i for i in range(k+1)]))), '= 0')

from random import randint
k = int(input("Введите коэффициент: "))
polindrom = ''
for i in range(k, 0, -1):
    if (i > 1):
        polindrom += ((str(randint(0, 101))) + 'x' + '^' + str(i) + '+')
    else:
        polindrom += ((str(randint(0, 101))) + 'x' + '+')
print(polindrom + (str(randint(0, 101)) + '= 0'))
