#O codigo de transito brasileiro (ctb) prevê, para conduzir veiculos automotores a pessoa precisa ter idade minima de 18 anos
#Elabore um algoritmo que peça o nome e emque ano a pessoa nasceu, e retorne se esta pessoa pode dirigir

#não totalmente satisfeito com o sistema e precisando de mais informações
#O cliente precisa saber agora, quando não puder dirigir, quando anos ele precisa esperar para poder 
#dirigir.

nome = input("INFORME SEU NOME: ")
ano = int(input("INFORME SEU ANO DE NASCIMENTO: "))
anoatual = 2022
idade = anoatual - 2004


if (anoatual - ano >= 18):
     print(nome  + ' você é apto a dirigir' )

else:
     print(nome  + ' nao pode dirigir.Faltam ' + (str(18-(2022-ano))) + ' anos para dirigir')