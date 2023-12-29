import json

# Crear un diccionario vacío para almacenar los datos
personaje = {
    "Caracteristicas": {},
    "Nivel": {},
    "PuntosCaracter": {},
    "Idiomas": {},
    "Habilidades": {},
    "Dote": {}
}

# Solicitar al usuario que ingrese los datos
personaje["Caracteristicas"]["nombre"] = input("Nombre del personaje: ")
personaje["Caracteristicas"]["clase"] = input("Clase: ")
personaje["Caracteristicas"]["alineamiento"] = input("Alineamiento: ")
personaje["Caracteristicas"]["hogar"] = input("Hogar: ")
personaje["Caracteristicas"]["raza"] = input("Raza: ")
personaje["Caracteristicas"]["deidad"] = input("Deidad: ")
personaje["Caracteristicas"]["tamanio"] = input("Tamaño: ")
#personaje["Caracteristicas"]["tamanio"] = Tam(personaje["Caracteristicas"]["raza"])
personaje["Caracteristicas"]["sexo"] = input("Sexo: ")
personaje["Caracteristicas"]["edad"] = input("Edad: ")
personaje["Caracteristicas"]["altura"] = input("Altura: ")
personaje["Caracteristicas"]["peso"] = input("Peso: ")
personaje["Caracteristicas"]["cabello"] = input("Color de cabello: ")
personaje["Caracteristicas"]["ojos"] = input("Color de ojos: ")
# NIVEL
personaje["Nivel"]["nvl"] = int(input("Nivel: "))
#personaje["Nivel"]["experiencia"] = int(input("Experiencia: "))
personaje["Nivel"]["experiencia"] = int(0)

#  Puntos de Caracter
personaje["PuntosCaracter"]["str"] = int(input("Puntos de Fuerza (str): "))
personaje["PuntosCaracter"]["des"] = int(input("Puntos de Destreza (des): "))
personaje["PuntosCaracter"]["con"] = int(input("Puntos de Constitución (con): "))
personaje["PuntosCaracter"]["int"] = int(input("Puntos de Inteligencia (int): "))
personaje["PuntosCaracter"]["sab"] = int(input("Puntos de Sabiduría (sab): "))
personaje["PuntosCaracter"]["car"] = int(input("Puntos de Carisma (car): "))
#  IDIOMA
personaje["Idiomas"]["1"] = "comun"
num_idiomas = int(input("Número de idiomas que habla: "))
for i in range(1, num_idiomas + 1):
    idioma = input(f"Idioma {i}: ")
    personaje["Idiomas"][str(i)] = idioma

# Solicitar habilidades
print("Ingresa el nivel de habilidad para cada habilidad (0-9):")
habilidades = [
    "Acrobacias", "Artesania", "Averiguarintenciones", "Conocimientodeconjuros",
    "Curar", "Disfrazarse", "Diplomacia", "Enganar", "Escapismo", "Interpretar",
    "Intimidar", "Inutilizarmecanismo", "Juegodemanos", "Linguistica", "Montar",
    "Nadar", "Percepcion", "Profesion", "Saber_geografia", "Saber_losPlanos",
    "Saber_ingenieria", "Saber_arcano", "Saber_nobleza", "Saber_historia",
    "Saber_Naturaleza", "Saber_dungeons", "Saber_religion", "Sigilo", "Supervivencia",
    "Tasacion", "Tratoconanimales", "Trepar", "Usarobjetomogico", "Volar"
]

for habilidad in habilidades:
    nivel = int(input(f"Nivel de {habilidad}: "))
    personaje["Habilidades"][habilidad] = nivel

# Solicitar dotes
print("Ingresa las dotes del personaje:")
while True:
    dote = input("Dote (o deja vacío para finalizar): ")
    if not dote:
        break
    descripcion = input(f"Descripción de la dote '{dote}': ")
    personaje["Dote"][dote] = descripcion

# Guardar los datos en un archivo JSON
with open(personaje["Caracteristicas"]["nombre"] + "soul.json", "w") as json_file:
    json.dump(personaje, json_file, indent=4)

print("Se ha creado el archivo '"+ personaje["Caracteristicas"]["nombre"] + "soul.json' con los datos del personaje.")



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
       