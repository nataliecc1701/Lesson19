def print_upper_words(words):
    '''takes a list of words and prints them, all uppercase, each on a separate line'''
    for word in words:
        print(word.upper())

def print_upper_e_words(words):
    '''takes a list of words and prints the ones that start with e
    all words will be printed in all UPPERCASE, each word on a separate line'''

    for word in words:
        if word.upper()[0] == "E":
            print(word.upper())

def print_upper_initial_words(words, needed_initial = None):
    '''prints the words from the provided list that start with the needed initial
    If none is provided, prints all the words. The possible initials can be presented
    as a list of chars or as a string, and are not case-sensitive'''
    
    if not needed_initial or type(needed_initial) not in [str, list]:
        print_upper_words(words)
    else:
        # format the needed_initial bit
        if type(needed_initial) == str:
            needed_initial = [x for x in needed_initial.upper()]
        elif type(needed_initial) == list:
            for i in range(len(needed_initial)):
                needed_initial[i] = needed_initial[i].upper()
        # do the thing
        for word in words:
            if word.upper()[0] in needed_initial:
                print(word.upper())