twitter = open('tweets.txt', 'a')
print('Goed U te zien bij de NS')

stationsnaam = input('In welke station bent u nu:  ')
while stationsnaam == '':
    stationsnaam = input('Naam van het station:  ')

naam = input('Hoe heet u (Niet Verplicht): ')
if naam == '':
    naam = 'Anonieme twitter gebruiker'

tweet = input('Wat wil je tweeten: ')
while tweet == '':
    tweet = input('Wat wil je tweeten: ')

import datetime
x = datetime.datetime.now()

twitter.write(f'\n{tweet.capitalize()}- tweet van: {naam.capitalize()} - datum: {x.strftime("%c")}' )

print('Hartelijk bedankt voor uw feedback! ')
twitter.close()