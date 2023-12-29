import json

def Tam(raza):
    
    if raza == "Enano":
        return "Mediano"
    elif raza == "Elfo":
        return "Mediano"
    elif raza == "Gnomo":
        return "Pequeño"
    elif raza == "Mediano":
        return "Pequeño"
    elif raza == "Humano":
        return "Mediano"
    elif raza == "Semielfo":
        return "Mediano"
    elif raza == "Semiorcos":
        return "Mediano"
    elif raza == "Tiefling":
        return "Mediano"
    else:
        return "Opción no válida"

def Atrib(raza, atri):
    
    if raza == "Enano":
        if atri == "str":
            return 0
        elif atri == "des":
            return 0
        elif atri == "con":
            return 2
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 2
        elif atri == "car":
            return -2
        
    elif raza == "Elfo":
        if atri == "str":
            return 2
        elif atri == "des":
            return 2
        elif atri == "con":
            return -2
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 0      
        
    elif raza == "Gnomo":
        if atri == "str":
            return -2
        elif atri == "des":
            return 0
        elif atri == "con":
            return 2
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 2
        
    elif raza == "Mediano":
        if atri == "str":
            return -2
        elif atri == "des":
            return 2
        elif atri == "con":
            return 0
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 2 
        
    elif raza == "Humano":
        if atri == "str":
            return 0
        elif atri == "des":
            return 0
        elif atri == "con":
            return 0
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 0 
        
    elif raza == "Semielfo":
        if atri == "str":
            return 0
        elif atri == "des":
            return 0
        elif atri == "con":
            return 0
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 0 
        
    elif raza == "Semiorcos":
        if atri == "str":
            return 0
        elif atri == "des":
            return 0
        elif atri == "con":
            return 0
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 0 
        
    elif raza == "Tiefling":
        if atri == "str":
            return 0
        elif atri == "des":
            return 0
        elif atri == "con":
            return 0
        elif atri == "int":
            return 0
        elif atri == "sab":
            return 0
        elif atri == "car":
            return 0 
    else:
        return "Opción no válida"

# Crear un diccionario vacío para almacenar los datos
personaje = {
    "Caracteristicas": {},
    "Nivel": {},
    "Idiomas": {}
}

personaje["Caracteristicas"]["nombre"] = input("Nombre del personaje: ")
personaje["Caracteristicas"]["clase"] = input("Clase: ")
personaje["Caracteristicas"]["alineamiento"] = input("Alineamiento: ")
personaje["Caracteristicas"]["hogar"] = input("Hogar: ")
personaje["Caracteristicas"]["raza"] = input("Raza: ")
personaje["Caracteristicas"]["deidad"] = input("Deidad: ")
personaje["Caracteristicas"]["tamanio"] = Tam(personaje["Caracteristicas"]["raza"])
#personaje["Caracteristicas"]["tamanio"] = input("Tamaño: ")
personaje["Caracteristicas"]["sexo"] = input("Sexo: ")
personaje["Caracteristicas"]["edad"] = input("Edad: ")
personaje["Caracteristicas"]["altura"] = input("Altura: ")
personaje["Caracteristicas"]["peso"] = input("Peso: ")
personaje["Caracteristicas"]["cabello"] = input("Color de cabello: ")
personaje["Caracteristicas"]["ojos"] = input("Color de ojos: ")

personaje["Nivel"]["nvl"] = int(input("Nivel: "))
personaje["Nivel"]["experiencia"] = int(input("Experiencia: "))

personaje["Idiomas"]["1"] = "comun"
num_idiomas = int(input("Número de idiomas que habla: "))
for i in range(1, num_idiomas + 1):
    idioma = input(f"Idioma {i}: ")
    personaje["Idiomas"][str(i+1)] = idioma

print ("Nombre de personaje: " + personaje["Caracteristicas"]["nombre"])

print (personaje)



"""
Nombre del personaje: test
Clase: bardo
Alineamiento: bueno 
Hogar: Casa
Raza: Medio
Deidad: Alguno
Tamaño: pequeño
Sexo: Mujer
Edad: 21
Altura: 1:10m
Peso: 20kg
Color de cabello: negro
Color de ojos: azul
Nivel: 1
Experiencia: 0
Puntos de Fuerza (str): 10
Puntos de Destreza (des): 8 
Puntos de Constitución (con): 16
Puntos de Inteligencia (int): 15
Puntos de Sabiduría (sab): 16
Puntos de Carisma (car): 10

"""