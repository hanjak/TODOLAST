
from pripominka import Pripominka
import datetime
import pickle
from register import Register

from program import Program
program = Program()

pripominka1 = Pripominka ("zkouska",datetime.date.today(),0)
reg = Register()
reg.nova_pripominka(pripominka1.text,pripominka1.termin,pripominka1.id)

filename = 'todosoubor'
outfile = open (filename,'wb')
pickle.dump(reg,outfile)
outfile.close()

filename = 'todosoubor'
pickle_otevrit = open(filename, 'rb')
data = pickle.load(pickle_otevrit)
print (data)