#Scenario: je komt aan bij de bouncer van een club

naam = input("Fakka broer, wat is je naam? ")
print(f'welkom {naam}!')
print(type(naam))

leeftijd = input("Fakka wat is je leeftijd dan? ")
leeftijd = int(leeftijd)
if leeftijd < 18:
    print(f'{naam}, meen je dit? Ben je pas {leeftijd}? je mag niet naar binnen man')
elif leeftijd >= 18:
    print(f'aight {naam}, gezien je {leeftijd} bent mag je naar binnen!')
