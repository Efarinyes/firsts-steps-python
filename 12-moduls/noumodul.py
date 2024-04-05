def saludar(nom):
    return f'Hola {nom}, com estas?'

def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divisio = num1 / num2

    cadena = ''
    if basicas != False:
        cadena += 'Suma: ' + str(suma)
        cadena += '\n'
        cadena += 'Resta ' + str(resta)
        cadena += '\n'
    else:
        cadena += 'Multiplicació: ' + str(multi)
        cadena += '\n'
        cadena += 'Divisió ' + str(divisio)

    return cadena