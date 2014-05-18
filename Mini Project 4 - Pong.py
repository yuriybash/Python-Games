# Yuriy Bash
# An Introduction to Interactive Programming in Python
# Mini-Project 4: Pong
# April 30, 2014
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
ball_vel = [0, 0]
ball_pos = [300, 200]
player1score = 0
player2score = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    ball_vel = [0,0]
    
    if direction == 'RIGHT':
        ball_vel = [random.randrange(2, 5), random.randrange(-5, -4)]
        
    if direction == 'LEFT':
        ball_vel = [random.randrange(-4, -2), random.randrange(4, 5)]
    
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball('RIGHT')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, player1score, player2score
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if (ball_pos[1]<=BALL_RADIUS) or (ball_pos[1]>= HEIGHT-BALL_RADIUS):
        ball_vel[1] *= -1
    
   
    
    
    #tests whether ball has collided with paddle
    if (ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH) and (ball_pos[1] < paddle2_pos+HALF_PAD_HEIGHT) and (ball_pos[1] > paddle2_pos-HALF_PAD_HEIGHT):
        ball_vel[0] *= -1.2
        
    
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH) and (ball_pos[1] < paddle1_pos+HALF_PAD_HEIGHT) and (ball_pos[1] > paddle1_pos-HALF_PAD_HEIGHT):
        ball_vel[0] *= -1.2
    
    
    #LEFT gutter
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH and ((ball_pos[1] < paddle1_pos-HALF_PAD_HEIGHT) or (ball_pos[1] > paddle1_pos+HALF_PAD_HEIGHT)):
        spawn_ball('LEFT')
        player2score+=1
    
    #RIGHT gutter    
    if ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH and ((ball_pos[1] < paddle2_pos-HALF_PAD_HEIGHT) or (ball_pos[1] > paddle2_pos+HALF_PAD_HEIGHT)):
       spawn_ball('RIGHT')
       player1score+=1
    
    # draw ball
    canvas.draw_circle(ball_pos, 10, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos-HALF_PAD_HEIGHT)+paddle1_vel) >=0 and (paddle1_pos+HALF_PAD_HEIGHT)+paddle1_vel<HEIGHT:
        paddle1_pos += paddle1_vel
    
    if ((paddle2_pos-HALF_PAD_HEIGHT)+paddle2_vel) >=0 and (paddle2_pos+HALF_PAD_HEIGHT)+paddle2_vel<HEIGHT:
        paddle2_pos += paddle2_vel
    
    
       
    
    # draw paddles
    
    canvas.draw_line((0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), 12, 'White')
    canvas.draw_line((WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), 12, 'White') 
    
    
    # draw scores
    
    canvas.draw_text(str(player1score), (150, 80), 28, 'White')
    canvas.draw_text(str(player2score), (450, 80), 28, 'White')
    
def button_handler():
    global player1score, player2score
    new_game()
    player1score = 0
    player2score = 0
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 6
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 6
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 6
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 6
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', button_handler)

# start frame
new_game()
frame.start()
