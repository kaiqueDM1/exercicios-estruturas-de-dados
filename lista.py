lista = [1,2,3,10,11,15,22,33]

def pesquisa(item_buscar , lista):
        
    posicao_encontrada = -1
    i = 0

    while posicao_encontrada == -1:

        if len(lista) == i:
            break

        if lista[i] == item_buscar:
            posicao_encontrada = i
        
        i +=1

    if posicao_encontrada == -1:
        print('item nao encontrado!!!')
    else:
        print('item encontrado na posição:', posicao_encontrada)

item = int(input('digite um numero: '))

pesquisa(item, lista)