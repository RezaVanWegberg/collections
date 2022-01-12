from abc import abstractmethod
import random
from typing import Text, ValuesView
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

WitteDobbelSteenNummer = [1,1,1,2,2,3]
RedScoreBord = [-2," "," "," "," "," "," "," "," "," ",]
BluescoreBord = [" "," "," "," "," "," "," "," "," ",-2,]
WhiteBord = [" "," "," "," "," "]
RoodOfBlauw = 0
count = 0

Nmrs = [1,2,3,4,5,6,7,8,9,10]


def AlleDobbelstenen():
    global BlauwPlusRoodPlusWit
    global BlauwPlusRoodMinWit
    global BlauwPlusRood
    global HoogsteMinLaagste
    WitteDobbelSteen = random.choice(WitteDobbelSteenNummer)
    print(f"Wit: {WitteDobbelSteen}")

    RodeDobbelSteen = random.randint(1,6)
    print(f"Rood: {RodeDobbelSteen}")

    BlauweDobbelSteen = random.randint(1,6)
    print(f"Blauw: {BlauweDobbelSteen}")

    BlauwPlusRoodPlusWit = BlauweDobbelSteen+RodeDobbelSteen+WitteDobbelSteen
    print(f"A: {BlauwPlusRoodPlusWit}")

    BlauwPlusRoodMinWit = BlauweDobbelSteen+RodeDobbelSteen-WitteDobbelSteen
    print(f"B: {BlauwPlusRoodMinWit}")

    BlauwPlusRood = BlauweDobbelSteen+RodeDobbelSteen
    print(f"C: {BlauwPlusRood}")

    DobbelList = [RodeDobbelSteen,BlauweDobbelSteen,WitteDobbelSteen]
    HoogsteDobbel = max(DobbelList)
    LaagsteDobbel = min(DobbelList)
    HoogsteMinLaagste = HoogsteDobbel - LaagsteDobbel
    print(f"D: {HoogsteMinLaagste}")

    print("Als C of D wordt gekozen wordt de score bij de het witte score bord toegevoegd \n")
    if  (RoodOfBlauw / 2) == 0:
        print("Je moet nu bij rood gaan invullen\n")
    else:
        print("Je moet nu bij blauw gaan invullen\n")

def ScoreBord():
    print(Back.RED + str(RedScoreBord))
    print(Back.BLUE + str(BluescoreBord))
    print("          " + Back.WHITE + str(WhiteBord))

def Keuze():
    while True:
        global KeuzeIn
        KeuzeIn = input("Kies uit A, B, C, D :")
        if KeuzeIn == "A":
            KeuzeIn = BlauwPlusRoodPlusWit
            Positie()
            break
        elif KeuzeIn == "B":
            KeuzeIn = BlauwPlusRoodMinWit
            Positie()
            break
        elif KeuzeIn == "C":
            KeuzeIn = BlauwPlusRood
            Positie()
            break
        elif KeuzeIn == "D":
            KeuzeIn = HoogsteMinLaagste
            Positie()
            break
        else:
            print("Een hoofdletter alstublieft")


def Check(list1,value):
    global count
    for i in list1:
        if i == " ":
            i = 0
        if value > int(i):
            count = count + 1        



def Positie():
    global RoodOfBlauw
    global count
    global PositieIn
    while True:
        if  (RoodOfBlauw / 2) == 0:
            while True:
                PositieIn = int(input("Kies de positie van het getal :")) #rood
                Check(RedScoreBord,KeuzeIn)
                if count > 0:
                    RedScoreBord[PositieIn-1] = KeuzeIn
                    RoodOfBlauw = 1
                    count = 0
                    break
                else:
                    print("error opnieuw")
            break
        else:
            PositieIn = int(input("Kies de positie van het getal. (1 t/m 9) :")) #blauw
            Check(BluescoreBord,KeuzeIn)
            if count > 0:
                BluescoreBord[PositieIn-1] = KeuzeIn
                RoodOfBlauw = 0
                count = 0
                break
            break



def Game():
    AlleDobbelstenen()
    ScoreBord()
    Keuze()
    ScoreBord

for x in range(5):
    Game()