from ast import Str
import pandas as pd
df = pd.read_csv("spell_full - Updated 31Mar2020.csv", header=0, sep=',')
#print (df['name'])

#print (df [['name']] [df ['name'] == 'Aid'])
#print(df['name','descriptor'])
    
print("""
        Dime, ¿qué hecizo Buscas?
        
        """)

spl = input("Elige una opcion: ")

    


#Descripcion = df [['description']] [df ['name'] == 'Aid']
Descripcion = df [df ['name'] == spl]
print (Descripcion)
