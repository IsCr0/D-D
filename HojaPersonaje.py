
import ClasesPer
import Equipo
#Hoja de personaje PATHFINDER
"""
REMPLAZAR LINEA ESPECIFICA EN UN TXT, PARA SUBIR DE NIVEL
contenido = file("ARCHIVO.txt").read().splitlines()
contenido.insert(LINEA,TEXTO)
f = file("ARCHIVO.txt", "w")
f.writelines("\n".join(contenido))
"""
NomPer =  'Ioc'
NIVEL = 1#ALMA
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

Alma = open('Alma.txt','r')
Atributos = Alma.readlines()
FUE = Atributos[0]
DES = Atributos[1]
CON = Atributos[2]
INT = Atributos[3]
SAB = Atributos[4]
CAR = Atributos[5]
#Modificador de caracter
""" 
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
 
print(Alma.read())
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
#VELOCIDAD30 pies (9 m).
# if RAZA = 'HUMANA' : 30
VEL = 30 
#NADAR

#TREPARcac

#CAVAR

#print (ClasesPer.Guerrero.Fortaleza(NIVEL))

#Idioma
Idiomas = Alma.readline()
print(Idiomas)
#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------ARMAS y ARMADURAS----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#ARM
NombreArm   = Equipo.Puesto.Armas(0)
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
"""
Acrobacias					=MODDES+RANGOS+MODVARIOShABILIDAD
Artesanía					=MODINT+RANGOS+MODVARIOShABILIDAD
Averiguar intenciones 		=MODSAB+RANGOS+MODVARIOShABILIDAD
Conocimiento de conjuros*	=MODINT+RANGOS+MODVARIOShABILIDAD
Curar 						=MODSAB+RANGOS+MODVARIOShABILIDAD
Disfrazarse 				=MODCAR+RANGOS+MODVARIOShABILIDAD
Diplomacia 					=MODCAR+RANGOS+MODVARIOShABILIDAD
Engañar 					=MODCAR+RANGOS+MODVARIOShABILIDAD
Escapismo    				=MODDES+RANGOS+MODVARIOShABILIDAD
Interpretar					=MODCAR+RANGOS+MODVARIOShABILIDAD
Intimidar 				    =MODCAR+RANGOS+MODVARIOShABILIDAD
Inutilizar mecanismo* 		=MODDES+RANGOS+MODVARIOShABILIDAD
Juego de manos* 			=MODDES+RANGOS+MODVARIOShABILIDAD
Lingüística* 				=MODINT+RANGOS+MODVARIOShABILIDAD
Montar						=MODDES+RANGOS+MODVARIOShABILIDAD
Nadar						=MODFUE+RANGOS+MODVARIOShABILIDAD
Percepción 					=MODSAB+RANGOS+MODVARIOShABILIDAD
Profesión*					=MODSAB+RANGOS+MODVARIOShABILIDAD
Saber (geografía)*			=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (los Planos)* 		=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (ingeniería)*			=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (arcano)*				=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (nobleza)* 			=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (historia)*			=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (Naturaleza)* 		=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (dungeons)*			=MODINT+RANGOS+MODVARIOShABILIDAD
Saber (religión)*			=MODINT+RANGOS+MODVARIOShABILIDAD
Sigilo						=MODDES+RANGOS+MODVARIOShABILIDAD
Supervivencia				=MODSAB+RANGOS+MODVARIOShABILIDAD
Tasación 					=MODINT+RANGOS+MODVARIOShABILIDAD
Trato con animales* 		=MODCAR+RANGOS+MODVARIOShABILIDAD
Trepar						=MODFUE+RANGOS+MODVARIOShABILIDAD
Usar objeto mágico* 		=MODCAR+RANGOS+MODVARIOShABILIDAD
Volar 						=MODDES+RANGOS+MODVARIOShABILIDAD
"""
Idioas = 'comun'

#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------HABILIDADES----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

MODVARIOSH = 0
RANGOS = ClasesPer.Guerrero.ModHabilidad

Acrobacias=MODDES+RANGOS+MODVARIOSH
Artesanía=MODINT+RANGOS+MODVARIOSH
Averiguarintenciones=MODSAB+RANGOS+MODVARIOSH
Conocimientodeconjuros=MODINT+RANGOS+MODVARIOSH
Curar=MODSAB+RANGOS+MODVARIOSH
Disfrazarse=MODCAR+RANGOS+MODVARIOSH
Diplomacia=MODCAR+RANGOS+MODVARIOSH
Engañar=MODCAR+RANGOS+MODVARIOSH
Escapismo=MODDES+RANGOS+MODVARIOSH
Interpretar=MODCAR+RANGOS+MODVARIOSH
Intimidar=MODCAR+RANGOS+MODVARIOSH
Inutilizarmecanismo=MODDES+RANGOS+MODVARIOSH
Juegodemanos=MODDES+RANGOS+MODVARIOSH
Lingüística=MODINT+RANGOS+MODVARIOSH
Montar=MODDES+RANGOS+MODVARIOSH
Nadar=MODFUE+RANGOS+MODVARIOSH
Percepción=MODSAB+RANGOS+MODVARIOSH
Profesión=MODSAB+RANGOS+MODVARIOSH
Saber_geografía=MODINT+RANGOS+MODVARIOSH
Saber_losPlanos=MODINT+RANGOS+MODVARIOSH
Saber_ingeniería=MODINT+RANGOS+MODVARIOSH
Saber_arcano=MODINT+RANGOS+MODVARIOSH
Saber_nobleza=MODINT+RANGOS+MODVARIOSH
Saber_historia=MODINT+RANGOS+MODVARIOSH
Saber_Naturaleza=MODINT+RANGOS+MODVARIOSH
Saber_dungeons=MODINT+RANGOS+MODVARIOSH
Saber_religión=MODINT+RANGOS+MODVARIOSH
Sigilo=MODDES+RANGOS+MODVARIOSH
Supervivencia=MODSAB+RANGOS+MODVARIOSH
Tasación=MODINT+RANGOS+MODVARIOSH
Tratoconanimales=MODCAR+RANGOS+MODVARIOSH
Trepar=MODFUE+RANGOS+MODVARIOSH
Usarobjetomágico=MODCAR+RANGOS+MODVARIOSH
Volar=MODDES+RANGOS+MODVARIOSH
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
Dotes = Alma.read()

NDo = len(Dotes)

print(Dotes)
Alma.close()


#print (Dotes[0])



#REFEERNCIAS
#Defensa contra Maniobras de Combate (DMC)
#https://www.rolroyce.com/rol/DDP/CombatePF.php#:~:text=especial%20por%20tama%C3%B1o-,El%20modificador%20especial%20por%20tama%C3%B1o%20de%20una%20criatura%20es%20el,personaje%20cuando%20resiste%20maniobras%20concretas.