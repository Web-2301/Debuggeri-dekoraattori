# -*- coding: utf-8 -*-
# Tiedosto: ika.py
from dateutil import relativedelta as datediff
from datetime import date,datetime
from debuggeri import debuggeri
kysely = "Anna ikäsi muodossa 1.1.1970:"

@debuggeri
def ikalaskin(syntymaaika,toinen=""):
    d1 = datetime.strptime(syntymaaika,'%d.%m.%Y').date()
    d2 = date.today()
    d = datediff.relativedelta(d2,d1)
    tulos = "{0.years} v {0.months} kk".format(d)
    print("Ikä: ",tulos)
    return tulos

def ikakysely():
    valmis = False
    ika = ""
    while not valmis:
        try:
            syntymaaika = input(kysely)
            datetime.strptime(syntymaaika,'%d.%m.%Y')
            ika = ikalaskin(syntymaaika)
            valmis = True
        except ValueError:
            print("Virhe")
        finally:
            print("Kysely on valmis, ikä on "+ika+".\n")
    return ika

# ikakysely()