#Faça um programa que mostre a letra da grade correspondente dependendo do valor de entrada, conforme tabela abaixo: 

grade = int(input('Insira o valor desejado: '))

if grade >= 90:
    print('Grade A')
elif grade >= 80:
    print('Grade B')
elif grade >= 70:
    print('Grade C')
elif grade >=60:
    print('Grade D')
else:
    print('Grade E')
