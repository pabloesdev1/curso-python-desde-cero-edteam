mi_diccionario = {}
print(type(mi_diccionario))

diccionario_traduccion = {'hola' : 'hello', 'rojo' : 'red', 'libro' : 'book'}
print(diccionario_traduccion)
diccionario_traduccion['rojo'] = 'blue'
print(diccionario_traduccion)
del(diccionario_traduccion['libro'])
print(diccionario_traduccion)

estudiante = {
    'Nombre': 'Juan',
    'Apellido': 'Rodriguez',
    'Edad': 23,
    'Curso': 'Python'
}

estudiante1 = {
    'Nombre': 'Juan',
    'Apellido': 'Rodriguez',
    'edad': 23,
    'Cursos': [
        {'nombre_curso':'Python', 'nivel':'básico'}, 
        {'nombre_curso':'JavaScript', 'nivel':'medio'},
        {'nombre_curso':'Php', 'nivel':'avanzado'}
    ]
    }

estudiante2 = {
    'Nombre':'José',
    'Apellido':'Rodriguez',
    'edad':25,
    'Cursos': [
        {'nombre_curso':'Python', 'nivel':'básico'}, 
        {'nombre_curso':'JavaScript', 'nivel':'medio'},
        {'nombre_curso':'Php', 'nivel':'avanzado'}
    ]
    }

estudiantes = []
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
print(estudiantes[1]['Cursos'])
