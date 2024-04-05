# Comprobar si una variable esta buida. Si ho està, omplir-la de text en minuscules y mostrarla en majuscules

text = ""

if len(text.strip()) <= 0:
    
    text = 'hola mon mundial'
    
    print(text.upper())
    
else:
    print(f'{ text } es el contingut')

