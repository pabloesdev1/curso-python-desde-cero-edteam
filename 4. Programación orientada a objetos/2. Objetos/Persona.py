class Persona:
	
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def caminar(self):
		print(f'{self.nombre} está caminando')

	def correr(self):
		print(f'{self.nombre} está corriendo')

	def __str__(self):
		return f'La persona se llama {self.nombre} y su edad es {self.edad}'


persona = Persona('Pablo', 25)
print(persona)
persona.caminar()
persona.correr()
print(persona.nombre)
print(persona.edad)

persona1 = Persona('Pablo', 25)
persona2 = Persona('Nombre2', 26)
persona3 = Persona('Nombre3', 24)

persona1.caminar()
persona2.correr()
persona3.caminar()
