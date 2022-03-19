#Jogo Par ou Impar 
#Jogador escolhe entre par ou impar e coloca os dedos (10 dedos) 

import random

escolha =  int(input('Escolha [0]-Par ou [1]-Impar: '))
jogador = int(input('Quando dedos você vai lançar?: '))
computador = random.randint(0,10) # Modo aleatório

print(f'O Computador escolheu {computador} dedos')
print(f'O jogador escolheu {jogador} dedos')

soma = jogador + computador

if soma % 2 == 0 and escolha == 0:
    print ('O Jogador ganhou')
else: print('O computador ganhou')