import datetime
from datetime import date
from datetime import timedelta




class Pripominka:
    """reprezentuje pripominku v todo seznamu, pripominka muze byt splnena 1,
    nebo nesplnena 0"""
    def __init__(self,text,termin,posledni_id):
        """ Iniciuje pripominku s textem, automaticky nastavi jedinecne id
        pripominky a nesplneni podminky, termin zadavat ve formatu y,m,d """
        self.text = text
        self.id = posledni_id+1
        self.stav = 0
        self.date = datetime.date.today()
        self.termin = termin


    def splnit (self):
        """zmeni stav pripominky z nesplneno na splneno"""
        self.stav = 1

    def dnes_termin(self):
        """upozorni ze dnes je termin pripominky hlaskou 'dnes je termin'"""
        dnes = datetime.date.today()
        if dnes == self.termin:
            return True

    def doba_do_terminu (self):
        """vypocita kolik dni zbyva do konce terminu"""
        dnes = datetime.date.today()
        doba = (self.termin - dnes)
        return doba