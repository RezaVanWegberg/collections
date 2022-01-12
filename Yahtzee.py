import random

aces = 0
twos = 0
threes = 0

dobbelList = []
bewaarList = []

def bord():
    print("PART 1")
    print(f"ACES {aces}")
    print(f"TWOS {twos}")
    print(f"THREES {threes}")

def RollDobbelsteen():
    for x in range(5):
        dobbelsteen = random.randint(1,6)
        dobbelList.append(dobbelsteen)
    print(dobbelList)

def KeuzeDobbelsteen():
    while True:
        KeuzeInput = input("Kies uit 1, 2, 3, 4 of 5 \n:")
        if KeuzeInput == "1":
            bewaarList.append(dobbelList.pop(0))
            print(bewaarList)
            print(dobbelList)
            return False
        if KeuzeInput == "2":
            bewaarList.append(dobbelList.pop(1))
            print(bewaarList)
            print(dobbelList)
            return False
        if KeuzeInput == "3":
            bewaarList.append(dobbelList.pop(2))
            print(bewaarList)
            print(dobbelList)
            return False
        if KeuzeInput == "4":
            bewaarList.append(dobbelList.pop(3))
            print(bewaarList)
            print(dobbelList)
            return False
        if KeuzeInput == "5":
            bewaarList.append(dobbelList.pop(4))
            print(bewaarList)
            print(dobbelList)
            return False
        else:
            print("Error")

RollDobbelsteen()
KeuzeDobbelsteen()



