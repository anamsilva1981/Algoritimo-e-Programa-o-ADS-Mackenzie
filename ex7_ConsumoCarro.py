# 3 . Faça um programa em Python que leia a quantidade em km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em km/litros e escreva uma mensagem de acordo com a tabela abaixo:  

combustivel = float(input('Insira a quantidade de combustivel consumido> \n'))
km = float(input('Insira a quantidade de Kilometros rodados: \n'))
media = km / combustivel

if media < 8:
    print('Venda o carro ')
elif media >= 8 and media <= 12:
    print('Carro econômico ')
else: 
    print('Super Econômico')

