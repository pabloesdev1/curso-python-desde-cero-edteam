class Usuario:
	
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def registrar(self):
		print(f'El usuario {self.nombre} ha sido registrado')

	def __str__(self):
		return f'La persona se llama {self.nombre} y su edad es {self.edad}'



class Empleado():
	
	def __init__(self, area_trabajo):
		self.area_trabajo = area_trabajo

	def generar_reporte(self):
		print(f'Generando reporte del empleado del área de {self.area_trabajo}')



class Cliente(Usuario):
	
	def __init__(self, nombre, edad, numero_compras):
		super().__init__(nombre, edad)
		self.numero_compras = numero_compras

	def ver_compras(self):
		print(f'El número de compras del cliente {self.nombre} es {self.numero_compras}')



class Vendedor(Usuario, Empleado):

	def __init__(self, nombre, edad, area_trabajo, numero_ventas):
		Usuario.__init__(self, nombre, edad)
		Empleado.__init__(self, area_trabajo)
		self.numero_ventas = numero_ventas

	def ver_ventas(self):
		print(f'El número de ventas del vendedor {self.nombre} es {self.numero_ventas}')

vendedor = Vendedor('Luis', 32, 'ventas', 200)
vendedor.generar_reporte()

