# Yuriy Bash
# An Introduction to Interactive Programming in Python
# Mini-project #6 - Blackjack
# May 14, 2014

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.total_value = 0
        self.totalAces = 0
        
    def __str__(self):
        self.ans = ""
        for i in range(len(self.cards)):
            self.ans+=str(self.cards[i]) + " "
        return self.ans

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.totalAces += 1

    def get_value(self):
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.total_value = 0
        for card in self.cards:
            self.total_value += VALUES.get(card.rank)
        if self.total_value <= 11 and self.totalAces > 0:
           self.total_value += 10
        return self.total_value
    
    def draw(self, canvas, pos):
        for x in self.cards:
            x.draw(canvas, [self.cards.index(x)*90 + pos[0], 30+ pos[1]])
                
       
   # def draw(self, canvas, pos):
          #      for y in self.cards:
       #             y.draw(canvas, [len(self.cards)*30, 30]
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cardsInDeck = []
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit, rank)
                self.cardsInDeck.append(c)
        

    def shuffle(self):
        return random.shuffle(self.cardsInDeck)
        
    def deal_card(self):
        return self.cardsInDeck.pop()	# deal a card object from the deck
    
    def __str__(self):
        self.ans = ""
        for card in self.cardsInDeck:
            self.ans = self.ans + str(card) + " "
        return ans

#global variables for player and dealer hands, and deck in play    

deckInPlay = Deck()
playerHand = Hand()
dealerHand = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, deckinPlay, playerHand, dealerHand, score, canvas
    if in_play:
        score-=1
        outcome = "Player forefeited last game. Hit or stand?"
    else:
        outcome = "Hit or stand?"
    deckInPlay = Deck()
    deckInPlay.shuffle()
    playerHand = Hand()
    dealerHand = Hand()
    playerHand.add_card(deckInPlay.deal_card())	
    playerHand.add_card(deckInPlay.deal_card())
    dealerHand.add_card(deckInPlay.deal_card())
    dealerHand.add_card(deckInPlay.deal_card())
    
    
    
    in_play = True

def hit():
    global in_play, playerHand, score, outcome, deckInPlay
    if in_play == True:
        playerHand.add_card(deckInPlay.deal_card())
        if playerHand.get_value() > 21:
            score -= 1
            outcome = "Player Busted. New game?"
            in_play = False
    
        
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, outcome, dealerHand, deckInPlay, playerHand, score
    if outcome == "Busted":
        print "Player, reminder: you have busted"
    else:
        if in_play == True:
            while dealerHand.get_value() < 17:
                dealerHand.add_card(deckInPlay.deal_card())
            if dealerHand.get_value() > 21:
                outcome = "Dealer busts. New game?"
                score += 1
                in_play = False
            else:
                if playerHand.get_value() <= dealerHand.get_value():
                    outcome =  "Dealer wins! New game?"
                    score -= 1
                    in_play = False
                else:
                    outcome = "Player wins! New game?"
                    score += 1
                    in_play = False
    
    
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def mouseclick(pos):
    pass    
    
# draw handler    
def draw(canvas):
    dealerHand.draw(canvas, (20,80))
    playerHand.draw(canvas, (20, 300))
    canvas.draw_text('Dealer hand:', [30, 70], 20, 'White')
    canvas.draw_text('Player hand:', [30, 300], 20, 'White')
    canvas.draw_text(outcome, [550, 250], 20, 'White')
    canvas.draw_text("Player score: " + str(score), [550, 150], 20, 'White')
    canvas.draw_text("BLACKJACK", [550, 50], 25, 'Blue')
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (57,161), CARD_BACK_SIZE)
    
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 1000, 800)
frame.set_canvas_background("Green")
frame.set_mouseclick_handler(mouseclick)

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric