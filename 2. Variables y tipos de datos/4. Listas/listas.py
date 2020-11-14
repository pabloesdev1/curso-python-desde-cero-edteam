mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
print(mi_lista[1])
mi_lista[1] = 0

lista_estudiantes = ['Pablo', 'José', 'Juan', 'Luis']
print(lista_estudiantes[-1])
print(lista_estudiantes[1:3])
print(lista_estudiantes[0:3])
print(lista_estudiantes[:3])
print(lista_estudiantes[1:-1])
print(lista_estudiantes[1:])

lista_combinada = ['Hola', 0, 12.3, True, 'Bienvenido']
print(lista_combinada)

nueva_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nueva_lista)


nueva_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], lista_combinada]
print(nueva_lista)

lista_combinada.append('Nuevo dato')
lista_combinada.insert(0, 'Dato 1')
print(lista_combinada)

lista_combinada.pop()
print(lista_combinada)

lista_combinada.remove('Hola')
print(lista_combinada)

print(len(lista_combinada))

print(lista_combinada.count('Hola'))

print(lista_combinada.index('Bienvenido'))