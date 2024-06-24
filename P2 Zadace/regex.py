import re

# U sportu, na primjer u kosarci mozemo koristiti regex za prepoznavanje nekih patterna u podacima utakmica

data = '''
Player: Mike James | Team: Monaco
Player: Shane Larkin | Team: Efes
Player: Nikola Mirotic | Team: Milano
Player: Nemanja Nedovic | Team: Partizan
'''

pattern = r'Player: (\w+\s\w+) \| Team: (\w+)'

guess = re.findall(pattern, data)

counter = len(guess)

print(f'You had 4 players in data and I found {counter} matches.')