def hajs():

    hajs.kwoty = []
    start = (input("Podajesz kwoty (TAK/NIE): ")).upper()

    if start == "TAK":
        x = (input("Podaj kwote: ")).upper()
        hajs.kwoty.append(x)

        while x != "KONIEC" and len(hajs.kwoty) >= 1:
            x = (input("Podaj kwote: ")).upper()
            hajs.kwoty.append(x)

        if x == "KONIEC" or x == "END" or x == "q":
            hajs.kwoty.pop(len(hajs.kwoty) - 1)

    elif start == "NIE":
        print("idź w hui")

    else:
        print("no nie tak, nie tak deklu")