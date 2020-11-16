class Usuario:

    '''def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad'''

    def __init__(self):
        self.__nombre = 'Ana'
        self.__edad = 23

    # getters
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    # setters
    def setNombre(self, nombre):
        if nombre == 'Ana':
            self.__nombre = nombre
        else:
            return 'No puede asignar ese nombre'

    def setEdad(self, edad):
        if edad == 23:
            self.__edad = edad
        else:
            return 'No puede asignar esa edad'

    def __registrar(self):
        print(f'El usuario {self.__nombre} ha sido registrado')

    def __str__(self):
        return f'El usuario se llama {self.__nombre} y su edad es {self.__edad}'

    def consultar_tipo(self):
        self.__registrar()
        print('Sin especificar')


usuario = Usuario()
print(usuario.setNombre('Ana'))
print(usuario.setEdad(23))

print(usuario.getNombre())
print(usuario.getEdad())