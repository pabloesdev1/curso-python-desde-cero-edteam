import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        print('Se ha conectado a la base de datos correctamente!')
        return conexion
    except Error:
        print('Ha ocurrido un error')


def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT NOT NULL, 
        apellido TEXT NOT NULL)'''
    cursor.execute(sentencia_sql)
    conexion.commit()
    conexion.close()

def insertar(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.execute(sentencia_sql, datos)
    conexion.commit()
    conexion.close()

def insertar_varios(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.executemany(sentencia_sql, datos)
    conexion.commit()
    conexion.close()

def consultar(conexion):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario'
    cursor.execute(sentencia_sql)
    datos = cursor.fetchall()
    conexion.close()
    return datos

def consultar_por_id(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario WHERE id=?'
    cursor.execute(sentencia_sql, (id,))
    datos = cursor.fetchall()
    conexion.close()
    return datos

def actualizar(conexion, id, nombre, apellido):
    cursor = conexion.cursor()
    sentencia_sql = 'UPDATE usuario SET nombre = ?, apellido = ? WHERE id = ?'
    cursor.execute(sentencia_sql, (nombre, apellido, id) )
    conexion.commit()
    conexion.close()

def eliminar(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'DELETE FROM usuario WHERE id = ?'
    cursor.execute(sentencia_sql, (id,))
    conexion.commit()
    conexion.close()


conexion = conectar()
crear_tabla(conexion)


conexion = conectar()
datos = [('Pablo', 'España'), ('Jaime', 'Pérez')]
insertar_varios(conexion, datos)


conexion = conectar()
datos = consultar_por_id(conexion, 4)
if len(datos) > 0:
    print(datos[0][1] + ' ' + datos[0][2])
else:
    print('No se encontró ese usuario')

conexion = conectar()
eliminar(conexion, 3)