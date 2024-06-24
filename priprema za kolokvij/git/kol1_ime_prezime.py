from countries import countries
import random

finalisti = random.sample(countries, 26)

listaFinalista = []
for finalist in finalisti:
    dic = {
        'drzava': finalist[0],
        'izvodjac': finalist[1],
        'pjesma': finalist[2]
    }
    listaFinalista.append(dic)
# Nakon izbora finalista, potrebno je simulirati glasanje. Svaka država s popisa 37 drzava moze glasati.
# Nasumice se dodjeljuju se bodovi (12, 10, 8, 7, ..., 1) nekoj od država finalista.
# Drzava ne moze glasati sama za sebe. Bodove spremati u novo svojstvo rječnika "bodovi".
# Nakon glasanja ispisati pobjedničku državu - ona koja ima najvise bodova.

bodovi = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]

