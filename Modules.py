def gissaTalet():
    import random
    nummer = random.randint(0, 100)
    while True: 
        print('Gissa ett tal mellan 0 och 100')
        gissning = int(input())
        if gissning == nummer:
            print('Du gissade rätt!, talet var', nummer)
            break
        elif gissning < nummer:
            print('Ditt tal är lägre än mitt tal, prova högre...')
        elif gissning > nummer:
            print ('Ditt tal är högre än mitt, prova lägre...')


def DelatMed():
    
        