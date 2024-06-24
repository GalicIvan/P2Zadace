# Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi dostavljanjem.
# Generirati 15 radnika random imena i prezimena iz ponuđene liste,
# te njegovu satnicu slučajnim odabirom floata između 4 i 6 zaokruženu na 2 decimale.
# Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika 
# {“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
# Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati”
# koji generira cijeli broj odrađenih sati u 1 tjednu od 20 do 30.
# Nakon toga napraviti obračun množenjem satnice sa tjednim satima i rezultate spremiti u listu tuple-a
# (trojki) oblika (ime, prezime, isplata).
# Iteriranjem ispisati podatke, a zatim izračunati ukupnu i prosječnu isplatu za taj tjedan.
# Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.
import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']
listaRadnika = []

for i in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.randint(4, 6), 2)

    rjecnik = {}
    rjecnik['ime'] = ime
    rjecnik['prezime'] = prezime
    rjecnik['satnica'] = satnica
    listaRadnika.append(rjecnik)

listaTrojki = []
for radnik in listaRadnika:
    tjedni_sati = random.randint(20, 30)
    radnik['tjedni_sati'] = tjedni_sati

    obracun = radnik['satnica'] * tjedni_sati
    trojka = (radnik['ime'], radnik['prezime'], obracun)
    listaTrojki.append(trojka)

ukupnePlace = 0
for element in listaTrojki:
    ukupnePlace += element[2]
    print(f'Ime i prezime radnika: {element[0]} {element[1]} | Isplata: {element[2]}')
print(f'Ukupna plaća za ovaj tjedan je: {ukupnePlace}')
prosjecnaPlaca = round(ukupnePlace / len(listaTrojki))
print(f'Prosječna plaća za ovaj tjedan je: {prosjecnaPlaca}')

for covjek in listaTrojki:
    if covjek[2] > prosjecnaPlaca:
        print(f'Radnik sa većom plaćom od prosječne je: {covjek[0]} {covjek[1]}, a plaća mu je {covjek[2]}')