from minmax import minmax

def decyzja(z,x):

    decyzja.zakład = (input("Podaj zakład z podanych (" + str(z) + "): ")).upper()

    if decyzja.zakład == z[0]:
        a = minmax()
        x.append((decyzja.zakład, a))

    elif decyzja.zakład == z[1]:
        wygra = input("PIERWSZA/DRUGA: ")
        x.append((decyzja.zakład, "WYGRA: " + wygra))

    elif decyzja.zakład == z[2]:
        b = minmax()
        x.append((decyzja.zakład, b))

    elif decyzja.zakład == z[3]:
        c = minmax()
        x.append((decyzja.zakład, c))

    elif decyzja.zakład == z[4]:
        d = minmax()
        x.append((decyzja.zakład, d))

    elif decyzja.zakład == z[5]:
        a = input("Strzeli PIERWSZA/DRUGA: ")
        x.append((decyzja.zakład, a))

    elif decyzja.zakład == "KONIEC":
        x.append("KONIEC")

    else:
        print("GLUPI JESTES")