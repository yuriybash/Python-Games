# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables

secret_number = 0
guesses_left = 0

# helper function to start and restart the game
def new_game():
    print "\n"
    print "\n \n New game! \n \n" 
    print "\n"
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number, guesses_left
    print "\n"
    secret_number = random.randint(0,100)
    guesses_left = 7
    print "New game. Range is 0 to 100. 7 guesses left"
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number, guesses_left
    print "\n"
    secret_number = random.randint(0,1000)
    guesses_left = 10
    print "New game. Range is 0 to 1000. 10 guesses left."
    
    
def input_handler(guess):
    # main game logic goes here	
    global guesses_left
    print "\n"
    print "Guess was " + guess
    
    guesses_left = guesses_left - 1
    
    
    if guesses_left == 0 and guess != secret_number:
        print "Game over. 0 guesses left. Correct answer was " + str(secret_number)
        if secret_number < 100:
            range100()
        if secret_number >= 100:
            range1000()
       
    elif int(guess) == secret_number:
        print "Number of guesses left is " + str(guesses_left)
        print "Correct!"
        if secret_number < 100:
            range100()
        elif secret_number >= 100:
            range1000()
    elif int(guess) < secret_number:
        print "Number of guesses left is " + str(guesses_left)
        print "Higher!"
    elif int(guess) > secret_number:
        print "Number of guesses left is " + str(guesses_left)
        print "Lower!"   
    print "\n"   
    
    

    
# create frame

frame=simplegui.create_frame("gameframe", 500, 500)
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.add_input("Enter a guess: ", input_handler, 100)


# register event handlers for control elements



# call new_game and start frame
frame.start()
range100()

