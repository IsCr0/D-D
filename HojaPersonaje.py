import ClasesPer
import Equipo
import json
#Hoja de personaje PATHFINDER
"""
REMPLAZAR LINEA ESPECIFICA EN UN TXT, PARA SUBIR DE NIVEL
contenido = file("ARCHIVO.txt").read().splitlines()
contenido.insert(LINEA,TEXTO)
f = file("ARCHIVO.txt", "w")
f.writelines("\n".join(contenido))
"""
Alma = open("soul.json","r")
Atributos = json.load(Alma)

NomPer =  'Ioc'
NIVEL = Atributos["Nivel"]["nvl"]#ALMA
CLASE = ClasesPer.Guerrero.NomClase
ALINEAMIENTO = 'NEUTRAL'
HOGAR   = 'AQUI'
RAZA    = 'HUMANA'
DEIDAD  = 'CAOS'
TAMANIO  = 'MEDIANO'
SEXO    = 'HOMBRE'
EDAD    = '22'
ALTURA  = '1.75'
PESO    = '89'
CABELLO = 'NEGRO'
OJOS    = 'NEGRO'
#BONIFICADOR DE TAMAÑO
# if TAMANIO = 'MEDIANO' : 0
# if TAMANIO = 'GRANDE' : -1
MODTAM = 0
#PUNTOS DE GOLPE
PG = 15
#Puntos de caracter ALMA

FUE = Atributos["PuntosCaracter"]["str"]
DES = Atributos["PuntosCaracter"]["des"]
CON = Atributos["PuntosCaracter"]["con"]
INT = Atributos["PuntosCaracter"]["int"]
SAB = Atributos["PuntosCaracter"]["sab"]
CAR = Atributos["PuntosCaracter"]["car"]
#Modificador de caracter

MODFUE = int((FUE-10)/2)
MODDES = int((DES-10)/2)
MODCON = int((CON-10)/2)
MODINT = int((INT-10)/2)
MODSAB = int((SAB-10)/2)
MODCAR = int((CAR-10)/2)
"""
k = 0
for val in range(10,45,2):
    
    #print(k)
    if int(FUE) >= int(val):
    #if 10 >= int(val):        
        MODFUE = int(k)
        
    if int(DES) >= int(val):
        MODDES = int(k)
        
    if int(CON) >= int(val):
        MODCON = int(k)
        
    if int(INT) >= int(val):
        MODINT = int(k)
        
    if int(SAB) >= int(val):
        MODSAB = int(k)
        
    if int(CAR) >= int(val):
        MODCAR = int(k)
        
    k=k+1    
        
    #k++
""" 


#print(Alma.read())
#ARMADURA NATURAL 
# if RAZA = 'HUMANA' : 0
# if RAZA = 'ELFO' : 0
ARMADURANATURAL = 0
#Modificador de Armadura
#EJEMPLO
MODVARIOS = 0
#'Escudo ligero de acero'
BONIFESCUDO = Equipo.Puesto.Escudo(1)
#'Camisote de mallas'
BONIFARMADURA = Equipo.Puesto.Armadura(1)
#EJEMPLO
CA = 10+BONIFARMADURA+BONIFESCUDO+MODDES+MODTAM+ARMADURANATURAL+MODVARIOS
#print(CA)
#TOQUE
TOQUE = 5
#DESPREVENIDO
DESPREVENIDO = 5
#INICIATIVA
INICIATIVA = MODDES+MODVARIOS
#TIRO DE SALVACION FORTALEZA
FORTALEZA = MODCON#+SALVBASE+MODMAGICO+MODVARIO+MODTEMPORAL
#TIRO DE SALVACION REFLEJOS
REFLEJOS = MODDES#+SALVBASE+MODMAGICO+MODVARIO+MODTEMPORAL
#TIRO DE SALVACION VOLUNTAD
VOLUNTAD = MODSAB#+SALVBASE+MODMAGICO+MODVARIO+MODTEMPORAL
#ATAQUE BASE
ATAQUEBASE = (ClasesPer.Guerrero.Atq(NIVEL))
#RESISTENCIA A CONJUROS
RESCONJUROS = 2
#BONO DE MANIOBRAS DE COMBATE
BMC = ATAQUEBASE+MODFUE+MODTAM
#Defensa contra Maniobras de Combate
DMC = 10 +ATAQUEBASE+MODFUE+MODDES+MODTAM
#VELOCIDAD: 30 pies (9 m).
# if RAZA = 'HUMANA' : 30
VEL = 30 
#NADAR

#TREPARcac

#CAVAR

#print (ClasesPer.Guerrero.Fortaleza(NIVEL))

#Idioma
Idiomas = Atributos["Idiomas"]
#print(Idiomas)
#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------ARMAS y ARMADURAS----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#ARM
NombreArm   = Equipo.Puesto.Armas(0)+" - Dado: "+Equipo.Puesto.Armas(1)
#ARMCOM = Equipo.Puesto.Armas

#ESCUDO
NOMESCUDO   = Equipo.Puesto.Escudo(0)

#ARMADURA
NOMARMADURA = Equipo.Puesto.Armadura(0)

#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------ARMAS y ARMADURAS----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------HABILIDADES----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

MODVARIOSH = 0
RANGOS = ClasesPer.Guerrero.ModHabilidad

Acrobacias=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Acrobacias"]
Artesania=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Artesania"]
Averiguarintenciones=((MODSAB+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Averiguarintenciones"]
Conocimientodeconjuros=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Conocimientodeconjuros"]
Curar=((MODSAB+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Curar"]
Disfrazarse=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Disfrazarse"]
Diplomacia=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Diplomacia"]
Engañar=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Enganar"]
Escapismo=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Escapismo"]
Interpretar=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Interpretar"]
Intimidar=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Intimidar"]
Inutilizarmecanismo=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Inutilizarmecanismo"]
Juegodemanos=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Juegodemanos"]
Lingüística=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Linguistica"]
Montar=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Montar"]
Nadar=((MODFUE+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Nadar"]
Percepción=((MODSAB+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Percepcion"]
Profesión=((MODSAB+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Profesion"]
Saber_geografía=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_geografia"]
Saber_losPlanos=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_losPlanos"]
Saber_ingeniería=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_ingenieria"]
Saber_arcano=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_arcano"]
Saber_nobleza=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_nobleza"]
Saber_historia=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_historia"]
Saber_Naturaleza=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_Naturaleza"]
Saber_dungeons=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_dungeons"]
Saber_religión=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Saber_religion"]
Sigilo=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Sigilo"]
Supervivencia=((MODSAB+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Supervivencia"]
Tasación=((MODINT+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Tasacion"]
Tratoconanimales=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Tratoconanimales"]
Trepar=((MODFUE+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Trepar"]
Usarobjetomágico=((MODCAR+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Usarobjetomogico"]
Volar=((MODDES+RANGOS+MODVARIOSH)*0)+Atributos["Habilidades"]["Volar"]

#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------HABILIDADES----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------DOTES----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

DoteNombre = 'Soltura con un arma'
Info       = 'Bonif. +1 a las tiradas de ataque con un arma determinada'

"""
Dotes = [['Soltura con un arma','Bonif. +1 a las tiradas de ataque con un arma determinada'],
         ['Ataque poderoso','Cambias bonificador al ataque cuerpo a cuerpo por daño'],
         ['Reflejos de combate','Haz ataques de oportunidad adicionales']]
"""
Dotes = Atributos["Dote"]

NDo = len(Dotes)

#print(Dotes)
Alma.close()


#print (Dotes[0])



#REFEERNCIAS
#Defensa contra Maniobras de Combate (DMC)
#https://www.rolroyce.com/rol/DDP/CombatePF.php#:~:text=especial%20por%20tama%C3%B1o-,El%20modificador%20especial%20por%20tama%C3%B1o%20de%20una%20criatura%20es%20el,personaje%20cuando%20resiste%20maniobras%20concretas.