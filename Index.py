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
print("====    MODFUE: " + str(pl.MODFUE)+"  -  MODDES:"+ str(pl.MODDES)+"  -  MODCON:"+ str(pl.MODCON),end='')
print("    MODINT: " + str(pl.MODINT)+"  -  MODSAB:"+ str(pl.MODSAB)+"  -  MODCAR:"+ str(pl.MODCAR))
print("====    CA : "+str(pl.CA)+"       *****    INICIATIVA: "+str(pl.INICIATIVA))
print("====    TOQUE: "+str(pl.TOQUE)+"      *****    DESPREVENIDO: "+str(pl.DESPREVENIDO))
print("====    FORTALEZA: " + str(pl.FORTALEZA)+"  *****    BMC: "+str(pl.BMC))
print("====    REFLEJOS: " + str(pl.REFLEJOS)+"   *****    DMC: "+str(pl.DMC))
print("====    VOLUNTAD: " + str(pl.VOLUNTAD)+"   *****    IDIOMA: "+str(pl.Idiomas))

    
print("****_________________________________________________________________________________________________")    
print("****    Habilidades: ")
print("****")    


print("****    Acrobacias = ",pl.Acrobacias           ,end='       ')
print("        Artesanía = ",pl.Artesania            ,end='       ')
print("        Averiguarintenciones = ",pl.Averiguarintenciones )
print("****    Conocimientodeconjuros = ",pl.Conocimientodeconjuros,end='')
print("   Curar = ",pl.Curar                ,end='        ')
print("        Disfrazarse = ",pl.Disfrazarse          )
print("****    Diplomacia = ",pl.Diplomacia           ,end='       ')
print("        Engañar = ",pl.Engañar              ,end='       ')
print("        Escapismo = ",pl.Escapismo            )
print("****    Interpretar = ",pl.Interpretar          ,end='      ')
print("        Intimidar = ",pl.Intimidar            ,end='     ')
print("        Inutilizarmecanismo = ",pl.Inutilizarmecanismo  )
print("****    Juegodemanos = ",pl.Juegodemanos         ,end='     ')
print("        Lingüística = ",pl.Lingüística          ,end='    ')
print("        Montar = ",pl.Montar               )
print("****    Nadar = ",pl.Nadar                ,end='            ')
print("        Percepción = ",pl.Percepción           ,end='    ')
print("        Profesión = ",pl.Profesión            )
print("****    Saber_geografía = ",pl.Saber_geografía      ,end='  ')
print("        Saber_losPlanos = ",pl.Saber_losPlanos      ,end='')
print("        Saber_ingeniería = ",pl.Saber_ingeniería     )
print("****    Saber_arcano = ",pl.Saber_arcano         ,end='     ')
print("        Saber_nobleza = ",pl.Saber_nobleza        ,end=' ')
print("        Saber_historia = ",pl.Saber_historia       )
print("****    Saber_Naturaleza = ",pl.Saber_Naturaleza     ,end=' ')
print("        Saber_dungeons = ",pl.Saber_dungeons       ,end=' ')
print("        Saber_religión = ",pl.Saber_religión       )
print("****    Sigilo = ",pl.Sigilo               ,end='           ')
print("        Supervivencia = ",pl.Supervivencia        ,end='')
print("        Tasación = ",pl.Tasación             )
print("****    Tratoconanimales = ",pl.Tratoconanimales     ,end=' ')
print("        Trepar = ",pl.Trepar               ,end='       ')
print("        Usarobjetomágico = ",pl.Usarobjetomágico     ,end=' ')
print("    Volar = ",pl.Volar                )
      
print("****    Dotes: ")

print(pl.Dotes)

for i in range(5):
    
    print('')

"""
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
"""