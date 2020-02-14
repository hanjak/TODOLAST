from pripominka import Pripominka
from register import Register

import pickle

class Program:
    """spousti program a zajistuje jeho chod"""
    def otevrit_program (self):
        """nacte todosoubor z pameti"""
        pickle_otevrit = open("todosoubor","rb")
        reg = pickle.load(pickle_otevrit)
        pickle_otevrit.close()
        return reg

    def uloz_prubezne_register (self, reg):
        pickle_uloz = open ("todosoubor","wb")
        pickle.dump(reg,pickle_uloz)
        pickle_uloz.close()


    def zobraz_menu(self):
        volba_1 = "Ukaz vsechny pripominky"
        volba_2 = "Zadej novou pripominku"
        volba_3 = "oznac pripominku jako splnenou"
        volba_4 = "konec"
        return volba_1, volba_2,volba_3,volba_4