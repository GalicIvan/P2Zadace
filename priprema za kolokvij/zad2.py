# Generiraj niz od 5 imena i 5 prezimena i 5 godina te ih konvertiraj ih u uređeni par ime, prezime, godina.
# Datoteke
# Rezultat spremiti u datoteku u obliku
# ime,prezime,godina
# ime2, prezime2, godina2

listaImena = ['Ivan', 'Matej', 'Marko', 'Luca', 'Josip']
listaPrezimena = ['Galic', 'Cavar', 'Suton', 'Barac', 'Masic']
listaGodina = [19, 25, 45, 20, 25]

with open("podaci.csv", "w") as file:
    file.write("ime,prezime,godina\n")
    for ime, prezime, godina in zip(listaImena, listaPrezimena, listaGodina):
        file.write(f"{ime},{prezime},{godina}\n")