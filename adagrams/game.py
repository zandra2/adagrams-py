import random


def draw_letters():
    LETTER_POOL = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1
    }
    #making an array of all the tiles
    letters = []
    for key, value in LETTER_POOL.items():
        for num in range(0, value):
            letters.append(key)

    #scrambling the tiles and return the first 10
    random.shuffle(letters)
    return letters[0:10]


def uses_available_letters(word, letter_bank):

    #count the letters in letter_bank 
    new_dict = {}
    for char in letter_bank:
        if char not in new_dict:
            new_dict[char] = 1
        else:
            new_dict[char] += 1

    #checking to see if letter is in letter_bank
    for letter in word:
        if letter not in new_dict:
            return False
        elif new_dict[letter] == 0:
            return False
        else:   #remove a tile if already used
            new_dict[letter] -= 1

    return True

def score_word(word):
    POINT_VALUES = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P:": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    #calculate the total points for each letter
    sum = 0
    for letter in word:
        sum += POINT_VALUES[letter]

    return sum


def get_highest_word_score(word_list):
    pass
