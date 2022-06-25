from HojaPersonaje import Dotes
import HojaPersonaje as pl

print("======================================================================================================")
print("======================================================================================================")
print("====                                 Guerrero                                                    =====")
print("======================================================================================================")
print("======================================================================================================")
for i in range(1):
    print("==== ")
print("====    Nombre del Personaje: " + pl.NomPer,end='           ')
print("    *****    Arma: ",end='')
print(pl.NombreArm)
print("====    Nivel del Personaje: " + str(pl.NIVEL))
print("====    Alineamiento del Personaje: " + pl.ALINEAMIENTO)
#print("====")
print("====    Puntos de Golpe: " + str(pl.PG))
print("====    CA : "+str(pl.CA)+"       *****    INICIATIVA: "+str(pl.INICIATIVA))
print("====    TOQUE: "+str(pl.TOQUE)+"      *****    DESPREVENIDO: "+str(pl.DESPREVENIDO))
print("====    FORTALEZA: " + str(pl.FORTALEZA)+"  *****    BMC: "+str(pl.BMC))
print("====    REFLEJOS: " + str(pl.REFLEJOS)+"   *****    DMC: "+str(pl.DMC))
print("====    VOLUNTAD: " + str(pl.VOLUNTAD)+"   *****    IDIOMA: "+str(pl.Idiomas))
print("****    Dotes: ")
for i in range(int(pl.NDo)):
    print('****    ',end='') 
    print(pl.Dotes[i])
    
print("****    Habilidades: ")

print("****    Acrobacias = ",end='       ')
print("        Artesanía = ",end='       ')
print("        Averiguarintenciones = ")

print("****    Conocimientodeconjuros = ",end='')
print("   Curar = ",end='        ')
print("        Disfrazarse = ")

print("****    Diplomacia = ",end='       ')
print("        Engañar = ",end='       ')
print("        Escapismo = ")

print("****    Interpretar = ",end='      ')
print("        Intimidar = ",end='     ')
print("        Inutilizarmecanismo = ")

print("****    Juegodemanos = ",end='     ')
print("        Lingüística = ",end='       ')
print("        Montar = ")

print("****    Nadar = ",end='            ')
print("        Percepción = ",end='    ')
print("        Profesión = ")

print("****    Saber_geografía = ",end='  ')
print("        Saber_losPlanos = ",end='       ')
print("        Saber_ingeniería = ")

print("****    Saber_arcano = ",end='     ')
print("        Saber_nobleza = ",end='       ')
print("        Saber_historia = ")

print("****    Saber_Naturaleza = ",end=' ')
print("        Saber_dungeons = ",end='       ')
print("        Saber_religión = ")

print("****    Sigilo = ",end='           ')
print("        Supervivencia = ",end='       ')
print("        Tasación = ")

print("****    Tratoconanimales = ",end=' ')
print("        Trepar = ",end='       ')
print("        Usarobjetomágico = ",end='       ')
print("        Volar = ")

for i in range(5):
    print(" ")
    