
from math import sqrt
import string

#1

list = [0 for i in range(8)]
print(list)

#--------------------------------------------------------------------------

#2

numberlist = [4, 9, 25, -2]
numberlist2 = [sqrt(n) for n in numberlist if n >= 0]
print(numberlist2)

#--------------------------------------------------------------------------

#3

words = ['ovarb', 'neib', 'sirpmoc', 'sel', 'setsil', 'ne', 'noisnehérpmoc', ');']
invers = [word[::-1] for word in words]
print(invers)

#-----------------------------------------------------------------------------

#4

import string

alphabet = "&'(-_)=+°~#{[|`\^@]}$¿*?!"
mots = "HELLO WORLD"
dico = {mot : sym for mot, sym in zip(string.ascii_uppercase, alphabet)}
dico[' '] = ' '
trad = [dico[i] for i in mots[:]]
print(trad)