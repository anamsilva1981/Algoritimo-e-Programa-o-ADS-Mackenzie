#Fça um programa em python que receba um valor referente ao ano e emita mensagem se este ano é ou não bissexto.

#São bissextos todos os anos multiplos de 400 / Multiplos de 4 exceto se formultiplo de 100 mas não de 400 por exemplo: 1996, 2000, 20004, 20008, 2012, 2016, 2020
import math

ano = int(input('Insira o ano a ser analisado: \n'))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0 ):
    print(f'O ano {ano} é bissexto')
else: 
    print(f'O ano {ano} não é bissexto')