# Tiedosto: ika.py
from dateutil import relativedelta as datediff
from datetime import date,datetime
from debuggeri import debuggeri
kysely = "Anna syntymäaikasi muodossa 1.1.1970: "

@debuggeri
def ikalaskin(syntymaaika,toinen=""):
    d1 = datetime.strptime(syntymaaika,'%d.%m.%Y').date()
    d2 = date.today()
    d = datediff.relativedelta(d2,d1)
    # tulos = "{0.years} v {0.months} kk {0.days} pv".format(d)
    tulos = f"{d.years} v {d.months} kk {d.days} pv"
    print("Ikä: ",tulos)
    return tulos

@debuggeri
def ikakysely():
    valmis = False
    virhe = False
    ika = ""
    while not valmis:
        try:
            syntymaaika = input(kysely)
            datetime.strptime(syntymaaika,'%d.%m.%Y')
            ika = ikalaskin(syntymaaika)
            valmis = True
        except ValueError:
            print("Virhe")
            virhe = True
        # finally:
        #    if virhe:
        #        print(f"Kysely päättyi virheeseen.")
        #    else:
        #        print("Kysely on valmis, ikä on "+ika+".\n")
        else:
            print("Kysely on valmis, ikä on "+ika+".\n")
    return ika

# ikakysely()