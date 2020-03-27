#This is a Python project that
#lets you play hangman in a 
#textual interface. I made 
#this project to deepen my 
#understanding of Python.
#
# - Grant Shanklin




import random

def clear():
    print(" \n"*10)

def draw_stand():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" | \n"*8, "|")
    print(" |")
    print(" |","_"*10)

def draw_stand_1():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |         |____|  ")
    print(" | \n"*6, "|")
    print(" |")
    print(" |","_"*10)

def draw_stand_2():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |         |____|  ")
    print(" |           |")
    print(" |           |")
    print(" |           |")
    print(" |           |")
    print(" | \n"*2, "|")
    print(" |")
    print(" |","_"*10) 

def draw_stand_3():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |    \    |____| ")
    print(" |     \     | ")
    print(" |      \____|")
    print(" |           |")
    print(" |           |")
    print(" | \n"*2, "|")
    print(" |")
    print(" |","_"*10)

def draw_stand_4():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |    \    |____|   / ")
    print(" |     \     |     / ")
    print(" |      \____|____/ ")
    print(" |           |")
    print(" |           |")
    print(" | \n"*2, "|")
    print(" |")
    print(" |","_"*10) 

def draw_stand_5():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |    \    |____|   / ")
    print(" |     \     |     / ")
    print(" |      \____|____/ ")
    print(" |           |")
    print(" |           |")
    print(" |          /")
    print(" |         /")
    print(" |        /")
    print(" |       /")
    print(" |","_"*10)

def draw_stand_6():
    print("")
    print(" |-----------")
    print(" |           |")
    print(" |           |")
    print(" |         __|__    ")
    print(" |         |    | ")
    print(" |    \    |____|   / ")
    print(" |     \     |     / ")
    print(" |      \____|____/ ")
    print(" |           |")
    print(" |           |")
    print(" |          / \ ")
    print(" |         /   \ ")
    print(" |        /     \ ")
    print(" |       /       \ ")
    print(" |","_"*10)

word_list = ["bagpipes", "banjo", "bungler", "croquet", "crypt", "dwarves", "fervid", "fish", "fjord"]
word = random.choice(word_list)
def split(word): 
    return list(word)
letters_in_word = split(word)

used_letters = []
used_letters_string = " "
number_of_correct_letters = 0
number_of_incorrect_letters = 0
correct_guess = 2
position = []
reused_letter = 0
while number_of_correct_letters < len(word) and number_of_incorrect_letters < 6:
    clear()
    if number_of_incorrect_letters == 0:
        draw_stand()
    elif number_of_incorrect_letters == 1:
        draw_stand_1()
    elif number_of_incorrect_letters == 2:
        draw_stand_2()
    elif number_of_incorrect_letters == 3:
        draw_stand_3()
    elif number_of_incorrect_letters == 4:
        draw_stand_4()
    elif number_of_incorrect_letters == 5:
        draw_stand_5()
    elif number_of_incorrect_letters == 6:
        draw_stand_6()
    print(" \n The blanks for your word:   ", end =" ")
    index = 0
    for i in letters_in_word:
        if index in position:
            print(letters_in_word[index], end=" ")
        else:
            print("_ ", end =" ")
        index += 1
    print("\n")
    if correct_guess == 1:
        print("Your guess is correct")
    elif correct_guess == 0:
        print("Your guess is incorrect")
    elif reused_letter == 1:
        print("You already used that letter, try again")
    elif correct_guess == 2:
        print("Welcome to Hangman \n")
    print("Used letters: ", used_letters)
    guessed_letter = input("Guess a letter:  ")
    correct_guess = 0
    reused_letter = 0
    if guessed_letter not in used_letters:
        for letter in  letters_in_word:
            if guessed_letter == letter:
                correct_guess = 1
                correct_letter = letter
                position.append(letters_in_word.index(correct_letter))
                position.sort()
        if correct_guess == 1:
            number_of_correct_letters += 1
        else:
            number_of_incorrect_letters += 1
    elif guessed_letter in used_letters:
        reused_letter = 1
    used_letters.append(guessed_letter)
    
if number_of_incorrect_letters == 6:
    clear()
    draw_stand_6()
    print("YOU LOSE :( ")
if number_of_correct_letters == len(word):
    clear()
    print("YOU WIN!!!!!    :)  ")
    print("\n "*4)


