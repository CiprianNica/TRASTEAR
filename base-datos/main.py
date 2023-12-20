import mysql.connector

# conexion

conexion = mysql.connector.connect(
    host ="127.0.0.1",
    user = "root",
    passwd = "Madrid_2014",
    database = 'master_python'
)
# cursor
cursor = conexion.cursor(buffered=True)

# crear base de datos
cursor.execute('CREATE DATABASE IF NOT EXISTS master_python')
    
# crear tablas
cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehiculos(
                id int(10) auto_increment not null,
                marca varchar(20) not null,
                modelo varchar(20) not null,
                precio float(10, 2) not null,
                CONSTRAINT pk_vehiculo PRIMARY KEY(id)) 
            """)
coches = [
    ('seat', 'ibiza', 4000),
    ('renault', 'clio', 3000),
    ('citroen', 'saxo', 2000),
    ('mercedes', 'c class', 35000)]
#cursor.executemany("INSERT INTO vehiculos(marca, modelo, precio) VALUES(%s, %s, %s)", coches)
conexion.commit()
cursor.execute("SELECT marca FROM vehiculos")
result = cursor.fetchall()
for marca in result:
    print(f"marca: {marca[0]}")