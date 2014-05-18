# Yuriy Bash
# An Introduction to Interactive Programming in Python
# Mini-Project 3: Stopwatch: The Game
# April 23, 2014

import simplegui

# define global variables

current_time = 0
current_time_formatted = "0:00.0"
num_attempts = 0
num_successes = 0
is_running = False


#current_time_formatted - amt of time properly formatted
#stopwatch_is_running - boolean that says whether stopwatch is running


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global current_time_formatted
    num_minutes = t/600
    
    seconds = int(round((t-(num_minutes*600))/10))
    
    tenths_of_seconds = int(round((t-(num_minutes*600))%10))
    
    if seconds < 10:
        current_time_formatted = str(num_minutes) + ":0" + str(seconds) + "." + str(tenths_of_seconds)
    else:    
        current_time_formatted = str(num_minutes) + ":" + str(seconds) + "." + str(tenths_of_seconds)
    

    # define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global is_running
    is_running = True
    timer.start()
    
def reset():
    global current_time
    timer.stop()
    global is_running
    global num_attempts
    global num_successes
    is_running = False
    current_time = 0
    format(current_time)
    num_attempts = 0
    num_successes = 0
    
def stop():
    global num_attempts
    global num_successes
    global is_running
    if is_running == True:
        num_attempts += 1
        if current_time%10 == 0:
            num_successes += 1
    is_running = False        
    timer.stop()
    


#Handler for timer - every 100 ms, 0.1 seconds are added

def tick():
    global current_time
    current_time += 1
    format(current_time)
    



# define event handler for timer with 0.1 sec interval

timer = simplegui.create_timer(100, tick)


# define draw handler
def draw(canvas):
    canvas.draw_text(current_time_formatted, (150, 150), 42, 'Red')
    canvas.draw_text(str(num_successes) + "/" + str(num_attempts), (50,50), 30, 'Green')

    
# create frame

frame = simplegui.create_frame("Frame1", 500, 500)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Reset", reset, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Start", start, 100)

# start frame
frame.start()

