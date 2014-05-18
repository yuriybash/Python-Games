# Yuriy Bash
# An Introduction to Interactive Programming in Python
# Mini-Project 5 - Memory
# May 7, 2014
# implementation of card game - Memory

import simplegui
import random

list1 =[1, 2, 3, 4, 5, 6, 7, 8]
list2 = list1  
deck_of_cards = list1+list2
chosenCardIndex = 0
state = 0
state1Index = 1
state2Index = 3
turns = 0
history_of_indices = []


exposed =[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# helper function to initialize globals
def new_game():
    global deck_of_cards, exposed, state, turns
    state = 0
    turns = 0
    label.set_text( "Turns = " + str(turns) )
    random.shuffle(deck_of_cards)
    # print "deck_of_cards is: " + str(deck_of_cards)
    exposed =[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
     
# define event handlers
def mouseclick(pos):
    global chosenCardIndex, state, exposed, deck_of_cards, turns, index1, index2, history_of_indices
    chosenCardIndex = pos[0]/50
    print chosenCardIndex
     
    #no cards visible
    if exposed[chosenCardIndex] == False:
        exposed[chosenCardIndex] = True #flip it
        print "A"
        if state == 0:
            state = 1		# we opened 1st card 
            index1 = chosenCardIndex   
        elif state == 1:
            state = 2		# we opened 2nd card 
            index2 = chosenCardIndex
            turns += 1
            label.set_text( "Turns = " + str(turns) )
        else:
            state = 1		# we opened 3rd card
            
            # now check if 1st and 2nd cards match 
            # if they don't we need to flip them back 
            if deck_of_cards[index1] == deck_of_cards[index2]:
                print "Hurray! We get to keep the cards"
            else:
                exposed[index1] = False
                exposed[index2] = False
                
            index1 = chosenCardIndex      
    else:
         print "We are ignoring clicks on exposed cards"
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck_of_cards, exposed
    where_to_draw_x_coord = 0
        
    
    
    #LOOP THAT GOES THROUGH ALL CARDS
    for card in deck_of_cards:
            cardPosition = where_to_draw_x_coord/50
            
            if exposed[cardPosition] == True:
                canvas.draw_text(str(card), (where_to_draw_x_coord, 75), 72, 'White') #DRAWS NUMBER
                where_to_draw_x_coord += 50
            else:
                canvas.draw_polygon([(where_to_draw_x_coord+50, 0),(where_to_draw_x_coord, 0), (where_to_draw_x_coord, 100), (where_to_draw_x_coord+50, 100)], 1, 'Red', 'Green')
                where_to_draw_x_coord += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric