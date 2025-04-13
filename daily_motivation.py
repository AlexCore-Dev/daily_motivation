import random
from datetime import datetime

def nev_beker():
    return input('Add meg a neved: ')

def random_motivacio(motiv):
    idopont = datetime.now()
    keszlet = ["ma egy nagyszerű nap lesz!", 
               "ne add fel, menni fog!", "büszke lehetsz magadra!", 
               "csak így tovább!", 
               "többre vagy képes, mint hinnéd!"]
    valasztas = random.choice(keszlet)
    szoveg = (f'{idopont.strftime("%H:%M:%S")} - {motiv}, {valasztas}')
    print(szoveg)

    with open(r'C:\Users\csisz\OneDrive\Dokumentumok\motivacio.txt', 'a', encoding='utf-8') as fajl:fajl.write(szoveg + "\n")

def main():
    while True:
        neved = nev_beker()
        if neved == 'q':
            print('Kilepes...')
            break
        else:
            random_motivacio(neved)

main()