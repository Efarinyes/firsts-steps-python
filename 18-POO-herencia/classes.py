
# Herencia: Compartir mètodes i atributs d'una classe Pare a una filla que hereda els mètodes i els atributs

class Persona:
    # nom
    # cognoms
    # edat
    # estatura

    # Getters
    def getNom(self):
        return self.nom
    
    def getCognoms(self):
        return self.cognoms
    
    def getEdat(self):
        return self.edat
    
    def getEstatura(self):
        return self.estatura
    
    # Setters
    def setNom(self, nom):
        self.nom = nom
    
    def setCognoms(self, cognoms):
        self.cognoms = cognoms
    
    def setEdat(self, edat):
        self.edat = edat
    
    def setEstatura(self, estatura):
        self.estatura = estatura

    # accions genèriques
        
    def parlar(self):
        return 'Jo parlo'
    def caminar(self):
        return 'Estic caminant'
    def dormir(self):
        return 'Estic sommiant'
    
class Informatic(Persona):

    def __init__(self):
        self.llenguatges = 'Python, CSS, javaScript, Perl, PHP, C+'
        self.experiencia = 3

    def getLlenguatges(self):
        return self.llenguatges
    
    def aprendre(self, llenguatges):
        self.llenguatges = llenguatges
        return self.llenguatges
    
    def programar(self):
        return 'Faig un script amb Perl'
    
    def arreglar(self):
        return 'Estic arreglant el Mac'
    
class TecnicInformatic(Informatic):
    
    def __init__(self):
        super().__init__()
        self.auditarXarxes = 'Expert'
        self.experienciaXarxes = 5

        

       

    
    
