import random


mmkleuren = ['blauw','rood']

randommm = random.choice(mmkleuren)

mmbag = {'rood':0,'blauw':0,'bruin': 0, 'geel':0, 'groen':0}

if randommm == 'rood':
    mmbag['rood'] += 1
elif randommm == 'blauw':
    mmbag['blauw'] += 1

print(mmbag)
