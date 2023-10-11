def mecze():

    mecze.mecz = []
    start = (input("Podajesz mecz (TAK/NIE): ")).upper()

    if start == "TAK":
        x = (input("Podaj gospodarzy: ")).upper()
        y = (input("Podaj gości: ")).upper()
        z = x + " - " + y
        mecze.mecz.append(z)

        while x != "KONIEC" and len(mecze.mecz) >= 1:
            x = (input("Podaj gospodarzy: ")).upper()
            y = (input("Podaj gości: ")).upper()
            z = x + " - " + y
            mecze.mecz.append(z)

        if x == "KONIEC" or x == "END" or x == "q":
            mecze.mecz.pop(len(mecze.mecz) - 1)

    elif start == "NIE":
        print("TO NA HUI TU PRZYSZEDLES")

    else:
        print("HUI CI W CYCE")
