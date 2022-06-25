
#-----------------------------------------------------------------------------------------------------------------
#---------------------------------------------- Guerrero ---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------- 
GuerreroAtaqueBase = [1,2,3,4,5]
GuerreroFor = [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12]
GuerreroRef = [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
GuerreroVol = [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]

#print(len(GuerreroRef))

class Guerrero:
    
    NomClase = 'Guerrero'
    DadoGolpe = '1d10'
    ModHabilidad = 2
    #Hacer una lista con las tiradas
    #AtaqueBase = nvl*1#Cada 2 niveles +1

    #Return (AtaqueBase)
    def Atq(nvl):
        AtaqueBase = nvl*1
        return AtaqueBase
    
    def Fortaleza(nvl):
        #Tirada de Salvacion Fortaleza
        TirFor = GuerreroFor[nvl-1]#Cada 2 niveles +1
        return TirFor
    
    def Reflejos(nvl):
        #Tirada de Salvacion Reflejos
        TirRef = GuerreroRef[nvl-1]#Cada 2 niveles +1
        return TirRef
    
    def Voluntad(nvl):
        #Tirada de Salvacion Voluntad
        TirVol = GuerreroVol[nvl-1]#Cada 2 niveles +1
        return TirVol
        
    #Habilidades
    """ 
	Artesania           = TRUE
    Intimidar           = TRUE
    Montar              = TRUE
    Nadar               = TRUE
    Profesión           = TRUE
    SaberIngeniería     = TRUE
    SaberNaturaleza     = TRUE
    SaberdDungeons      = TRUE
    TratoconAnimales    = TRUE
    Trepar              = TRUE
    """

#-----------------------------------------------------------------------------------------------------------------
#---------------------------------------------- Mago ----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------    

MagoAtaqueBase = [0,1,1,2,2,3,3,4,4,5,5]
MagoFor = [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
MagoRef = [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
MagoVol = [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12]

#print(len(MagoRef))

class Mago:
      
    NomClase = 'Mago'
    DadoGolpe = '1d6'
    ModHabilidad = 2
    #Hacer una lista con las tiradas
    #AtaqueBase = nvl*1#Cada 2 niveles +1

    #Return (AtaqueBase)
    def Atq(nvl):
        AtaqueBase = nvl*1
        return AtaqueBase
    
    def Fortaleza(nvl):
        #Tirada de Salvacion Fortaleza
        TirFor = MagoFor[nvl-1]#Cada 2 niveles +1
        return TirFor
    
    def Reflejos(nvl):
        #Tirada de Salvacion Reflejos
        TirRef = MagoRef[nvl-1]#Cada 2 niveles +1
        return TirRef
    
    def Voluntad(nvl):
        #Tirada de Salvacion Voluntad
        TirVol = MagoVol[nvl-1]#Cada 2 niveles +1
        return TirVol
        
    #Habilidades
    """ 
	Artesania           = TRUE
    Intimidar           = TRUE
    Montar              = TRUE
    Nadar               = TRUE
    Profesión           = TRUE
    SaberIngeniería     = TRUE
    SaberNaturaleza     = TRUE
    SaberdDungeons      = TRUE
    TratoconAnimales    = TRUE
    Trepar              = TRUE
    """
    

