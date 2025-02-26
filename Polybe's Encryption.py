#1
def encrypt_polybe(msg):
    tab= []
    for letter in msg :
        rank = ord(letter) - ord('a')
        if rank > 8:
            rank -= 1
        colonne = rank // 5 + 1
        ligne = rank % 5 + 1
        tab.append(str(colonne))
        tab.append(str(ligne))
        test =''.join(tab)
    print(test, sep='')

text = 'hello'
encrypt_polybe(text)

#-------------------------------------------------------------------


def decrypt_polybe(cipher) :
    for x in range(0,len(cipher)-1,2) :

        row = cipher[x]
        col = cipher[x+1]
        rang = (int(row)-1)*5+(int(col)-1)
        if rang > 8:
            rang = rang + 1
        print (chr(rang + ord('a')), end ="")
decrypt_polybe('124211513415531315313115334444421151112431')
    
    