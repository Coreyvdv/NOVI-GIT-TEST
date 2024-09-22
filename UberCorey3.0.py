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
rides = []

# Welkom statement buiten de loop, is niet nodig bij nieuwe bestelling
print('Welkom bij Uber Rides.\n')

# loop openen
while True:
    print('Kies alstublieft een van onderstaande opties:')

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

    rides.append((uber_chosen, distance, total_price))

    # user moet optie krijgen om nog een ride toe te voegen
    extra_ride = input('\nWilt u nog een rit toevoegen? [ja of nee?] ')

    if extra_ride.lower() == 'nee':
        break

print('\nU heeft',len(rides),' rit(ten) geboekt. \nUw ritten zijn:')

for ride in rides:
    print(f'*{ride[0]}, voor een afstand van {ride[1]} km en een bedrag van €{ride[2]:.2f}')

print(f'\nVoor een totaalbedrag van: €{sum(ride[2] for ride in rides):.2f}')



# Start van de loop
# while True:
#
#
#
#
#
#     # print('Je kunt kiezen uit de volgende opties:')
#     # print(f'[1]Uber_X ({prices_of_options[0][1]}/km)')
#     # print(f'[2]Uber_BLACK ({prices_of_options[1][1]}/km)')
#     # print(f'[3]Uber_VAN ({prices_of_options[2][1]}/km)')
#
# # de gebruiker moet een keuze maken uit de Uber-opties
# user_keuze = input("Welk type Uber wil je reserveren? Maak een keuze uit optie 1, 2 of 3:  ")
#
# # de gebruiker geeft aan hoeveel km lang de reis is
# user_afstand = int(input("Hoeveel km ga je reizen? "))
#
#
# if user_keuze == '1':
#     print(f'Uw Uber is geboekt. De totaalprijs voor uw reis is €{UBER_X * user_afstand}')
# elif user_keuze == '2':
#     print(f'Uw Uber is geboekt. De totaalprijs voor uw reis is €{UBER_BLACK * user_afstand}')
# elif user_keuze == '3':
#     print(f'Uw Uber is geboekt. De totaalprijs voor uw reis is €{UBER_VAN * user_afstand}')
# else:
#     print("U heeft geen geldige keuze gemaakt, start het proces aub opnieuw en voer een getal in.")
#
# print("Wilt u nog een extra rit toevoegen?")


# keuze_check = UBER_X * (user_keuze == 1) + UBER_BLACK * (user_keuze == 2) + UBER_VAN * (user_keuze == 3)
# #zonder 'if' statements gebruiken we deze manier om de juiste constante variabele te pakken op basis van de keuze van de user. !Een True is een 1 en een False is 0!
# totaal_prijs = keuze_check * user_afstand
# #de totaalprijs is de constante variabele welke gekozen is * de afstand welke ingevoerd is
# print(f'Uw Uber is geboekt. De totaalprijs voor uw reis is €{totaal_prijs}')
# #de user krijgt de totaalprijs voor zijn/haar rit te zien
