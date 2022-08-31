import HojaPersonaje as HP

Np = int(input("cuantos personajes: "))

    #import HojaPP as HP
Par = open('lol/prueba.json', 'w')#Crea el json de la pelea
    
for item in range(2):
    
    #linea = '{"' + str(HP).NomPer+'":{''"pg":"'+ str(HP.PG+','+'"str":"'+ str(HP).MODFUE+'"des":"'+ str(HP).MODDES+'"con":"'+ str(HP).MODCON+'"int":"'+ str(HP).MODINT+'"sab":"'+ str(HP).MODSAB+'"car":"'+ str(HP).MODCAR+'}'
    linea = '{"' + str(HP.NomPer)+'":{''"pg":'+ str(HP.PG)+',"str":'+ str(HP.MODFUE)+',"des":'+ str(HP.MODDES)+',"con":'+ str(HP.MODCON)+',"int":'+ str(HP.MODINT)+',"sab":'+ str(HP.MODSAB)+',"car":'+ str(HP.MODCAR)+'}'

    #print (linea)
    #quit()
    
    Par.write(linea)
    
    Par.write('}')
    if item > (Np-1): Par.write(',')

Par.close()

with open('lol/prueba.json','r') as pru :
    
    
    
    print(pru.read())
"""
for item in range(Np):
    
    #Opc = int(input("nombre del personaje"))
    #HP.Hoja.soul = Opc+".json"
    HP.Hoja.soul = "soulPru3.json"
    #HP.SoulSel(2)
    #HP
"""


