import pandas as pd
import cable as cb
import random
import imagecrawl as ic

def callai():
    df = pd.read_csv('Interdimensional Cable Chat GPT lists - Characters (3).csv')

    keywords = []


    guest_stars = df['Guest Stars']
    settings = df['Settings']
    situations = df['Situations']

    setting = settings[random.randint(0, settings.count())]
    situation = situations[random.randint(0, situations.count())]



    if "<character>" in situation:
        character = guest_stars[random.randint(0, guest_stars.count())]
        situation = situation.replace("<character>", character)
        keywords.append(character)

    if "<character1>" in situation:       
        character1 = guest_stars[random.randint(0, guest_stars.count())]
        situation = situation.replace("<character1>", character1)
        keywords.append(character1)
    
    if "<character2>" in situation:
        character2 = guest_stars[random.randint(0, guest_stars.count())]
        situation = situation.replace("<character2>", character2)
        keywords.append(character2)

    if "<character3>" in situation:
        character3 = guest_stars[random.randint(0, guest_stars.count())]
        situation = situation.replace("<character3>", character3)
        keywords.append(character3)

    if "<setting>" in situation:
        situation = situation.replace("<setting>", setting)
        keywords.append(setting)

    if "<setting1>" in situation:
        setting1 = settings[random.randint(0, settings.count())]
        situation = situation.replace("<setting1>", setting1)
        keywords.append(setting1)

    if "<setting2>" in situation:
        setting2 = settings[random.randint(0, settings.count())]
        situation = situation.replace("<setting2>", setting2)
        keywords.append(setting2)


    
    print(keywords)
    ic.crawl(keywords)

    script = cb.generate(situation)
    #print(script)
    return script



