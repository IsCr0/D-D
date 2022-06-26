#import HojaPersonaje
import json

"""
soul = ''
Opc = int(input(
    
    Personajes: 
        1) Ioc
        2) PGenerico1
    Elige la Opcion 
    ))


if Opc == 1: soul = "Personajes/soulPru1.json"           
if Opc == 2: soul = "Personajes/soulPru3.json"
"""


#print(data["Dote"]["Soltura con un arma"])

#Agregar Dotte
#data["Dote"].update({'Hendedura' : 'Haz un ataque adicional si el primero impacta'})
#Eliminar Dote
#data["Dote"].pop('Hendedura')

#f.close

#data["PuntosCaracter"]["str"] = 20
#while True:
soul = "Personajes/soul.json"

f = open(soul,"r")

data = json.load(f)

print("""
        Dime, ¿qué quieres hacer?
        
        1) Subir de Nivel
        2) Agregar Dote
        3) Subir Habilidad
        4) Subir PuntosCaracter
        5) Agregar Idioma
        6) Eliminar Dote??
        7) Salir
        """)

opcion = int(input("Elige una opcion: "))

if opcion == 1:
        
        nvlA = int(data["Nivel"]["nvl"])
        #nvl = int(input("Introduce tu nuevo nivel: "))
        print("Nivel Actual: ",nvlA)
        
        #n1 = int(input("Introduce tu primer número: ") )
        data["Nivel"]["nvl"] = nvlA+1
        
        print("Nuevo Nivel: ", data["Nivel"]["nvl"])
            
if opcion == 2:
        Dote = input("Introduce Dote: ")
        DoteDes = input("Introduce Descripcion del Dote: ")
        data["Dote"].update({Dote : DoteDes})
            
if opcion == 3:
        print("Luego veo lol xD")
        punhab = input("Introduce el nombre de la habilidad se va a subir: ")
        
        print(punhab)
        punhabn = int(input("Introduce tu nuevo nivel de habilidad: "))
        data["Habilidades"][punhab] = punhabn

if opcion == 4:
        puncar = input("""Introduce que caracter se va a subir:
                        str, des ,con ,int ,sab ,car
                        """)
        print(puncar)
        nvlpuncar = int(input("Introduce tu nuevo nivel de carcter: "))
        data["PuntosCaracter"][puncar] = nvlpuncar

if opcion == 5:
        Idioma = input("Introduce el nuevo Idioma: ")
        #DoteDes = input("Introduce Descripcion del Dote: ")
        numerodeIdioma=2
        data["Idiomas"].update({2 : Idioma})
        
if opcion == 6:
        DoteE = input("Introduce Dote: ")
        #data["Dote"].pop(DoteE)
            
if opcion == 7:
        print("Bye")
        #break
    
f.close  

with open(soul, 'w') as outfile:
    json.dump(data, outfile)


    
    
"""
Pagina donde viene el while para que siempre aparesca la pantalla
https://estadisticamente.com/programar-calculadora-python/1

#print(data["Ataque poderoso"])

crece = open('Alma.txt','w')

crece.write(line.replace('16','18'))

crece.close()
"""