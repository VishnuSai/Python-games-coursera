# template for "Stopwatch: The Game"

#import modules

import simplegui
import time

# define global variables

count = 0
total = 0
success = 0
milliseconds = 0
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    seconds = int(time/10)
    global milliseconds
    milliseconds = time%10
    minutes = int(seconds/60)
    r_seconds = seconds%60
    if(r_seconds<10):
        rem_seconds = "0" + str(r_seconds)
    else:
        rem_seconds = str(r_seconds)
    return str(minutes) + ":" + rem_seconds + "." + str(milliseconds)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    global total
    total = total + 1
    if(milliseconds == 0):
        global success
        success = success + 1
    else:
        pass
    global score
    score = str(success) + "/" + str(total)

def reset():
    timer.stop()
    global count
    count = 0
    global total
    total = 0
    global success
    success = 0
    global score
    score = "0/0"

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count), (120, 100), 40, 'White')
    canvas.draw_text(score, (250, 30), 30, 'Green')

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)
start = frame.add_button('Start', start, 150)
stop = frame.add_button('Stop', stop, 150)
reset = frame.add_button('Reset', reset, 150)


# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()
