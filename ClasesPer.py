
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
        
    #Habilidades Tiradas de clase +3 al subir estas habilidades
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
        
    #Habilidades Tiradas de clase +3 al subir estas habilidades
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
    

def DotesLista():
    dotes = [
    "Abstención de materiales — Lanzas conjuros sin componentes materiales",
    "Acometer* Ataque base +6 Aceptas un pen. –2 a tu CA para atacar con alcance",
    "Acrobático — Bonif. +2 a las pruebas de Acrobacias y de Volar",
    "Afinidad con los animales — Bonif. +2 a las pr. de Trato con animales y de Montar",
    "Aguante — Bonificador +4 a las pruebas para evitar daño no letal",
    "Duro de pelar Aguante Automáticamente estabilizado y consciente a menos de 0 pg",
    "Alerta — Bonif. +2 a las pr. de Percepción y de Averiguar intenciones",
    "Aptitudes mágicas — Bonif. +2 a las pr. de Con. de conjuros y Usar objeto mágico",
    "Artesano maestro 5 rangos en cualquier Puedes crear obj. mágicos sin ser un lanzador de conjuros habilidad de Artesanía o Profesión",
    "Ataque poderoso* Fue13, ataque base +1 Cambias bonificador al ataque cuerpo a cuerpo por daño",
    "Arrollar mejorado* Ataque poderoso Bonificador +2 a intentos de arrollar, no AdO",
    "Arrollar mayor* Arrollar mejorado, ataque base +6 Los enemigos a los que arrollas provocan AdO",
    "Embestida mejorada* Ataque poderoso Bonificador +2 a los intentos de embestida, sin AdO",
    "Embestida mayor* Embestida mejorada, ataque base +6 Los enemigos a los que embistes provocan AdO",
    "Hendedura* Ataque poderoso Haz un ataque adicional si el primero impacta",
    "Gran hendedura* Hendedura, ataque base +4 Haz un ataque adicional después de cada ataque que impacte",
    "Romper arma mejorado* Ataque poderoso Bonificador +2 a los intentos de romper arma, sin AdO",
    "Romper arma mayor* Romper arma mejorado, Daño de intentos de romper arma transferido a tu enemigo",
    "Atlético — Bonificador +2 a las pruebas de Trepar y Nadar",
    "Aumentar convocación Soltura con conjuros (conjuración) Criaturas convocadas obtienen +4 Fue y Con",
    "Autosuficiente — Bonificador +2 a las pruebas de Curar y de Supervivencia",
    "Canalización adicional Rasgo de clase canalizar energía Canalizas energía 2 veces/día adicionales",
    "Canalización elemental Rasgo de clase canalizar energía Canalizar energía puede curar o dañar elementales",
    "Canalización mejorada Rasgo de clase canalizar energía Bonificador +2 a la CD de canalizar energía",
    "Canalización selectiva Car 13, r. de clase canalizar energía Escoges a quién afectar con canalizar energía",
    "Canalizar alineamiento Rasgo de clase canalizar energía Canalizar energía puede curar o dañar a los ajenos",
    "Canalizar castigo* Rasgo de clase canalizar energía Canalizas energía a través de tu ataque",
    "Comandar muertos vivientes R. de clase canalizar energía negativa C. energía puede utilizarse para controlar muertos vivientes",
    "Combate con dos armas* Des 15 Reduce los penalizadores por luchar con dos armas",
    "C. con dos armas mejorado* Des 17, C. con dos armas, at. base +6 Obtienes un ataque adicional con la mano torpe",
    "C. con dos armas mayor* Des 19, C. con dos armas mejorado, Obtienes un tercer ataque con la mano torpe",
    "C. con dos armas, ataque base +11",
    "Defensa con dos armas* Combate con dos armas Bonificador +1 por escudo cuando luchas con dos armas",
    "Doble tajo* Combate con dos armas Sumas bonif. por Fue a las tiradas de daño con la mano torpe",
    "Desgarrar con dos armas* Doble tajo, C. con dos armas mej., Desgarras a un enemigo impactado por tus dos armas ataque base +11",
    "Combatir desde una montura* Montar 1 rango Evitas ataques a la montura con una prueba de Montar",
    "Ataque al galope* Combatir desde una montura Te mueves antes y después de un ataque montado",
    "Carga impetuosa* Ataque al galope Doble daño en una carga montado",
    "Desmontar jinete* Combatir desde una montura, Derribas a los oponentes de sus monturas Embestida mejorada",
    "Disparar desde una montura* Combatir desde una montura Mitad de penalización por ataques a distancia montado",
    "Pisotear* Combatir desde una montura Arrollas a objetivos montado",
    "Comp. con arma exótica* Ataque base +1 Sin penalizador en ataques con un arma exótica",
    "Comp. con arma marcial — Sin penalizador a los ataques hechos con un arma marcial",
    "Competencia con armadura ligera — Sin penalizadores a los ataques llevando armadura ligera",
    "Comp. con arm. intermedia Comp. con armadura ligera Sin penalizadores a los ataques llevando arm. intermedia",
    "Comp. con armadura pesada Comp. con armadura intermedia Sin penalizadores a los ataques llevando armadura pesada",
    "Competencia con armas sencillas — Sin penalizadores a los ataques hechos con armas sencillas",
    "Competencia con escudo — Sin penalizadores a las tiradas de ataque usando un escudo",
    "Comp. con escudo pavés* Competencia con escudo Sin pen. a las tiradas de ataque al usar un escudo pavés",
    "Golpear con esc. mejorado* Competencia con escudo Mantienes tu bonificador por escudo cuando golpeas con él",
    "Golpetazo con el escudo * Golpear con el escudo mejorado, Embestida gratuita con un ataque de golpear con el escudo",
    "Combate con dos armas, ataque base +6",
    "Maestro del escudo* Golp. con el escudo, at. base +11 Sin penalizadores atacar con dos armas con un escudo",
    "Soltura con el escudo* Comp. con escudo, ataque base +1 Obtienes un bonificador +1 a tu CA al usar un escudo",
    "Solt. mayor con el escudo* Solt. con el escudo, gue. de 8º nivel Obtienes un bonificador +1 a tu CA al usar un escudo",
    "Conjurar en combate — Bonificador +4 a las pr. de concentración lanz. a la defensiva",
    "Conjuros naturales Sab 13, rasgo de clase forma salvaje Lanzas conjuros estando en forma salvaje",
    "Conjuros perforantes — Bonificador +2 a las pruebas de nivel para superar la RC",
    "Conjuros perforantes mayor Conjuros perforantes Bonificador +2 a las pruebas de nivel para superar la RC",
    "Contraatacar* Ataque base +11 Atacas a enemigos que te atacan usando alcance",
    "Contraconjuro mejorado — Contraconjuras con un conjuro de la misma escuela",
    "Correr — Corres a 5 veces tu velocidad normal",
    "Crítico mejorado* Comp. con un arma, at. base +8 Doblas el rango de amenaza de un arma",
    "Desenvainado rápido* Ataque base +1 Desenvainas un arma como acción gratuita",
    "Disparo a bocajarro* — +1 ataque y daño a objetivos a 30 pies (9 m) o menos",
    "Disparo a la carrera* Des 13, Movilidad, Disp. a bocajarro, Atacas a distancia en cualquier punto del movimiento ataque base +4",
    "Disparo a larga distancia* Disparo a bocajarro Reduce a la mitad las penalizaciones por alcance",
    "Disparo preciso* Disparo a bocajarro Sin penalizador por disparar a un cuerpo a cuerpo",
    "Disparo preciso mejorado* Des 19, D. preciso, ataque base +11 Sin cobertura u ocultamiento en ataques a distancia",
    "Puntería precisa* D. preciso mej., ataque base +16 Sin bonif. por armadura o escudo en un ataque a distancia",
    "Disparo rápido* Des 13, Disparo a bocajarro Haces un ataque a distancia adicional",
    "Disparos múltiples* Des 17, Disp. rápido, ataque base +6 Disparas dos flechas simultáneamente",
    "Dureza — +3 puntos de golpe, +1 por Dado de golpe más allá del 3º",
    "Engañoso — Bonificador +2 a las pruebas de Engañar y Disfrazarse",
    "Entr. arcano con armadura* Comp. arm. ligera, n. de lanzador 3º Reduce probabilidad de fallo de conjuros arcanos en 10%",
    "Maestría arcana con armadura* Entr. arcano con armadura, Reduce probabilidad de fallo de conjuros arcanos en 20%",
    "Comp. arm. intermedia, NL 7º",
    "Entr. en combate defensivo* — Usas todos tus DG como ataque base para la DMC",
    "Esquiva* Des 13 Bonificador +1 por esquiva a la CA",
    "Movilidad* Esquiva +4 a la CA contra ataques de oportunidad por movimiento",
    "Ataque elástico* Movilidad, ataque base +4 Te mueves antes y después de un ataque cuerpo a cuerpo",
    "Posición del viento* Des 15, Esquiva, ataque base +6 Obtienes 20% de ocultación si te mueves",
    "Posición del relámpago* Des 17, Pos. del viento, at. base +11 Obtienes 50% de ocultación si te mueves",
    "Expulsar muertos vivientes R. de clase canalizar energía positiva C. energía puede usarse para hacer huir a los m. vivientes",
    "Familiar mejorado Capacidad para obtener un familiar, Obtienes un familiar más poderoso ver texto de la dote",
    "Furia adicional Rasgo de clase furia Tienes 6 asaltos/día adicionales de furia",
    "Golpe arcano* Aptitud para lanzar conjuros arcanos +1 al daño y las armas se consideran mágicas",
    "Golpe vital* Ataque base +6 Infliges el doble de daño normal en un solo ataque",
    "Golpe vital mejorado* Golpe vital, ataque base +11 Infliges el triple de daño normal en un solo ataque",
    "Golpe vital mayor* G. vital mej., G. vital, at. base +16 Infliges el cuádruple de daño normal en un solo ataque",
    "Gran fortaleza — +2 a las salvaciones de Fortaleza",
    "Gran fortaleza mejorada Gran fortaleza Puedes repetir una salvación de Fortaleza 1 vez/día",
    "Impacto sin arma mejorado* — Siempre se te considera armado",
    "Desviar flechas* Des 13, Impacto sin arma mejorado Evitas 1 ataque a distancia por asalto",
    "Atrapar flechas* Des 15, Desviar flechas Atrapas 1 ataque a distancia por asalto",
    "Estilo del escorpión* Impacto sin arma mejorado Reduces la velocidad del objetivo en 5 pies (1,5 m)",
    "Puño del gorgón* Estilo del escorpión, ataque base +6 Dejas grogui a un enemigo cuya velocidad ha sido reducida",
    "Ira de la medusa* Puño del gorgón, ataque base +11 2 ataques adicionales contra un enemigo obstaculizado",
    "Presa mejorada* Des 13, Impacto sin arma mejorado Bonif. +2 a las pruebas de presa, sin ataque de oportunidad",
    "Presa mayor* Presa mejorada, ataque base +6 Mantienes una presa como acción de movimiento",
    "Puñetazo aturdidor* Des 13, Sab 13, Imp. sin arma mej., Aturdes a un oponente con un impacto sin arma ataque base +8",
    "Imposición de manos adicional Rasgo de clase imposición de manos Tienes 2 usos/día adicionales de imposición de manos",
    "Iniciativa mejorada* — Bonificador +4 a las pruebas de iniciativa",
    "Interpretación adicional Rasgo de clase interp. de bardo Tienes 6 asaltos/día adicionales de interpretación de bardo",
    "Ki adicional Rasgo de clase reserva de ki Aumentas tu reserva de ki en 2 puntos",
    "Lanzar cualquier cosa* — Sin penalizadores por armas a distancia improvisadas",
    "Liderazgo Nivel de personaje 7º Ganas un allegado y seguidores",
    "Lucha a ciegas* — Tira de nuevo probabilidades de ocultación fallidas",
    "Maestría con armas improvisadas* Usar arma improvisada o Conviertes en mortal un arma improvisada",
    "Lanzar cualquier cosa, ataque base +8",
    "Maestría en conjuros Mago de 1er nivel Preparas algunos conjuros sin libro de conjuros",
    "Maniobras ágiles* — Usas tu bonificador de Des para calcular tu BMC",
    "Manos hábiles — Bonif. +2 a las pr. de Inutilizar mecanismo y Juego de manos",
    "Merced adicional Rasgo de clase merced Tu imposición de manos tiene 1 merced adicional",
    "Movimientos ágiles Des 13 Ignoras 5 pies (1,5 m) de terreno difícil cuando te mueves",
    "Pasos acrobáticos Des 15, Movimientos ágiles Ignoras 20 pies (6 m) de terreno difícil cuando te mueves",
    "Paso adelante* Ataque base +1 Das un paso de 5 pies (1,5 m) como acción inmediata",
    "Pericia en combate* Int 13 Cambias bonificador al ataque por bonificador a la CA",
    "Ataque de torbellino* Des 13, Pericia en combate, Haz un at. c/c contra todos los enemigos a tu alcance",
    "Ataque elástico, ataque base +4",
    "Derribo mejorado* Pericia en combate Bonif. +2 a los intentos de derribo, sin AdO",
    "Derribo mayor* Derribo mejorado, ataque base +6 Enemigos a los que derribas provocan AdO",
    "Desarme mejorado* Pericia en combate Bonificador +2 a los intentos de desarmar, sin AdO",
    "Desarme mayor Desarme mejorado, ataque base +6 Armas afectadas arrojadas fuera del alcance de tu enemigo",
    "Finta mejorada* Pericia en combate Fintas como acción de movimiento",
    "Finta mayor* Finta mejorada, ataque base +6 Enemigos fintados pierden 1 asalto su bonificador por Des",
    "Persuasivo — Bonificador +2 a las pruebas de Diplomacia y de Intimidar",
    "Perturbador* Guerrero de 6º nivel Aumenta la CD de lanzar conjuros adyacentes a ti",
    "Rompeconjuros* Perturbador, guerrero de 10º nivel Enemigos provocan ataques si sus conjuros fallan",
    "Pies ligeros — Tu velocidad base aumenta en 5 pies (1,5 m)",
    "Poderío intimidante* — Suma Fue a Intimidar además de Car",
    "Puntería mortal* Des 13, ataque base +1 Cambias bonificador de ataque a distancia por daño.",
    "Recarga rápida* Competencia con arma (ballestas) Recargas rápidamente una ballesta",
    "Reflejos de combate* — Haz ataques de oportunidad adicionales",
    "Detener* Reflejos de combate Evitas que los enemigos te rebasen",
    "Reflejos rápidos — Bonificador +2 a las salvaciones de Reflejos",
    "Reflejos rápidos mejorados Reflejos rápidos Una vez al día puedes repetir una salvación de Reflejos",
    "Sigiloso — Bonificador +2 a las pruebas de Escapismo y de Sigilo",
    "Soltura con los conjuros — Bonificador +1 a la CD de las salvaciones para una escuela",
    "Soltura mayor con los conjuros Soltura con conjuros Bonificador +1 a la CD de las salvaciones para una escuela",
    "Soltura con los críticos* Ataque base +9 Bonificador +4 a las tiradas de ataque para confirmar impactos críticos",
    "Crítico asombroso* Soltura con los críticos , at. base +13 Cuando consigues un crítico, el objetivo queda grogui.",
    "Crítico aturdidor* Crítico asombroso, ataque base +17 Cuando consigues un crítico, el objetivo queda aturdido",
    "Crítico cegador* Soltura con los críticos , at. base +15 Cuando consigues un crítico, el objetivo queda cegado",
    "Crítico ensordecedor* Soltura con los críticos , at. base +13 Cuando consigues un crítico, el objetivo queda ensordecido",
    "Crítico fatigante* Soltura con los críticos , at. base +13 Cuando consigues un crítico, el objetivo queda fatigado",
    "Crítico agotador* Crítico fatigante, ataque base +15 Cuando consigues un crítico, el objetivo queda exhausto",
    "Crítico nauseabundo* Soltura con los críticos , at. base +11 Cuando consigues un crítico, el objetivo queda indispuesto",
    "Crítico sangrante* Soltura con los críticos , at. base +11 Cuando consigues un cr., además 2d6 pg de sangrado",
    "Maestría con los críticos* 2 dotes de crítico, guerrero nivel 14º Aplica 2 efectos a tus impactos críticos",
    "Soltura con un arma* Comp. con un arma, ataque base +1 Bonif. +1 a las tiradas de ataque con un arma determinada",
    "Especialización con un arma* S. con un arma, guerrero de 4º nivel Bonificador +2 a las tiradas de daño con un arma determinada",
    "Esp. mayor con un arma* Esp. con un arma, gue. de 12º nivel Bonificador +2 a las tiradas de daño con un arma determinada",
    "Exhibición deslumbrante* Soltura con un arma Intimidas a todos los enemigos a 30 pies (9 m) o menos",
    "Destrozar defensas* Exh. deslumbrante, ataque base +6 Los enemigos obstaculizados quedan desprevenidos",
    "Golpe mortal* Soltura mayor con un arma, Infliges doble daño y además 1 punto de sangrado de Con",
    "Destrozar defensas, ataque base +11",
    "Golpe perforante* S. con un arma, guerrero de 12º nivel Tus ataques ignoran 5 puntos de RD",
    "Golpe perforante mayor* G. perforante, guerrero de 16º nivel Tus ataques ignoran 10 puntos de RD",
    "Soltura mayor con un arma * S. con un arma, guerrero de 8º nivel Bonif. +1 a las tiradas de ataque con un arma determinada",
    "Soltura con una habilidad — Bonificador +3 a una habilidad (+6 con 10 rangos)",
    "Sutileza con las armas* — Des en lugar de Fue en tiradas de ataque con armas ligeras",
    "Usar arma improvisada* — Sin penalizadores por armas cuerpo a cuerpo improvisadas",
    "Voluntad de hierro — Bonificador +2 a las salvaciones de Voluntad",
    "Voluntad de hierro mejorada Voluntad de hierro Una vez al día puedes repetir una salvación de Voluntad",
    "Dotes de creación de objeto Prerrequisitos Beneficios",
    "Elaborar poción Nivel de lanzador 3º Crear pociones mágicas",
    "Fabricar ar. y armaduras mágicas Nivel de lanzador 5º Crear armas, armaduras y escudos mágicos",
    "Fabricar bastón Nivel de lanzador 11º Crear bastones mágicos",
    "Fabricar cetro Nivel de lanzador 9º Crear cetros mágicos",
    "Fabricar objeto maravilloso Nivel de lanzador 3º Crear objetos maravillosos mágicos",
    "Fabricar varita Nivel de lanzador 5º Crear varitas mágicas",
    "Forjar anillo Nivel de lanzador 7º Crear anillos mágicos",
    "Inscribir pergamino Nivel de lanzador 1º Crear pergaminos mágicos",
    "Ampliar conjuro — Doblas el alcance de un conjuro",
    "Apresurar conjuro — Lanzas un conjuro como acción rápida",
    "Conjurar en silencio — Lanzas un conjuro sin componentes verbales",
    "Conjurar sin moverse — Lanzas un conjuro sin componentes verbales",
    "Extender conjuro — Doblas el área de un conjuro",
    "Intensificar conjuro — Tratas un conjuro como de un nivel mayor",
    "Maximizar conjuro — Maximizas las variables de un conjuro",
    "Potenciar conjuro — Incrementas en un 50% las variables de un conjuro",
    "Prolongar conjuro — Doblas la duración de un conjuro",
] 