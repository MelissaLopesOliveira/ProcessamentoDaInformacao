# Verificar se o ano informado é bissexto ou não
print('Informe o ano: ')
ano = int(input())
ano1 = (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0)
print(ano1)
