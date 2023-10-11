def minmax():

    min = int()
    maks = int()
    min = input("Jakie będzie MIN: ")
    maks = input("Jaki bedzie MAX: ")

    if min < maks:
        ilosc = (min, maks)

    elif min > maks:
        print("MIN > MAX")
        ilosc = "error"

    elif min == maks:
        ilosc= "Bedzie dokładnie: " + maks

    return ilosc