import string

alphabet_string = list(string.ascii_lowercase)

#ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJ RXVLJZEXRSILKVWFITVRKKRTBKYVEKIPUVTIPGKZEX ZKLJZEXRWIVHLVETPRERCPJZJRKKRTBZEJKVRU 

def crack(cipher):
    cipher = cipher.lower().replace(' ','')
    with open("output.txt", "a") as myfile:
        for i in range(25):
            for letter in cipher:
                myfile.write(alphabet_string[alphabet_string.index(letter) - i].upper())
            myfile.write('\n')


crack('ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJ RXVLJZEXRSILKVWFITVRKKRTBKYVEKIPUVTIPGKZEX ZKLJZEXRWIVHLVETPRERCPJZJRKKRTBZEJKVRU')