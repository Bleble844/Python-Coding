#1

import math

def encrypt_transpo(plaintext, transpo):
    plaintext = plaintext.replace(" ", "")
    
    num_col = len(transpo)
    num_ligne = math.ceil(len(plaintext) / num_col)
    
    while len(plaintext) < num_ligne * num_col:
        plaintext += 'X'
    
    grid = []
    for i in range(num_ligne):
        row = []
        for j in range(num_col):
            row.append(plaintext[i * num_col + j])
        grid.append(row)

    ciphertext = ""
    for col in transpo:
        for ligne in range(num_ligne):
            if col - 1 < len(grid[ligne]):
                ciphertext += grid[ligne][col - 1]
    
    return ciphertext

plaintext = "MESSAGE SUPER SECRET"
transpo = [3, 4, 2, 1]
print(encrypt_transpo(plaintext, transpo))  # SEECXSSRRXEGPETMAUSE


#---------------------------------------------------------------------------------------------

def decrypt_transpo(ciphertext, transpo):
    num_col = len(transpo)
    num_ligne = math.ceil(len(ciphertext) / num_col)
    
    inverse_transpo = [0] * num_col
    for i, col in enumerate(transpo):
        inverse_transpo[col - 1] = i + 1
    
    grid = [[''] * num_col for _ in range(num_ligne)]
    index = 0
    for col in transpo:
        for ligne in range(num_ligne):
            grid[ligne][col - 1] = ciphertext[index]
            index += 1
    

    plaintext = ""
    for ligne in grid:
        plaintext += "".join(ligne)
    
    return plaintext.strip('X')


encrypted_text = "ICNIMEXVEECRTSELODFEUONUHERITAREFNS"
transpo_key = [5, 3, 1, 4, 2]
print(decrypt_transpo(encrypted_text, transpo_key))

#----------------------------------------------------------------------

#3. L'indice de coicidence est presque identique car cette methode de chiffrement
# est basé sur le fait de changer l'emplacement des lettre sur une matrice avec
# des lignes et colonnes, la seule chose qui change est le fait qu'on rajoute 
# des X pour remplacer les espaces entre les mots.