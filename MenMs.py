import random

def streep():
    print("-----------------------------------")

Kleuren = ["oranje", "blauw", "groen", "bruin"]
Zak = []

Aantal = int(input("Hoeveel M&Ms moeten er in de zak worden toegevoegd? :"))
RandomNummer = random.randint(0,3)

def ZakMM():
    for x in range(Aantal):
        random.shuffle(Kleuren)
        Zak.append(Kleuren[1])
    print(Zak)
    print(f"Aantal = {Aantal}")

ZakMM()
streep()

ZakD = {"oranje":0, "blauw":0, "groen":0, "bruin":0}

def ZakMMD():
    for y in range(Aantal):
        random.shuffle(Kleuren)
        if Kleuren[1] == "oranje":
            ZakD["oranje"] += 1 
        elif Kleuren[1] == "blauw":
            ZakD["blauw"] += 1 
        elif Kleuren[1] == "groen":
            ZakD["groen"] += 1 
        elif Kleuren[1] == "bruin":
            ZakD["bruin"] += 1   
    print(ZakD)
    print(f"Aantal = {Aantal}")

ZakMMD()