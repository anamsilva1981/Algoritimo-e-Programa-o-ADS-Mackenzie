# Leia a nota e o número de faltas de um aluno e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas, ocorre uma redução de conceito: 

nota = float(input('Digite a nota do aluno: '))
falta = int(input('Digite a quantidade de faltas do aluno: '))

if nota >= 0 and nota <= 3.9: 
    conceito = 'E' #Se a nota for inferior a 4 ele entra no conceito E
elif nota <= 4.9: #Se a nota for inferior a 5 
    if falta <= 20:  # Mas as faltas forem inferiores a 20
        conceito = 'D' # então o conceito dele será D
    else:
        conceito = 'E' # Caso contrario, será E 
elif nota <= 7.4:
    if falta <=20:
        conceito = 'C'
    else:
        conceito = 'D'
elif nota <= 8.9:
    if falta <= 20:
        conceito = 'B'
    else:
        conceito = 'C'
else:
    if falta <=20:
        conceito = 'A'
    else:
        conceito = 'B'
print(f' O conceito do aluno é {conceito}')
    


