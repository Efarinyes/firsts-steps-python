


import mysql.connector

# Connexió a la base de dades

database = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '',
    database = 'curs_python'
)

# Per accedir als metodes per treballar amb la BBDD
cursor = database.cursor(buffered=True)
# Creem la base de dades
cursor.execute('CREATE DATABASE IF NOT EXISTS curs_python')

# LListem totes les bases de dades disponibles
# cursor.execute('SHOW DATABASES')

# for bd in cursor:
#     print(bd)

# Creem taules a la Base de dades
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    model varchar(40) not null,
    preu float(10,2) not null,
    CONSTRAINT pk_vehicles PRIMARY KEY(id)
)

""")


# Insertem un registre
cursor.execute('SHOW TABLES')
for table in cursor:
    print(table)

cursor.execute("INSERT INTO vehicles VALUES(NULL,'SEAT', 'Panda', 35500.99)")
# Insertem registres multiples
cotxes = [
    ('SEAT', 'Ibiza', 4500),
    ('RENAILT', 'Clio', 9000),
    ('CITROEN', 'C3', 6789),
    ('HYUNDAY', 'MODEL 1', 7890.98)
]
cursor.executemany("INSERT INTO vehicles VALUES(null, %s, %s, %s)", cotxes)

# Llegim registres amb condicions
cursor.execute('SELECT * FROM vehicles WHERE marca = "SEAT"') 

data = cursor.fetchall()

for cotxe in data:
     print(cotxe)

# Borrar registres
# cursor.execute("DELETE FROM vehicles WHERE marca = 'CITROEN'")
# cursor.execute("SELECT * FROM vehicles")

# data = cursor.fetchall()

# for cotxe in data:
    # print(cotxe)

# Modificar registres

cursor.execute("SELECT * FROM vehicles")
data = cursor.fetchall()
print('-------------- Registres Originals --------------' )
for cotxe in data:
    print(cotxe)


database.commit()

cursor.execute('UPDATE vehicles SET preu = 5100.75 WHERE model = "Panda"')
cursor.execute("SELECT * FROM vehicles")
data = cursor.fetchall()
print('-------------- Registres Modificats --------------' )
for cotxe in data:
    print(cotxe)

database.commit()
