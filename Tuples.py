#cours 03/10

#les tuple une fois creee leurs elements ne peuvent pas etre changé 


#1.1

    
def integer_division(a, b):
    reste = a % b
    quotient = int(a / b)
    
    return quotient, reste
    

#1.2

a = int(input("Entrez a : "))
b = int(input("Entrez b (non nul) : "))

quotient, reste = integer_division(a, b)
print(f"Le quotient de la divison de {a} par {b} vaut : {quotient}")
print(f"Le reste de la divison de {a} par {b} vaut : {reste}")
  

#-----------------------------------------------------------------------------------

#2

def salutation(name) : 

    firstname, *lastname = name.split()
    return firstname

name = input("Entrez votre nom complet : ")
firstname = salutation(name)
print(f"Bonjour, {firstname} ! ")

#-------------------------------------------------------------------------------

#Question 3

import random
def game(colors, values) : 
    liste = []
    for color in colors :
        for value in values :
            carte = liste.append(f'{value} de {color}')
        return liste


colors = ('Coeur', 'Trèfle', 'Carreau', 'Pique')
values = ('7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')
print(game(colors, values))

#--------------------------------------------------------------------------------

#3.2


import random
def game_shuffle(colors, values) : 
        liste2 = []
        for color in colors :
                   for value in values :
                          carte = liste2.append(f'{value} de {color}')
        random.shuffle(liste2)
        return liste2

colors = ('Coeur', 'Trèfle', 'Carreau', 'Pique')
values = ('7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')
print(game_shuffle(colors,values))
