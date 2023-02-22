import pandas as pd
import cable as cb
import random

def callai():
    df = pd.read_csv('Interdimensional Cable Chat GPT lists - Characters (2).csv')

    guest_stars = df['Guest Stars']
    settings = df['Settings']
    situations = df['Situations']

    setting = settings[random.randint(0, settings.count())]
    situation = situations[random.randint(0, situations.count())]

    new_situation = situation.replace("<character1>", guest_stars[random.randint(0, guest_stars.count())])
    situation = new_situation.replace("<character2>", guest_stars[random.randint(0, guest_stars.count())])

    if "<character3>" in situation:
        situation = situation.replace("<character3>", guest_stars[random.randint(0, guest_stars.count())])


    situation = situation.replace("<setting>", setting)

    cb.Cable().generate(situation)

print(callai())    
