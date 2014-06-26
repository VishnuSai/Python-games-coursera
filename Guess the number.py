# "Guess the number" mini-project

# modules required
import random
import simplegui


# initialize global variables 
secret_number = 0
guesses = 0


# helper function to start and restart the game

# decrements the total guesses left
# prints the guesses
def guess_left():
    global guesses
    guesses = guesses - 1
    print "Number of remaining guesses is ", guesses

# start new game    
def new_game():
    range100()
    return

# event handler for button
# button that changes range to range [0,100) and restarts
def range100():
    global secret_number
    secret_number = random.randrange(0,100)
    global guesses
    guesses = 7
    print
    print "New Game. Range is from 0 to 100"
    print "Number of remaining guesses is 7"
    print
    return

# event handler for button
# button that changes range to range [0,1000) and restarts
def range1000():
    global secret_number
    secret_number = random.randrange(0,1000)
    global guesses
    guesses = 10
    print
    print "New Game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    print
    return
        
    
# event handler for input field    
def input_guess(guess):
    # main game logic 	
    guess_number = int(guess)
    print "Guess was ",guess_number
    guess_left()
    if(guesses > 0):
        if(guess_number < secret_number):
            print "Higher!"
            print
        elif(guess_number > secret_number):
            print "Lower!"
            print
        elif(guess_number == secret_number):
            print "Correct!"
            print
            new_game()
        
    else:
        if(guess_number == secret_number):
            print "Correct!"
            print
            new_game()
        else:
            print "You ran out of guesses. The number was ",secret_number
            new_game()
        
        
    
       
# create frame
frame = simplegui.create_frame("Guess_the_number", 200, 200)

# register event handlers for control elements
button1 = frame.add_button("Range in 0-100", range100, 200 )
button1 = frame.add_button("Range in 0-1000", range1000, 200 )
inp = frame.add_input('Guess number', input_guess, 50)


# call new_game and start frame
frame.start()
new_game()

