def streep():
    print("----------------------")

print("DAGEN")
streep()

#AlleDagen
print("Alle dagen")
AlleDagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
print(AlleDagen)

streep()

#WerkDagen
print("Werk dagen")
for a in range(0,5):
    print(AlleDagen[a])

streep()

#WeekendDagen
print("Weekend dagen")
for a in range(5,7):
    print(AlleDagen[a])

streep()

#Reverse
print("Reverse")
AlleDagen.reverse()
print(AlleDagen)


streep()

#ReverseWerk
print("ReverseWerk")
for a in range(2,7):
    print(AlleDagen[a])

streep()

#ReverseWeekend
print("ReverseWeekend")
for a in range(0,2):
    print(AlleDagen[a])

streep()

print("Rekenen met lists")
streep()

listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]

# print(str(listOne[a])) + " + " + print(str(listTwo[a])) + " =  " + print(str(listOne[a]))+(str(listTwo[a]))



def addAndDisplayLists():
    print("Add lists")
    for a in range(0,10):    
        print(f"{listOne[a]} + {listTwo[a]} = {listOne[a]+listTwo[a]}")

addAndDisplayLists()

def subtractAndDisplayLists():
    print("Sub list")
    for a in range(0,10):
        print(f"{listOne[a]} - {listTwo[a]} = {listOne[a]-listTwo[a]}")

subtractAndDisplayLists()

def multiplyAndDisplayLists():
    print("Sub list")
    for a in range(0,10):
        print(f"{listOne[a]} * {listTwo[a]} = {listOne[a]*listTwo[a]}")

multiplyAndDisplayLists()

def divideAndDisplayLists():
    print("Sub list")
    for a in range(0,10):
        print(f"{listOne[a]} / {listTwo[a]} = {listOne[a]/listTwo[a]}")

divideAndDisplayLists()

streep()
print("SPEL")

minimum = int(input("Wat is het minimum? :"))
maximum = int(input("Wat is het maximum? :"))

import random
RandomAantal = random.randint(minimum,maximum)
RandomNummer = random.randint(0,6)
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma():
    for x in range(RandomAantal):
        random.shuffle(spelList)
        print(spelList[RandomNummer])

spelProgramma()