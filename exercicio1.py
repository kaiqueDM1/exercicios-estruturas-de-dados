#Crie uma lista que simule a contagem regressiva de um foguete sendo enviado para fora da Terra.
#Após isso responda, é uma pilha ou uma fila;

lista = []
for i in range(11):
    lista.append(i)
lista.reverse()
print('Contagem regressiva para o lançamento')
for i in lista:
    print(i)