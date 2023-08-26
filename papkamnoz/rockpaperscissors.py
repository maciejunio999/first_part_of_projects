from random import randint

choose = ''
while choose != 4:
    print("To end playing write '4'")
    choose = int(input("Rock - 1, Paper - 2, Scissors - 3\nChoose:"))
    PC = randint(1,3)
    if choose == PC:
        print("Tie\ngo on")
    elif (choose == 1 and PC == 2) or (choose == 2 and PC == 3) or (choose == 3 and PC == 1):
        print("PC won")
    else:
        print("You won")
