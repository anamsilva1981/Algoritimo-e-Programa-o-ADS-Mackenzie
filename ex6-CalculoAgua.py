#Faça um programa para resolver o seguinte problema: A empressa local de abastecimento de água, a sabeamento básico da cidade SBC está promovendo uma campanha de conservação de água, distribuindo cartilhas e promovendo ações demonstrando a importância da água para a vida e para o meio ambiente. 
# Para incentivar mais ainda a economia de água, a SBBC alterou os preços de seu fornecimento de forma que, proporcionamente, aqueles clientes que consumirem menos água paguem menos pelo metro cubico.
# Todo clinte paga mensalmente uma assinatura de R$ 7,00 que incuiu uma franquia de 10M3 de água. Isto é, para qualquer consumo entre 0 e 10 o consumidor paga a mesma quantia de R$ 7,00. 

consumo = int(input('Informe o consumo em M³: \n'))

if consumo <= 10:
    conta = 7
elif consumo >= 11 and consumo <= 30:
    conta = (consumo - 10)* 1 + 7
elif consumo >= 31 and consumo <=100:
    conta = (consumo - 30) * 2 + 27
else:
    conta = (consumo - 100) * 5 + 167

print(f'Valor da conta = {conta}')