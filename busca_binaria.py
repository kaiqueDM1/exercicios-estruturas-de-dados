lista = [3,4,8,13,2,10,6,7,32,95,5,0,11,12,34,9,17]
lista.sort

item_buscar = 34
posicao_encontrado = -1
maior_menor = -1 #inicio, 0 menor , 1 maior
i = 1
adicao_impar = 0 # não andou, 1 ja andou
tamanho_divisor = 0

while posicao_encontrado == -1:

    if (tamanho_divisor == 1 and adicao_impar == 1):
        break

    tamanho_divisor = round(len(lista)/ (2**i))
    if len(lista)/(2**i) < 1:
        tamanho_divisor = 1
        adicao_impar = 1

    if maior_menor == -1:
        tamanho = tamanho_divisor

    elif maior_menor == 0:
        tamanho = tamanho - tamanho_divisor
    
    else:
        tamanho = tamanho + tamanho_divisor

    if lista[tamanho] == item_buscar:
        posicao_encontrado = tamanho

    elif lista[tamanho] > item_buscar:
        maior_menor = 0

    else:
        maior_menor = 1

    i += 1

if posicao_encontrado == -1:
    print('item nao encontrado')
    print('foram feitas', i, 'buscas na lista')
else:
    print('item encontrado na posição :', posicao_encontrado)
    print('foram feitas', i, 'buscas na lista')