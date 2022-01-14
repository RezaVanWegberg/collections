from math import comb
import random

aces = 0
twos = 0
threes = 0

k = True
o = True

ListCijfer = ["1","2","3","4","5"]
dobbelList = []
bewaarList = []


def bord():
    print("PART 1")
    print(f"[1] ACES {aces}")
    print(f"[2] TWOS {twos}")
    print(f"[3] THREES {threes}")

def RollDobbelsteen():
    dobbelList.clear()
    for x in range(5 - len(bewaarList)):
        dobbelsteen = random.randint(1,6)
        dobbelList.append(dobbelsteen)
    print(dobbelList)

RollDobbelsteen()

for z in range (3):
    while o == True:
        NogEenKeer = input("Wilt U een dobbelsteen eruit halen? Y/N \n:")
        if NogEenKeer == "Y":
            o = False
            k = True
            while k == True:
                KeuzeInput = input("Kies uit 1, 2, 3, 4, 5 of N\n:")
                if KeuzeInput in ListCijfer:
                    bewaarList.append(dobbelList.pop(int(KeuzeInput)-1))
                    print(bewaarList)
                    print(dobbelList)
                    k = False
                    o = True
                elif KeuzeInput == "N":
                    k = False
                    o = True
                else:
                    print("error")
        elif NogEenKeer == "N":
            o = False
            combolist = dobbelList + bewaarList
            bord()
            KeuzeScore = input("Kies welke score je wilt invullen! \n:")
            if KeuzeScore == "1":
                for i in range(5):
                    if combolist[i] == "1":
                        aces += 1
        else:
            o = True
bord()
# RollDobbelsteen

print("pog")

        



