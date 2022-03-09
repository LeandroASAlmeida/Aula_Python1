#ELABORE UM ALGORITMO  QUE PEÇA  O USUARIO INFORMAR DOIS VALORES INTEIROS
#A CALCULADORA DEVERA IMPRIMIR A SOMA , SUBTRAÇÃO, DIVISÃO E MULTIPLICAÇÃO DOS VALORES.


valor1 = int(input("INFORME UM VALOR: "))
valor2 = int(input("INFORME OUTRO VALOR: "))
escolha = (input("Qual operação deseja fazer?"))


if escolha == '+':
    print('Soma: ' + str((valor1+valor2)))#soma
elif escolha == '-':
    print('Subtração: ' + str((valor1-valor2)))#subtração
elif escolha == '/':
    print('Divisão: ' + str((valor1/valor2)))#divisão
elif escolha == '*':
    print('Multiplicação: ' + str((valor1*valor2)))#multiplicação
else:
    print('Operação Invalida')

# Agora o sistema deve perguntar qual operação aritimética o cliente deseja executar