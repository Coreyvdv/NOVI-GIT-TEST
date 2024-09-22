# De Uber opties worden in een lijst met tuples weergegeven.
uber_options = [('UBER_X', 1.5), ('UBER_BLACK', 2.5), ('UBER_VAN', 3.5)]

# Ik wil een aantal keuzes van de user opslaan:
total_user_info = {}


# Functie om het welkomstbericht weer te geven
def print_welcome():
    print('Welkom bij Uber Rides.\n')


# Functie om Uber-opties te tonen en de keuze van de gebruiker te verwerken
def get_user_info():
    user = input('Wat is uw naam? ')

    # Als de user_name nog niet gebruikt is, maak een nieuwe lijst voor in de dictionary
    if user not in total_user_info:
        total_user_info[user] = []

    print('Kies alstublieft een van onderstaande opties:')

    # for-loop om de opties uit de uber_options list te pakken. Nummering begint bij 1
    for index, (name, price) in enumerate(uber_options, start=1):
        print(f'[{index}] {name} (€{price}/km)')

    # User maakt een keuze
    choice = int(input('\nWelke optie wilt u kiezen voor deze reis? ')) - 1
    distance = int(input('\nHoeveel km gaat u deze reis afleggen? '))

    # Keuze verwerken
    uber_chosen, price_per_km = uber_options[choice]
    total_price = distance * price_per_km

    # Voeg de rit toe aan de lijst voor de gebruiker
    total_user_info[user].append((uber_chosen, distance, total_price))

    # Vraag of de gebruiker nog een rit wil toevoegen
    extra_ride = input('\nWilt u, of een andere gebruiker, nog een rit toevoegen? [ja of nee] ')
    return extra_ride.lower() != 'nee'  # Ga door als het antwoord niet 'nee' is


# Functie om de ritten per gebruiker te printen en totale kosten te berekenen
def print_user_rides():
    price_of_all_users = 0
    for user, rides in total_user_info.items():
        print(f'\nRitten van {user}:')
        price_per_user = 0
        for ride in rides:
            print(f'* {ride[0]}, voor een afstand van {ride[1]} km en een bedrag van €{ride[2]:.2f}')
            price_per_user += ride[2]
        print(f'Totaalbedrag voor {user} is €{price_per_user:.2f}')
        price_of_all_users += price_per_user

    return price_of_all_users


# Functie om de totale prijs voor alle gebruikers te berekenen
def calculate_total_price(price_of_all_users):
    print(f'\nTotaalbedrag van alle gebruikers is: €{price_of_all_users:.2f}')


# Het hoofdprogramma
if __name__ == '__main__':
    print_welcome()  # Welkomstbericht

    while True:
        continue_rides = get_user_info()  # Verwerk de keuze van de gebruiker
        if not continue_rides:
            break  # Stop de loop als de gebruiker geen extra rit wil toevoegen

    total_price = print_user_rides()  # Print ritten en bereken totale kosten per gebruiker
    calculate_total_price(total_price)  # Print totale kosten van alle gebruikers
