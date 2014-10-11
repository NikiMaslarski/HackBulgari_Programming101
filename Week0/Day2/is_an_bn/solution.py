import re


def is_an_bn(word):
    return word.count('a') == word.count('b') and \
        bool(re.match(r'a*b*$', word))

