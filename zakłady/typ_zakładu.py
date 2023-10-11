from zaklad_i_co import decyzja

def zakłady():

    mozliwosci = ["ZOLTE KARTKI", "KTO WYGRA", "BRAMKI", "FAULE", "ROZNE", "KTO STRZELI"]
    zakłady.zakladziki = []
    start = (input("Podajesz zakład (TAK/NIE): ")).upper()

    if start == "TAK":
        decyzja(mozliwosci,zakłady.zakladziki)

        while zakłady.zakladziki[len(zakłady.zakladziki)-1] != "KONIEC" and len(zakłady.zakladziki) >= 1:
            decyzja(mozliwosci,zakłady.zakladziki)

        if zakłady.zakladziki[len(zakłady.zakladziki)-1] == "KONIEC":
            zakłady.zakladziki.pop(len(zakłady.zakladziki) - 1)
            return zakłady.zakladziki

    elif start == "NIE":
        print("WYPIERDALAJ")

    else:
        print("HUI CI W CYCE")