# author Melissa Lopes
import math
print('Digite a: ')
a = float(input())
print('Digite b: ')
b = float(input())
print('Digite c: ')
c = float(input())

delta = math.sqrt((b ** 2) - ((4 * a) * c))
ylinha = ((-b + delta) / (2 * a))
y2linha = ((- b - delta) / (2 * a))

print('raíz 1: ', ylinha)
print('raíz 2: ', y2linha)