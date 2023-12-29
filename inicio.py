import Index as pl
import json

soul = "Personajes/soulPru1.json" 

Alma = open(soul, "r")

Atributos = json.load(Alma)

equipos = [nombre for nombre, equipado in Atributos['ObjEq'].items() if equipado]

print(equipos)

class inicio:
    
    Interfaz = pl.Interfaz
    Interfaz
    
