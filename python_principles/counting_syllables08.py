# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method



# using split


def count(word):
    return len(word.split("-"))


# #Burayi değistirdim