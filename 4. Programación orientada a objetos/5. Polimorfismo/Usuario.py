class Usuario:
	
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def registrar(self):
		print(f'El usuario {self.nombre} ha sido registrado')

	def __str__(self):
		return f'La persona se llama {self.nombre} y su edad es {self.edad}'

	def consultar_tipo(self):
		print('Sin especificar')


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

	def consultar_tipo(self):
		print('El tipo de usuario es: cliente')



class Vendedor(Usuario, Empleado):

	def __init__(self, nombre, edad, area_trabajo, numero_ventas):
		Usuario.__init__(self, nombre, edad)
		Empleado.__init__(self, area_trabajo)
		self.numero_ventas = numero_ventas

	def ver_ventas(self):
		print(f'El número de ventas del vendedor {self.nombre} es {self.numero_ventas}')

	def consultar_tipo(self):
		print('El tipo de usuario es: vendedor')


usuario = Usuario('Nombre..', 21)
cliente = Cliente('Nombre..', 21, 100)
vendedor = Vendedor('Nombre..', 21, 'ventas', 200)

usuario.consultar_tipo()
cliente.consultar_tipo()
vendedor.consultar_tipo()


def mostrar_tipo(objeto):
	objeto.consultar_tipo()

mostrar_tipo(usuario)
mostrar_tipo(cliente)
mostrar_tipo(vendedor)


for objeto in (usuario, cliente, vendedor):
	objeto.consultar_tipo()