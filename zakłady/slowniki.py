from typ_zakładu import zakłady
from mecze import mecze

def zestaw():

    zestaw.zak = {}
    mecze()
    y = mecze.mecz
    zakłady()
    x = zakłady.zakladziki

    if len(x) == 1 and len(y) == 1:
        zestaw.zak[y[0]] = x[0]

    elif len(x) == len(y) and len(x) > 1:
        for i in range(len(x)):
            zestaw.zak[y[i]] = x[i]

    elif len(x) != len(y):
        print("DEBIL")
