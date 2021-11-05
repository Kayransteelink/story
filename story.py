import datetime
import time
def vraag1():
    print('hallo!')
    print('je gaat nu beginnen met je textbased applicatie')
    print('typ hier de naam die je wilt gebruiken voor dit varhaal')
    naam = input('')

    print(f"hallo {naam}")
    print(f"datum en tijd is {datetime.datetime.today()}")
    print(f"hoe oud is hij")
    leeftijd = input('')
    print(f"je karakter is {naam} en hij is {leeftijd} jaar oud")
    print(f'je komt thuis van school wat ga je doen A:naar je kamer om te game B:eten')
    option = input ('')
    if option.lower() == 'a':
        print('je gaat naar boven en start je computer op')
        print('je computer is opgestart wat ga je doen A:ga je samen met vrienden spelen B:ga je alleen spelen')
        computer = input('') 
        if computer.lower() == 'a':
            print('welke game ga je spelen') 
            game = input('')  
            print(f'oke je gaat nu {game} spelen met je vrienden')
            time.sleep(1)
            print('opeens komt je moeder naar boven en zegt van dat ze op het nieuws heeft gezien dat de duitsers weer gaan aanvallen')
            time.sleep(3)
            print('ze heeft gezien dat we naar een park kunnen gaan om daar opgehaald te worden door het leger en naar een veilige plek worden gebracht')
            time.sleep(3)
            print('maar je kan ook zelf kiezen om een auto te pakken en dan zelf ergens heen gaan')
            time.sleep(3)
            print('wat ga je doen A:ga je naar het park B:je gaat met de auto')
            park = input('')
            if park.lower() == 'a':
                print('je pakt een paar spullen in en loopt met je familie richting het park')
            else:
                print('je gaat met je familie de auto in')
                print('waar ga je heen')
                locatie = input
                print(f'je gaat met je familie richting {locatie}')
                print('maar ondertussen moeten jullie ook nog tanken A:ga je daar ook wat eten halen B:blijf in de auto zitten')
        else:
            print("")
    else:
        print(f'wat ga je eten')
        eten = input('')
        print(f'je eet {eten} en gaat daarna naar je kamer')
        print('je start je computer op')
        print('je computer is opgestart wat ga je doen A:ga je samen met vrienden spelen B:ga je alleen spelen')
        computer = input('') 
        if computer.lower() == 'a':
            print('welke game ga je spelen') 
            game = input('')  
            print(f'oke je gaat nu {game} spelen met je vrienden')
            time.sleep(1)
            print('opeens komt je moeder naar boven en zegt van dat ze op het nieuws heeft gezien dat de duitsers weer gaan aanvallen')
            time.sleep(3)
            print('ze heeft gezien dat we naar een park kunnen gaan om daar opgehaald te worden door het leger en naar een veilige plek worden gebracht')
            time.sleep(3)
            print('maar je kan ook zelf kiezen om een auto te pakken en dan zelf ergens heen gaan')
            time.sleep(3)
            print('wat ga je doen A:ga je naar het park B:je gaat met de auto')
            park = input('')
            if park.lower() == 'a':
                print('je pakt een paar spullen in en loopt met je familie richting het park')
            else:
                print('je gaat met je familie de auto in')
                print('waar ga je heen')
                locatie = input
                print(f'je gaat met je familie richting {locatie}')
                print('maar ondertussen moeten jullie ook nog tanken A:ga je daar ook wat eten halen B:blijf in de auto zitten')


        else:
            print('welke game ga je spelen') 
            game = input('')  
            print(f'oke je gaat nu {game} spelen')
            time.sleep(1)
            print('opeens komt je moeder naar boven en zegt van dat ze op het nieuws heeft gezien dat de duitsers weer gaan aanvallen')
            time.sleep(3)
            print('ze heeft gezien dat we naar een park kunnen gaan om daar opgehaald te worden door het leger en naar een veilige plek worden gebracht')
            time.sleep(3)
            print('maar je kan ook zelf kiezen om een auto te pakken en dan zelf ergens heen gaan')
            time.sleep(3)
            print('wat ga je doen A:ga je naar het park B:je gaat met de auto')
            park = input('')
            if park.lower() == 'a':
                print('je pakt een paar spullen in en loopt met je familie richting het park')
            else:
                print('je gaat met je familie de auto in')
                print('waar ga je heen')
                locatie = input
                print(f'je gaat met je familie richting {locatie}')
                time.sleep(2)
                print('maar ondertussen moeten jullie ook nog tanken A:ga je daar ook wat eten halen B:blijf in de auto zitten')


vraag1()

