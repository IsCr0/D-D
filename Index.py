from HojaPersonaje import Dotes
import HojaPersonaje as pl

class Interfaz:
    
    Clase = pl.CLASE
    
    print("======================================================================================================")
    print("======================================================================================================")
    print("====                                 "+Clase+"                                                    =====")
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
    print("====_________________________________________________________________________________________________")
    print("====    MODFUE: " + str(pl.MODFUE)+"  -  MODDES:"+ str(pl.MODDES)+"  -  MODCON:"+ str(pl.MODCON))
    print("====    MODINT: " + str(pl.MODINT)+"  -  MODSAB:"+ str(pl.MODSAB)+"  -  MODCAR:"+ str(pl.MODCAR))
    print("====_________________________________________________________________________________________________")
    print("====    CA : "+str(pl.CA)+"       *****    INICIATIVA: "+str(pl.INICIATIVA))
    print("====    TOQUE: "+str(pl.TOQUE)+"      *****    DESPREVENIDO: "+str(pl.DESPREVENIDO))
    print("====    FORTALEZA: " + str(pl.FORTALEZA)+"  *****    BMC: "+str(pl.BMC))
    print("====    REFLEJOS: " + str(pl.REFLEJOS)+"   *****    DMC: "+str(pl.DMC))
    print("====    VOLUNTAD: " + str(pl.VOLUNTAD)+"   *****    IDIOMA: "+str(pl.Idiomas))

        
    print("****_________________________________________________________________________________________________")    
    print("****    Habilidades: ")
    print("****")    


    print("****    Acrobacias = ",pl.Acrobacias           ,end='       ')
    print("        Artesan??a = ",pl.Artesania            ,end='    ')
    print("        Averiguarintenciones = ",pl.Averiguarintenciones )
    print("****    Conocimientodeconjuros = ",pl.Conocimientodeconjuros,end='')
    print("   Curar = ",pl.Curar                ,end='        ')
    print("        Disfrazarse = ",pl.Disfrazarse          )
    print("****    Diplomacia = ",pl.Diplomacia           ,end='       ')
    print("        Enga??ar = ",pl.Enga??ar              ,end='      ')
    print("        Escapismo = ",pl.Escapismo            )
    print("****    Interpretar = ",pl.Interpretar          ,end='      ')
    print("        Intimidar = ",pl.Intimidar            ,end='    ')
    print("        Inutilizarmecanismo = ",pl.Inutilizarmecanismo  )
    print("****    Juegodemanos = ",pl.Juegodemanos         ,end='     ')
    print("        Ling????stica = ",pl.Ling????stica          ,end='  ')
    print("        Montar = ",pl.Montar               )
    print("****    Nadar = ",pl.Nadar                ,end='            ')
    print("        Percepci??n = ",pl.Percepci??n           ,end='   ')
    print("        Profesi??n = ",pl.Profesi??n            )
    print("****    Saber_geograf??a = ",pl.Saber_geograf??a      ,end='  ')
    print("        Saber_losPlanos = ",pl.Saber_losPlanos      ,end='')
    print("      Saber_ingenier??a = ",pl.Saber_ingenier??a     )
    print("****    Saber_arcano = ",pl.Saber_arcano         ,end='     ')
    print("        Saber_nobleza = ",pl.Saber_nobleza        ,end='')
    print("        Saber_historia = ",pl.Saber_historia       )
    print("****    Saber_Naturaleza = ",pl.Saber_Naturaleza     ,end=' ')
    print("        Saber_dungeons = ",pl.Saber_dungeons       ,end='')
    print("       Saber_religi??n = ",pl.Saber_religi??n       )
    print("****    Sigilo = ",pl.Sigilo               ,end='           ')
    print("        Supervivencia = ",pl.Supervivencia        ,end='')
    print("        Tasaci??n = ",pl.Tasaci??n             )
    print("****    Tratoconanimales = ",pl.Tratoconanimales     ,end=' ')
    print("        Trepar = ",pl.Trepar               ,end='       ')
    print("        Usarobjetom??gico = ",pl.Usarobjetom??gico     ,end=' ')
    print("    Volar = ",pl.Volar                )
        
    print("****    Dotes: ")

    print(pl.Dotes)

    for i in range(5):
        
        print('')
"""
class InterfazMago:
    print("======================================================================================================")
    print("======================================================================================================")
    print("====                                   Mago                                                      =====")
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
    print("        Artesan??a = ",pl.Artesania            ,end='       ')
    print("        Averiguarintenciones = ",pl.Averiguarintenciones )
    print("****    Conocimientodeconjuros = ",pl.Conocimientodeconjuros,end='')
    print("   Curar = ",pl.Curar                ,end='        ')
    print("        Disfrazarse = ",pl.Disfrazarse          )
    print("****    Diplomacia = ",pl.Diplomacia           ,end='       ')
    print("        Enga??ar = ",pl.Enga??ar              ,end='       ')
    print("        Escapismo = ",pl.Escapismo            )
    print("****    Interpretar = ",pl.Interpretar          ,end='      ')
    print("        Intimidar = ",pl.Intimidar            ,end='     ')
    print("        Inutilizarmecanismo = ",pl.Inutilizarmecanismo  )
    print("****    Juegodemanos = ",pl.Juegodemanos         ,end='     ')
    print("        Ling????stica = ",pl.Ling????stica          ,end='    ')
    print("        Montar = ",pl.Montar               )
    print("****    Nadar = ",pl.Nadar                ,end='            ')
    print("        Percepci??n = ",pl.Percepci??n           ,end='    ')
    print("        Profesi??n = ",pl.Profesi??n            )
    print("****    Saber_geograf??a = ",pl.Saber_geograf??a      ,end='  ')
    print("        Saber_losPlanos = ",pl.Saber_losPlanos      ,end='')
    print("        Saber_ingenier??a = ",pl.Saber_ingenier??a     )
    print("****    Saber_arcano = ",pl.Saber_arcano         ,end='     ')
    print("        Saber_nobleza = ",pl.Saber_nobleza        ,end=' ')
    print("        Saber_historia = ",pl.Saber_historia       )
    print("****    Saber_Naturaleza = ",pl.Saber_Naturaleza     ,end=' ')
    print("        Saber_dungeons = ",pl.Saber_dungeons       ,end=' ')
    print("        Saber_religi??n = ",pl.Saber_religi??n       )
    print("****    Sigilo = ",pl.Sigilo               ,end='           ')
    print("        Supervivencia = ",pl.Supervivencia        ,end='')
    print("        Tasaci??n = ",pl.Tasaci??n             )
    print("****    Tratoconanimales = ",pl.Tratoconanimales     ,end=' ')
    print("        Trepar = ",pl.Trepar               ,end='       ')
    print("        Usarobjetom??gico = ",pl.Usarobjetom??gico     ,end=' ')
    print("    Volar = ",pl.Volar                )
        
    print("****    Dotes: ")

    print(pl.Dotes)

    for i in range(5):
        
        print('')
"""