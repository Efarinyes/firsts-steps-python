import usuaris.conexio as conexio

connect = conexio.conectar()
databse = connect[0]
cursor = connect[1]

class Todo:

    def __init__(self, usuari_id, titol = "", contingut = ""):

        self.usuari_id = usuari_id
        self.titol = titol
        self.contingut = contingut

    def guardar(self):
        sql = 'INSERT INTO todos VALUE(null, %s, %s, %s, NOW())'
        todo = ( self.usuari_id, self.titol, self.contingut)

        cursor.execute( sql, todo )
        databse.commit()

        return [ cursor.rowcount, self ]

    def llistar(self):
        sql = f'SELECT * FROM todos WHERE usuari_id = {self.usuari_id}'
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self):
        sql = f'DELETE FROM notas WHERE usuari_id = { self.usuari_id } AND titol LIKE "%{self.titol}%"'

        cursor.execute(sql)
        databse.commit()

        return [cursor.rowcount, self]
