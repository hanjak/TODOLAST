from pripominka import Pripominka
import pickle
import datetime
from datetime import date
class Register:
    """Reprezentuje register pripominek, pripominky mohou byt nesplneny nebo
    splneny"""

    def __init__ (self):
        """initializuje prazdny register"""
        self.pripominky = []

    def nova_pripominka (self,text,termin,posledni_id):
        """Vytvori novou pripominku a prida ji do registru"""
        self.pripominky.append(Pripominka(text, termin,posledni_id))

    def zadej_pripominku (self):
        """ zepta se uzivatele na text a termin pripominky a vyvtvori novou
        pripominku"""
        pripominka_text = input ("zadej text pripominky:")
#tady kontroluju aby termin pripominky byl ve spravnem tvaru a sel predelat
#do formatu datetime - mozna existuje nejaky jednodussi zpusob?
        while True:
            try:
                pripominka_den_rok =int(input("zadej deadline pripominky -rok: "))
            except ValueError:
                print ("rok musi byt cislo")
            else:
                if pripominka_den_rok <2019:
                    print ("pripominka musi mit deadline v roce 2019 nebo vic")
                else:
                    break
        while True:
            try:
                pripominka_den_mesic = int(input("mesic: "))
            except ValueError:
                print ("mesic musi byt cislo od 1 do 12")
            else:
                if pripominka_den_mesic <1 or pripominka_den_mesic>12:
                    print ("mesic musi byt cislo od 1 do 12")
                else:
                    break
        while True:
            try:
                pripominka_den_den= int(input("den: "))
            except ValueError:
                print ("den musi byt cislo od 1 do 31")
            else:
                if pripominka_den_den <1 or pripominka_den_den >31:
                    print ("den musi byt cislo od 1 do 31")
                else:
                    break
        pripominka_den =datetime.date(pripominka_den_rok,pripominka_den_mesic,
        pripominka_den_den)
        last_id = self.zjisti_last_id()
        self.nova_pripominka(pripominka_text,pripominka_den,last_id)

    def ukaze_pripominky (self):
        """ukaze vsechny pripominky v seznamu, text a stav"""
        seznam_pripominek = []
        for pripominka in self.pripominky:
            seznam_pripominek.append ( (pripominka.text, "stav:", pripominka.stav,"id:",pripominka.id,
             "deadline:",pripominka.termin, "datum zadani:", pripominka.date))
        return seznam_pripominek

    def splnit(self,id_pripominky_pro_splneni):
        for pripominka in self.pripominky:
            if pripominka.id == id_pripominky_pro_splneni:
                pripominka.splnit()

    def splnit_pro_cmd(self):
        """zepta se jakou pripominku chci splnit a oznaci ji jako splnenou"""
        #tady otazka - jakou datovou strukturu, abych mohla pouzit indexovani
        #ikdyz pripominku smazu  - viz splnit s indexem nize
        while True:
            try:
                id_pripominky_pro_splneni = int(input
                ("zadejte id pripominky kterou chcete splnit: "))
            except ValueError:
                print ("musi byt cislo")
            else:
                seznam_id = []
                for pripominka in self.pripominky:
                    if pripominka.id == id_pripominky_pro_splneni:
                        pripominka.splnit()
                        #abych zjistila, jestli se opravdu neco deje / lze jinak
                        #zjisti jestli akce probehla?
                        seznam_id.append(id_pripominky_pro_splneni)
                if seznam_id:
                    break
                else:
                    print ("id musi byt existujici id")


    def splnit_s_indexem(self):
        """zepta se jakou pripominku chci splnit a oznaci ji jako splnenou"""
        while True:
            try:
                id_pripominky_pro_splneni = int(input
                ("zadejte id pripominky kterou chcete splnit: "))
            except ValueError:
                print ("musi byt cislo")
            else:
                if self.zjisti_last_id() < id_pripominky_pro_splneni or id_pripominky_pro_splneni<1:
                    print("je nutne zadat platne id")
                else:
                    break
        self.pripominky[id_pripominky_pro_splneni - 1].splnit()


    def kontrola_termin(self):
        """zkontroluje seznam pripominek, zda nektera dnes nema termin"""
        for pripominka in self.pripominky:
            if pripominka.dnes_termin() == True:
                print (pripominka.text, "ma dnes termin")

    def pripomenuti (self):
        """pripomene pripominky ktere maji tyden den do terminu a napise kolik
        zbyva do terminu"""
        for pripominka in self.pripominky:
            dnes = date.today()
            za_tyden = dnes + timedelta (days = 7)
            if termin < za_tyden:
                print ("pripominka", pripominka.id, "zbyva",
                termin - dnes, "do terminu")

    def zjisti_last_id (self):
        """zjisti jake je nejvyssi id pouzite v seznamu aby mohla indexace
        poznamek pokracovat dal"""
        pocet_zaznamu = len(self.pripominky)
        return self.pripominky[pocet_zaznamu - 1].id