# Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
# Nakon toga napisati regex za provjeru eduId koji 
# mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena+ prezime.
# X predstavlja bilo koji broj (moze ici u beskonacnost),
# a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
# Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

import re

unos = input('Unesite e-mail adresu: ')
eduId = input('Unesite eduId adresu: ')

uzorak = '^[a-zA-Z]+\.[a-zA-Z]+\d*@fpmoz\.sum\.ba$'
eduIdUzorak = '^[a-zA-Z][a-zA-Z]+\d*@sum\.ba$'
match = re.search(uzorak, unos)
match2 = re.search(eduIdUzorak, eduId)

if match and match2:
  print(match.group())
  print(match2.group())
  print('Uspjesna prijava!')
else:
  print("Pattern not found")