VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

def count_vowels(string):
    counter = 0
    for vowel in VOWELS:
        counter += string.count(vowel)
        counter += string.count(vowel.upper())
    return counter

