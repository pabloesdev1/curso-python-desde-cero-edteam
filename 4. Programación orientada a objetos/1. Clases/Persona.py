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
