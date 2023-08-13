#Crie uma tupla com os alunos da sala (busquem os nomes lá no AVA) depois faça a chamada normal em fila;

tuplaChamada = ('ALEXSANDRA OLIVIEIRA PACHECO',
'BRUNO ROSSO DA ROCHA',
'BRUNO SEZAR MARCELINO AIOLFI',
'CARLOS HENRIQUE GENUINO ALESSIO',
'DANIEL FREITAS',
'GABRIEL CUSTODIO BOELTER',
'GABRIEL MILANO ALVES',
'GEOVANE VIEIRA DE SOUZA',
'JOÃO AUGUSTO PUPO FAGUNDES',
'JOÃO VITOR WIRTH UESSLER',
'KAIQUE DEMETRIO')

for i in tuplaChamada:
    chamada = str(input(f'{i} esta presente? s/n: '))
    chamada.lower
    if chamada == 's':
        print(f'{i}, veio para aula')
    else:
        print(f'{i}, nao veio')