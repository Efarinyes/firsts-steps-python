# Montar un script que contingui 4 tipus de dades i que mostri quin és el seu tipus (llista enter, string o boleà)

def traduirTipus(tipus):
    resposta = None
    if tipus == list:
        resposta = 'LLISTA'
    elif tipus == str:
        resposta = 'CADENA DE TEXT'
    elif tipus == bool:
        resposta ='BOOLEÂ'
    elif tipus == int:
        resposta = 'NÜMERO' 
    return resposta

def comprobarTipat(item, tipus):
    test = isinstance(item, tipus)
    resultat = ''
    if test:
       resultat = f"Aquest item es de tipus {traduirTipus(tipus)}"
    else:
        resultat = None
    return resultat
    
llista = ['hola', 'mon', 'mundial', 66]
titol = 'curs de python'
num = 89
verdader = True

print(comprobarTipat(num, int))
print(comprobarTipat(titol, str))
print(comprobarTipat(verdader, bool))
print(comprobarTipat(num, int))