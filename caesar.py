import string

alphabet_string = list(string.ascii_lowercase)
count = [0 for i in range(26)]
occurrances = dict(zip(alphabet_string, count))

frequent = {'e':4, 't':19, 'a':0, 'o':13, 'i':8, 'n':14}

#ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJ RXVLJZEXRSILKVWFITVRKKRTBKYVEKIPUVTIPGKZEX ZKLJZEXRWIVHLVETPRERCPJZJRKKRTBZEJKVRU 

def crack(cipher):
    cipher = cipher.lower().replace(' ','')

    for letter in cipher:
        occurrances[letter] += 1

    top_3 = sorted(occurrances, key=occurrances.get, reverse=True)[:3]

    indices = [alphabet_string.index(top_3[i]) for i in range(len(top_3))]

    with open('output.txt', 'a') as my_file:


crack('ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJ RXVLJZEXRSILKVWFITVRKKRTBKYVEKIPUVTIPGKZEX ZKLJZEXRWIVHLVETPRERCPJZJRKKRTBZEJKVRU')
