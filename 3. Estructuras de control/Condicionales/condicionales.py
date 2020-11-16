condicion = True

if condicion:
	print('Se cumple la condición')
else:
	print('No se cumple la condición')

numero1 = 1
numero2 = 5
suma = numero1 + numero2
if suma == 9:
	print('Se cumple la condición')
else:
	numero1 = input('Ingrese el número1: ')
	numero2 = input('Ingrese el número2: ')
	suma = int(numero1) + int(numero2)
	if suma == 9:
		print('¡Lo lograste!')
	else:
		print('No se cumple la condición')


numero_ingresado = input('Ingrese un número')
if numero_ingresado == '1':
	print('Ingresaste el número 1')
else:
	if numero_ingresado == '2':
		print('Ingresaste el número 2')
	else:
		if numero_ingresado == '3':
			print('Ingresaste el número 3')
		else:
			print('No ingresaste los números esperados')


numero_ingresado = input('Ingrese un número')
if numero_ingresado == '1':
	print('Ingresaste el número 1')
elif numero_ingresado == '2':
		print('Ingresaste el número 2')
elif numero_ingresado == '3':
	print('Ingresaste el número 3')
else:
	print('No ingresaste los números esperados')



if numero_ingresado == '1' or numero_ingresado == '2' or numero_ingresado == '3':
	print('Ingresaste el número correcto')
else:
	print('No ingresaste los números esperados')



