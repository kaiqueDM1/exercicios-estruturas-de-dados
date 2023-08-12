#Crie um dicionário que armazene as três notas e a sua média, depois crie um método para calcular a média dessas notas, ou seja, a média deve ser calculada após a inserção das notas, em momentos diferentes;

dicioNota = {'nota': [9,4,9]}

soma = sum(dicioNota['nota'])
media = soma / 3
dicioNota.update({'media': media})
print(dicioNota)