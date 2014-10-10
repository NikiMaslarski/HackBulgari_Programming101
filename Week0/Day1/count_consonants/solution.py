CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def count_consonants(string):
    counter = 0
    for consonants in CONSONANTS:
        counter += string.count(consonants)
        counter += string.count(consonants.upper())
    return counter

