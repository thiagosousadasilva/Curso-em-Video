#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
#possíveis sobre ele.
print("=========== desafio 004 ============")
n = input("Digite algo: ")
print('Você digitou "{}", e essas são as propriedades: '.format(n))
print('O tipo primitivo desse valor é: {}'.format(type(n)))
print('Alfanumérico: {}'.format(n.isalnum()))
print('Alfabético: {}'.format(n.isalpha()))
print('Numérico: {}'.format(n.isnumeric()))
print('ASCII: {}'.format(n.isascii()))
print('Decimal: {}'.format(n.isdecimal()))
print('Digito: {}'.format(n.isdigit()))
print('Identificador: {}'.format(n.isidentifier()))
print('Minúsculo: {}'.format(n.islower()))
print('Printável: {}'.format(n.isprintable()))
print('Contém apenas espaços: {}'.format(n.isspace()))
print('Title: {}'.format(n.istitle()))
print('Maiúsculo: {}'.format(n.isupper()))