from flask import Flask
from flask import render_template, redirect, url_for, request
from register import Register
from pripominka import Pripominka
import datetime

app = Flask (__name__)

from program import Program
program = Program()



@app.route ('/')
def uvodni_strana():
    zvoleny_register = program.otevrit_program ()
    volby = program.zobraz_menu()
    return render_template ('uvodni_strana.html',prvni_button = volby[0],
    druhy_button = volby[1], treti_button = volby[2], ctvrty_button = volby[3])

@app.route('/ukaze_vse')
def ukaze_vse():
    zvoleny_register = program.otevrit_program()
    vse_pripominky = (zvoleny_register.ukaze_pripominky())
    volby = program.zobraz_menu()
    return render_template("ukaz_vse.html",
    vse_pripominky = vse_pripominky, prvni_button = volby[0],
    druhy_button = volby[1], treti_button = volby[2], ctvrty_button = volby[3])

@app.route('/nova_pripominka')
def nova_pripominka():
    return render_template ('nova_pripominka.html')

@app.route('/zadana_pripominka', methods = ['POST'])
def zadana_pripominka():
    text_pripominky = request.form.get ("text_pripominky")
    termin = request.form.get ('termin')
    zvoleny_register = program.otevrit_program()
    last_id = zvoleny_register.zjisti_last_id()
    zvoleny_register.nova_pripominka(text_pripominky,termin,last_id)
    vse_pripominky = (zvoleny_register.ukaze_pripominky())
    volby = program.zobraz_menu()
    program.uloz_prubezne_register(zvoleny_register)
    return render_template ('zadana_pripominka.html',
    text_pripominky = text_pripominky, termin = termin,
    vse_pripominky = vse_pripominky, prvni_button = volby[0])

@app.route('/oznacit_splnena')
def oznacit_splnena():
    zvoleny_register = program.otevrit_program()
    vse_pripominky = (zvoleny_register.ukaze_pripominky())
    last_id = zvoleny_register.zjisti_last_id()
    return render_template ('oznacit_splnena.html',
    vse_pripominky = vse_pripominky,last_id = last_id)

@app.route('/splneno', methods = ['POST'])
def splneno():
    zvoleny_register = program.otevrit_program()
    pripominka_k_oznaceni_id = request.form.get ('pripominka_k_oznaceni_id')
    zvoleny_register.splnit(int(pripominka_k_oznaceni_id))
    vse_pripominky = (zvoleny_register.ukaze_pripominky())
    volby = program.zobraz_menu()
    program.uloz_prubezne_register(zvoleny_register)
    return render_template('splneno.html', vse_pripominky = vse_pripominky,
    pripominka_k_oznaceni_id = pripominka_k_oznaceni_id, prvni_button = volby[0],
    druhy_button = volby[1], treti_button = volby[2], ctvrty_button = volby[3])

@app.route('/konec')
def konec():
    zvoleny_register = program.otevrit_program()
    program.uloz_prubezne_register(zvoleny_register)
    return render_template("konec.html")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True #automaticke nacitani zmen sablon
    app.run (debug=True)