def gissaTalet():
    import random
    nummer = random.randint(0, 100)
    rundor = 1
    while rundor < 20: 
        print('Gissa ett tal mellan 0 och 100, du har 20 försök på dig att gissa rätt, annars dör du :)')
        gissning = int(input())
        if gissning == nummer:
            print('Du gissade rätt!, talet var', nummer)
            print('Det tog dig', rundor, 'antal försök')
            break
        elif gissning < nummer:
            print('Ditt tal är lägre än talet, prova högre...')
        elif gissning > nummer:
            print ('Ditt tal är högre än talet, prova lägre...')
        rundor +=1
        if not rundor < 20:
            print('Du har använt alla dina försök, get pwned puny mortal')

def DelatMed():
    for num in range(0, 1000):
        if num%4==0 and num%8==0:
            print(num)