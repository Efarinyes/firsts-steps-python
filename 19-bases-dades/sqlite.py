# Importem mòdul de base de dades
import sqlite3

# Conexió a la bade de dades

conexio = sqlite3.connect('proves.db')

# Crear Cursor
cursor = conexio.cursor()

# Crear taula
cursor.execute("""
CREATE TABLE IF NOT EXISTS productes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titol VARCHAR(255), 
    descripcio TEXT,
    preu int(255)
)
""")

# Guardar els cambis
conexio.commit()

#Insertar dades a la BD
# cursor.execute("INSERT INTO productes VALUES( NULL, 'Cinquè producte', 'Aqui tenim el meravellòs producte 5', 4789)")
# conexio.commit()

# Borrar registres de la BD
cursor.execute('DELETE FROM productes')
conexio.commit()

# Insertar multiples registres a la BD
productes = [
    ( "Primer Producte", "Aqui tenim el meravellòs producte 1", 456),
    ( "Segon Producte", "Aqui tenim el meravellòs producte 2", 987),
    ( "Tercer Producte", "Aqui tenim el meravellòs producte 3", 990)
]

cursor.executemany("INSERT INTO productes VALUES (NULL,?,?,?)", productes )
conexio.commit()

# Modificar registre
cursor.execute('UPDATE productes SET preu = 1100 WHERE preu = 990')
conexio.commit()
 
# Recuperar dades de la BD
cursor.execute("SELECT * FROM productes WHERE preu >= 500")
productes = cursor.fetchall()

for producte in productes:
    print('ID ', producte[0])
    print("Titol: ", producte[1])
    print("Descripcio: ", producte[2])
    print("Preu: ", producte[3])
    print('\n')


cursor.execute("SELECT titol FROM productes")
producte = cursor.fetchone()
print('El primer producte es: ', producte )
# Tanquem la conexió
conexio.close()
