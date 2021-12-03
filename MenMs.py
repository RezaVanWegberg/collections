import random

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