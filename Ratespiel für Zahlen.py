import random
# Test für GitHub

def zahlen_raten():
    durchgang = 1
    aktiv = True
    zufalls_zahl = random.randint(0, 100)

    while aktiv:
        print()
        print('Sie befinden sich in Versuch Nr.', durchgang)
        durchgang = durchgang + 1
        eingabe = input('Bitte eine Zahl eingeben (um abzubrechen "Ende" eingeben):')

        if eingabe == 'Ende':
            aktiv = False
        elif durchgang == 8:
            print('Sie haben leider keine Versuche mehr! - Verloren!!!')
            print('Die gesuchte Zahl war', zufalls_zahl)
            aktiv = False
        else:
            eingabe = int(eingabe)
            if zufalls_zahl < eingabe and durchgang < 7:
                print('Die gesuchte Zahl ist kleiner')
            elif zufalls_zahl > eingabe and durchgang < 7:
                print('Die gesuchte Zahl ist größer')
            elif eingabe == zufalls_zahl:
                print('Sie haben die Zahl richtig erraten! Herzlichen Glückwunsch!!! ')
                aktiv = False
            elif durchgang == 7 and eingabe > zufalls_zahl:
                print('LETZTER VERSUCH!!!')
                print('Die gesuchte Zahl ist kleiner')
            elif durchgang == 7 and eingabe < zufalls_zahl:
                print('LETZTER VERSUCH!!!')
                print('Die gesuchte Zahl ist größer')


zahlen_raten()
