
import datetime
import hashlib
import usuaris.conexio as conexio

conecta = conexio.conectar()
database = conecta[0]
cursor = conecta[1]


class Usuari:

    def __init__(self, nom, cognoms, email, password ):
        self.nom = nom
        self.cognoms = cognoms
        self.email = email
        self.password = password

    def registrar(self):
        data = datetime.datetime.now()
        # Encriptem contrassenya
        encript = hashlib.sha256()
        encript.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuaris VALUES(null, %s, %s, %s, %s, %s)"
        usuari = ( self.nom, self.cognoms, self.email, encript.hexdigest(), data )

        try:
            cursor.execute(sql, usuari)
            database.commit()
            result = [ cursor.rowcount, self ]
        except:
            result = [ 0, self ]
        
        return result

        

    def identificar(self):

        sql = 'SELECT * FROM usuaris WHERE email = %s AND password = %s'

        # Encriptem contrassenya
        encript = hashlib.sha256()
        encript.update(self.password.encode('utf8'))
        usuari = (self.email, encript.hexdigest())

        cursor.execute(sql, usuari)
        result = cursor.fetchone()

        return result
