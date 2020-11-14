conjunto = {1, 2, 3}
conjunto.add('p')
conjunto.add('A')
conjunto.add('Elemento nuevo')
print(conjunto)

existe = 'p' in conjunto
print(existe)

lista_convertida = list(conjunto)
lista_convertida.append(2)
conjunto.add(2)
print(lista_convertida)
print(conjunto)

texto = 'Se convertirá a conjunto'
print(set(texto))

conjunto.discard(1)
conjunto.clear()

print(conjunto)
