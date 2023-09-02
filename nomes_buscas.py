
nomes = ['kaique','pablo','mario','joao','oscar','cezar','vericimo','lucas','andre','arthur','carlos','jonas','daniel','andrei',
         'rhyan','julio','marcos','henrique','joilson','paulin']
nomes.sort()


item_buscar = 'vericimo'
posicao_encontrado = -1
maior_menor = -1 #inicio, 0 menor , 1 maior
i = 1
adicao_impar = 0 # não andou, 1 ja andou
tamanho_divisor = 0

while posicao_encontrado == -1:

    if (tamanho_divisor == 1 and adicao_impar == 1):
        break

    tamanho_divisor = round(len(nomes)/ (2**i))
    if len(nomes)/(2**i) < 1:
        tamanho_divisor = 1
        adicao_impar = 1

    if maior_menor == -1:
        tamanho = tamanho_divisor

    elif maior_menor == 0:
        tamanho = tamanho - tamanho_divisor
    
    else:
        tamanho = tamanho + tamanho_divisor

    if nomes[tamanho] == item_buscar:
        posicao_encontrado = tamanho

    elif nomes[tamanho] > item_buscar:
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


item_buscar = 'vericimo'
posicao_encontrado = -1

for i in range(len(nomes)):
    if nomes[i] == item_buscar:
        posicao_encontrado = i
        break

if posicao_encontrado == -1:
    print('Item não Encontrado') 
else:
    print('Item encontrado na posição: ', posicao_encontrado)

print('foram feitas', i, 'buscar na lista')