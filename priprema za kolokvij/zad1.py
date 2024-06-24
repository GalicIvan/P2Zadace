# Napisati program koji broji broj slova u tekstu koristeci rječnike.
# Ključevi rječnika su slova, a vrijednosti broj ponavljanja.

# Provjeriti pojavljuju li se u tekstu engleski znakovi (x, y, w) ili brojevi.

# Iz rječnika dohvatiti uređene parove slova i broj ponavljanja te iterirati kroz for petlju i ispisati.

tekst = 'Lorem ipsum dolor sit amet, consectetur axdipiscing elit. Sed commodo mi sed sollicitudin tempor. Maecenas a massa vitae ipsum rhoncus iaculis vitae sed arcu. Morbi sagittis lorem sapien, et iaculis felis semper eget. Etiam vitae pretium ante. Ut interdum mollis dolor at finibus. Nulla accumsan, elit at euismod scelerisque, mauris nunc feugiat enim, et tempus metus risus at ligula. Donec erat urna, bibendum blandit luctus vitae, porta in ipsum. Ut in fermentum nisl, sollicitudin hendrerit lectus. Praesent tristique lacus a tortor ullamcorper, eu facilisis ligula pulvinar. Etiam vitae tortor quis velit faucibus efficitur.'

dic = {}
for slovo in tekst.lower():
    dic[slovo] = dic.get(slovo, 0) + 1
    if slovo == 'x' or slovo == 'y' or slovo == 'w':
        print('x, y ili w se nalaze u tekstu.')

for key, value in dic.items():
    print(f'Slovo {key} se u tekstu nalazi {value} puta.')