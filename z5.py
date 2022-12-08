# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# # В file1.txt :
# # 2*x**2 + 4*x + 5
# # В file2.txt:
# # 4*x**2 + 1*x + 4
# # Результирующий файл:
# # 6*x**2 + 5*x + 9

from sympy import simplify 

with open('file1.txt', 'r') as Data1:
    pol1 = Data1.read()
    print(pol1)
with open('file2.txt', 'r') as Data2:
    pol2 = Data2.read()
    print(pol2)
sum = simplify(pol1 + "+" + pol2)

print(sum)
