#2

def encryptaffine(plaintext, a=3, b=2):
    ciphertext = ''
    for letter in plaintext:

        letter_order = ord(letter) - ord('A')
        rang = (a * letter_order + b) % 26
        cipherletter = chr(rang + ord('A'))

        if letter == ' ' :
            cipherletter = ' '

        ciphertext += cipherletter
    return ciphertext

print(encryptaffine(input('Entrez le texte a encoder :'), ))

#-----------------------------------------------------------------------

#3

def decryptaffine(ciphertext, a =5, b=3):
    decrypted_text = " "
    modulo_inverse = pow(a, -1, 26)

    for char in ciphertext:
        if char.isalpha(): 
            letter_order = ord(char) - ord('A')
            decrypted_formule = (modulo_inverse * (letter_order - b)) % 26
            decrypted_char = chr(decrypted_formule + ord('A'))

        else :
            decrypted_char = char


        decrypted_text += decrypted_char
    return decrypted_text

ciphertext = "IKDEV EVRNR GX AKXLRXK LXPPDHX"
print(decryptaffine(ciphertext, a=5, b=3))