from flask import Flask, render_template
#from DungeonsAndDragons import dotes
import HojaPersonaje as pl

app = Flask(__name__)

@app.route('/')
def home():
    nom = str(pl.NomPer)
    insEq = pl
    lEqu = insEq.Equipos
    Armad = insEq.Armadura
    return render_template('DandDhp.html', nombrePer = str(pl.NomPer), nvl = str(pl.NIVEL),
                           alin = pl.ALINEAMIENTO, pungol = str(pl.PG), FUE = str(pl.FUE),
                           DES = str(pl.DES), CON = str(pl.CON), INT = str(pl.INT), SAB = str(pl.SAB), CAR = str(pl.CAR),
                           MODFUE = str(pl.MODFUE), MODDES = str(pl.MODDES), MODCON = str(pl.MODCON),
                           MODINT = str(pl.MODINT), MODSAB = str(pl.MODSAB), MODCAR = str(pl.MODCAR),
                           CLASE = str(pl.CLASE), ALINEAMIENTO = str(pl.ALINEAMIENTO), RAZA = str(pl.RAZA), lEqu = lEqu, Armad=Armad)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/webassambly')
def webassambly():
    return render_template('webassambly.html')

@app.route('/ia')
def ia():
    return render_template('ia.html')

"""
@app.route('/otros')
def otros():
    return render_template('otros.html')
"""
nombres = ["Juan", "María", "Carlos", "Luisa", "Ana", "Pedro", "Sofía", "David", "Laura", "Miguel"]
@app.route('/otros')
def otros():
    
    return render_template('DandD.html', nombres = pl.dotes)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()