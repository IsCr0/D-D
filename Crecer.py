#import HojaPersonaje
import json

f = open("soul.json","r")

data = json.load(f)

#print(data["Dote"]["Soltura con un arma"])

#Agregar Dotte
data["Dote"].update({'Hendedura' : 'Haz un ataque adicional si el primero impacta'})
#Eliminar Dote
#data["Dote"].pop('Hendedura')

f.close


with open('soul.json', 'w') as outfile:
    json.dump(data, outfile)
    #data["str"] = 20
    
"""

#print(data["Ataque poderoso"])

crece = open('Alma.txt','w')

crece.write(line.replace('16','18'))

crece.close()
"""