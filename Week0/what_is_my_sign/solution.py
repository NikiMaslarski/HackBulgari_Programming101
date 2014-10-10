SIGNS = {
    ((1, 21), (2, 19)): "Aquarius",
    ((2, 20), (3, 20)): "Pisces",
    ((3, 21), (4, 20)): "Aries",
    ((4, 21), (5, 21)): "Taurus",
    ((5, 22), (6, 21)): "Gemini",
    ((6, 22), (7, 22)): "Cancer",
    ((7, 23), (8, 22)): "Leo",
    ((8, 23), (9, 23)): "Virgo",
    ((9, 24), (10, 23)): "Libra",
    ((10, 24), (11, 22)): "Scorpio",
    ((11, 23), (12, 21)): "Sagittarius",
    ((12, 22), (1, 20)): "Capricorn"
}


def what_is_my_sign(day, month):
    for key, value in SIGNS.items():
        if month == key[0][0] and day > key[0][1]:
            return value
        elif month == key[1][0] and day < key[1][1]:
            return value

