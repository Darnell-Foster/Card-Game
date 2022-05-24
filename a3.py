#Darnell Foster 101229310

import random
import re
from turtle import up
from unicodedata import category

def create_deck():
    """ Takes no parameter
        Returns a 2D-list """
    
    # an intially empty deck
    deck = []
    suits = ["SP", "CL", "HR", "DM"]
    faces = []
    
    # creates a list of all face values
    for x in range(2,10):
        faces.append(x)
    # faces = [x for x in range(2,10)] # an alternative technique - list comprehension 
    
    # creates cards [s,f] and inserting them to the deck
    for s in suits:
        for f in faces:
            deck.append([s, f])
    return deck

def shuffle(deck):
    """Takes a 2D-list
        Returns a shuffled 2D-list"""
    
    # copies the deck, so the original deck remains same    
    sdeck = deck[:]
    random.shuffle(sdeck)
    return sdeck

## ---- add the rest of the required functions here ----##
## ---- you must add a docstring to your functions ----##
def deal(sdeck):
    """ Takes a shuffle 2d list
        Returns a 3D-list of 9 elements """
    
    #Initialize 2d-list with 3 elements
    ddeck = [[],[],[]] #[row][card/column][suit,face]

    #populates each element(3) with 3 elements each from the shuffled deck and removes them
    for i in range(3):
        for j in range (3):
            ddeck[i].append(sdeck.pop(0))
    return ddeck

def print_board(ddeck):
    """ Takes a 3d list
        Returns nothing """
    print("\n|", ddeck[0][0],"|", ddeck[0][1],"|", ddeck[0][2], "|", "\n" + "|", ddeck[1][0],"|", ddeck[1][1],"|", ddeck[1][2], "|", "\n" + "|", ddeck[2][0],"|", ddeck[2][1],"|", ddeck[2][2], "|"  )


def update_board(sdeck, ddeck):
    """ Takes the same suffled 2d list and 3d list
        Returns a edited 3D-list """

    #runs until an input is made for column and row
    while(True):
        #must input a valid row value before you input a column value
        r = input("New card: " + str(sdeck[0]) + ", enter location to replace card \nEnter a value between [0,2] for row[0,2]: ")
        if r.isdigit():
            r = int(r)
            if 0 <= r <= 2:

                #runs until a iput is made for column
                while(True):
                    c = input("Enter a value between [0,2] for column: ")
                    if c.isdigit():
                        c = int(c)
                        if 0 <= c <= 2:
                            #replaces the card you selected with the in index [0] for the shufled deck
                            ddeck[r][c] = sdeck.pop(0)
                            return ddeck
                        else:
                            print("Number must be between between [0,2]\n")
                    else:
                        print("Error, enter number for column\n")
            else:
                print("Number must be between between [0,2]\n")
        else:
            print("Error, enter number for row\n")

def sameSuit(ddeck):
    """takes in 3D-list for board
        returns boolean"""
    #Checks for matching suit ""SP", "CL", "HR", "DM"

    """
    Checks row 1 colum 1 and diagonals then shifts too row 2 colum 2 and diagonals does this one more time for 3 
    if it matchs at any point stops checking and returns true
    """
    for i in range(3):
        if (ddeck[i][0][0] == ddeck[i][1][0] == ddeck[i][2][0]) or (ddeck[0][i][0] == ddeck[1][i][0] == ddeck[2][i][0]) or (ddeck[0][0][0] == ddeck[1][1][0] == ddeck[2][2][0]) or (ddeck[2][0][0] == ddeck[1][1][0] == ddeck[0][2][0]):
            return True

    
def sameFace(ddeck):
    """takes in 3D-list for board
        returns boolean"""
    #Checks for matching Face "2,3,4,5,6,7,8,9"

    for i in range(3):
        if (ddeck[i][0][1] == ddeck[i][1][1] == ddeck[i][2][1]) or (ddeck[0][i][1] == ddeck[1][i][1] == ddeck[2][i][1]) or (ddeck[0][0][1] == ddeck[1][1][1] == ddeck[2][2][1]) or (ddeck[2][0][1] == ddeck[1][1][1] == ddeck[0][2][1]):
            return True

    
def consecutiveFace(ddeck):
    """takes in 3D-list for board
        returns boolean"""
    #Checks for 3 numbers of ascending or descending order from "2,3,4,5,6,7,8,9"
        
    for i in range(3):
        if (ddeck[i][0][1] + 1 == ddeck[i][1][1] and ddeck[i][1][1] +1 == ddeck[i][2][1]) or (ddeck[0][i][1] + 1 == ddeck[1][i][1] and ddeck[1][i][1] +1 == ddeck[2][i][1]) or (ddeck[0][0][1] +1 == ddeck[1][1][1] and ddeck[1][1][1] +1 == ddeck[2][2][1]) or (ddeck[0][2][1] +1 == ddeck[1][1][1] and ddeck[1][1][1] +1 == ddeck[2][0][1]):
            return True
        elif (ddeck[i][0][1] -1 == ddeck[i][1][1] and ddeck[i][1][1] -1 == ddeck[i][2][1]) or (ddeck[0][i][1] -1 == ddeck[1][i][1] and ddeck[1][i][1] -1 == ddeck[2][i][1]) or (ddeck[0][0][1] -1 == ddeck[1][1][1] and ddeck[1][1][1] -1 == ddeck[2][2][1]) or (ddeck[0][2][1] -1 == ddeck[1][1][1] and ddeck[1][1][1] -1 == ddeck[2][0][1]):
            return True


def suit_consecutiveFace(ddeck):
    """takes in 3D-list for board
        returns boolean"""
    #Checks for matching suit ""SP", "CL", "HR", "DM" and Checks for 3 numbers of ascending or descending order from "2,3,4,5,6,7,8,9"

    for i in range(3):
        if (ddeck[i][0][0] == ddeck[i][1][0] == ddeck[i][2][0]) and ( (ddeck[i][0][1] + 1 == ddeck[i][1][1] and ddeck[i][1][1] +1 == ddeck[i][2][1]) or (ddeck[i][0][1] -1 == ddeck[i][1][1] and ddeck[i][1][1] -1 == ddeck[i][2][1]) ):
            return True
        elif (ddeck[0][i][0] == ddeck[1][i][0] == ddeck[2][i][0]) and ( (ddeck[0][i][1] + 1 == ddeck[1][i][1] and ddeck[1][i][1] +1 == ddeck[2][i][1]) or (ddeck[0][i][1] -1 == ddeck[1][i][1] and ddeck[1][i][1] -1 == ddeck[2][i][1]) ):
            return True
        elif (ddeck[0][0][0] == ddeck[1][1][0] == ddeck[2][2][0]) and ( (ddeck[0][0][1] +1 == ddeck[1][1][1] and ddeck[1][1][1] +1 == ddeck[2][2][1]) or (ddeck[0][0][1] -1 == ddeck[1][1][1] and ddeck[1][1][1] -1 == ddeck[2][2][1]) ):
            return True
        elif (ddeck[2][0][0] == ddeck[1][1][0] == ddeck[0][2][0]) and ( (ddeck[0][2][1] +1 == ddeck[1][1][1] and ddeck[1][1][1] +1 == ddeck[2][0][1]) or (ddeck[0][2][1] -1 == ddeck[1][1][1] and ddeck[1][1][1] -1 == ddeck[2][0][1]) ):
            return True


def verify_matching(ddeck, score):
    """ Takes updated 3D-list and integer for score
        Returns Boolean for a match, Sting for the catgeory matched, and integer of updated score """
        
    match = False
    pointsEarned = 0
    categoryMatched = ""
    if sameSuit(ddeck) == True:
        pointsEarned = 10
        categoryMatched = "simple set"
        match = True
    if sameFace(ddeck) == True:
        pointsEarned = 15
        categoryMatched = "set"
        match = True
    if consecutiveFace(ddeck) == True:
        pointsEarned = 20
        categoryMatched = "simple run"
        match = True
    if suit_consecutiveFace(ddeck) == True:
        pointsEarned = 25
        categoryMatched = "run"
        match = True
    
    score += pointsEarned
    return match, categoryMatched, score
    
def game(sdeck):
    """ Takes in 2d list
        Returns (i) if the winner wins/loses the game (boolean), (ii) the final score (int), (iii) the winning category"""
    score = 0
    print("Welcome to the game!", end="")
    ddeck = deal(sdeck)
    print_board(ddeck)

    while(True):
        if len(sdeck) >= 1:
            play = input("Score: " + str(score) + ", Deal or Done? ")
            if play.isalpha:
                if play.lower() == "done":

                    match , categoryMatched , score = verify_matching(ddeck, score)
                    return match, categoryMatched, score
                    
                elif play.lower() == "deal": 
                    score -= 1
                    update_board(sdeck, ddeck)
                    print_board(ddeck)
                    print("Cards left to play:", len(sdeck))
                else:
                    print("Error, must enter Deal or Done\n")
            else:
                print("Error, must enter Deal or Done\n")
        else:
            match , categoryMatched , score = verify_matching(ddeck, score)
            return match, categoryMatched, score,


    
# main() function should call all other functions in the appropriate order to run the game
def main():
    #create and print the deck of cards
    deck = create_deck()
    print(f"\nDeck: {deck}")
    #create and print the shuffled deck of cards
    sdeck = shuffle(deck)
    print(f"\nShuffled deck: {sdeck}")
    
    print()
    

    match, categoryMatched, score = game(sdeck)
    if match == True:
        print("Congrats you've got a", categoryMatched, "on the board, Score:", score)
    else: 
        print("Sorry, no match on the board. Score:", score)

# main guard    
if __name__ == "__main__":
    main()
    