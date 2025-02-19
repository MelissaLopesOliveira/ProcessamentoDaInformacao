# Digite um valor e o programa informa o próximo número ímpar depois dele
num = int(input())
proximoimpar = num + 1 - (num % 2)
print(proximoimpar)