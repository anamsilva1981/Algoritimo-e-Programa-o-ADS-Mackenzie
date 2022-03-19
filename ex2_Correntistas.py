# Receba o saldo em conta corrente de um correntista, calcule e mostre o valor de crédito, dependendo do saldo informado conforme tabela abaixo: 

#Exemplos de códigos para o mesmo exercicios

# Exemplo 1

saldo = float(input('Digite o saldo: '))

if saldo > 4000:
    credito = saldo * 0.30
elif saldo >= 3000:
    credito = saldo * 0.25
elif saldo >= 2000:
    credito = saldo * 0.20
else:
    credito = saldo * 0.10
print(f'Crédito = {credito}')


# Exemplo 2
saldo = float(input('Digite o saldo: '))

if saldo > 4000:
    credito = 0.30
elif saldo >= 3000:
    credito = 0.25
elif saldo >= 2000:
    credito = 0.20
else:
    credito = 0.10
print(f'Crédito = {saldo * credito}')
