# Napisati regex za validaciju unešene lozinke.

# Lozinka mora sadržavati:
# Veliko slovo
# Broj
# Specijalni znak
# Biti duža od 8 znakova
import re

lozinka = 'testLO123.*'
uzorak = '(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&?*@])[A-Za-z\d!#$%&?*@]{8,}'

match = re.search(uzorak, lozinka) 

if match:
  print(match.group())
else:
  print("pattern not found")
