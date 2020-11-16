class Usuario:
	
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def registrar(self):
		print(f'El usuario {self.nombre} ha sido registrado')

	def __str__(self):
		return f'La persona se llama {self.nombre} y su edad es {self.edad}'

usuario = Usuario('Pablo', 25)
usuario.registrar()


class Cliente(Usuario):
	
	def __init__(self, nombre, edad, numero_compras):
		super().__init__(nombre, edad)
		self.numero_compras = numero_compras

	def ver_compras(self):
		print(f'El número de compras del cliente {self.nombre} es {self.numero_compras}')

cliente = Cliente('Pepe', 30, 100)
cliente.ver_compras()


class Vendedor(Usuario):

	def __init__(self, nombre, edad, numero_ventas):
		super().__init__(nombre, edad)
		self.numero_ventas = numero_ventas

	def ver_ventas(self):
		print(f'El número de ventas del vendedor {self.nombre} es {self.numero_ventas}')

vendedor = Vendedor('Luis', 32, 200)
vendedor.ver_ventas()

