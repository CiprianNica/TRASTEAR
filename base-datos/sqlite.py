import sqlite3
# conexion
conexion = sqlite3.connect('pruebas.db')
#crear cursor
cursor = conexion.cursor()
# crear tabla
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo varchar(255),
        description text,
        precio int(255));
    """)
# insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'descripcion prim producto', 500)")
cursor.execute("INSERT INTO productos VALUES (null, 'segundo producto', 'descripcion segundo producto', 300)")
cursor.execute("INSERT INTO productos VALUES (null, 'tercer producto', 'descripcion tercer producto', 2000)")
cursor.execute("INSERT INTO productos VALUES (null, 'cuarto producto', 'descripcion cuarto producto', 400)")

# guardar cambios
conexion.commit()
# listar datos
cursor.execute("SELECT * FROM productos WHERE precio = 500")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
# borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()
#cerrar la conexion
conexion.close()