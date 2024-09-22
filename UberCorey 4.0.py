# We gaan een simplistische Uber applicatie maken waarbij op basis van het aantal km de prijs willen berekenen.
# uber X á 1,5eu per km
# uber Black á 2.0eu per km
# Uber Van á 3,5eu per km

# UBER_X = 1.5
# UBER_BLACK = 2.0
# UBER_VAN = 3.5

# De Uber opties worden in een lijst met tuples weergeven.
uber_options = [('UBER_X', 1.5), ('UBER_BLACK', 2.5), ('UBER_VAN', 3.5)]

# Ik wil een aantal keuzes van de user opslaan:
total_user_info = {}
price_of_all_users = 0

# Welkom statement buiten de loop, is niet nodig bij nieuwe bestelling
print('Welkom bij Uber Rides.\n')


# loop openen
while True:
    user = input('Wat is uw naam? ')
    print('Kies alstublieft een van onderstaande opties:')

    # Als de user_name nog niet gebruikt is, maak ik een nieuwe lijst voor in de dictionary zo kan ik later wél appenden aan bestaande gebruikers
    if user not in total_user_info:
        total_user_info[user] = []

# for-loop om de opties uit de uber_options list te pakken. Nummering begint bij 1
    for index, (name, price) in enumerate(uber_options, start=1):
        # user krijgt gegevens uit tuple corect weergegeven
        print(f'[{index}]{name} (€{price}/km)')
    # user moet een keuze maken uit de Ubers
    choice = int(input('\nWelke optie wilt u kiezen voor deze reis? ')) -1
    # user moet aangeven hoeveel km deze trip zal zijn
    distance = int(input('\nHoeveel km gaat u deze reis afleggen? '))

    # er worden 2 nieuwe variabelen gedefinieerd op basis van de keuze van de user
    uber_chosen, price_per_km = uber_options[choice]
    # de opgegeven afstand wordt vermenigvuldigt door de prijs per km en dan opgeslagen in variabele
    total_price = distance * price_per_km

    # ik append alle relevante info in de lijst van de eerder opgegeven user.
    total_user_info[user].append((uber_chosen, distance, total_price))

    # user moet optie krijgen om nog een ride toe te voegen
    extra_ride = input('\nWilt u, of een andere gebruiker, nog een rit toevoegen? [ja of nee] ')

    if extra_ride.lower() == 'nee':
        break


# .items om de keys en values terug te krijgen uit de dict, for loop beginnen om langs ieder user te gaan.
for user, rides in total_user_info.items():
    print(f'\nRitten van {user}:')
    #nieuwe variabele om prijs per user te berekenen, moet na elke user weer op 0 worden gezet.
    price_per_user = 0
    #de info zit in een tuple, in een lijst, in de dict. We willen bij de tuple binnen de lijst, dus we maken weer een loop.
    for ride in rides:
        #we pakken de relevante waarden uit de tuple.
        print(f'*{ride[0]}, voor een afstand van {ride[1]} km en een bedrag van €{ride[2]:.2f}')
        #totale prijs tellen we bij elkaar (alle ritten bij elkaar) en we tellen de ritten van de user bij elkaar. Na elke user wordt de price_per_user weer op 0 gezet (zie voorbeeld).
        price_of_all_users += ride[2]
        price_per_user += ride[2]
    print(f'Totaalbedrag voor {user} is €{price_per_user:.2f}')

print(f'\nTotaalbedrag van alle gebruikers is: €{price_of_all_users}')


    # for ride in rides:
    #     print(f'*{ride[0]}, voor een afstand van {ride[1]} km en een bedrag van €{ride[2]:.2f}')

# print(f'\nVoor een totaalbedrag van: €{sum(ride[2] for ride in rides):.2f}')
