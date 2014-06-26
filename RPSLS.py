# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random


def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    if(name =='rock'):
        return 0
    elif(name =='Spock'):
        return 1
    elif(name =='paper'):
        return 2
    elif(name =='lizard'):
        return 3
    elif(name =='scissors'):
        return 4
    else:
        return "Incorrect name"
    
    # convert name to number using if/elif/else
    
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
        
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    


def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print
    
    # print out the message for the player's choice
    if(player_choice =='rock'):
        print "Player chooses rock"
    elif(player_choice =='Spock'):
        print "Player chooses Spock"
    elif(player_choice =='paper'):
        print "Player chooses paper"
    elif(player_choice =='lizard'):
        print "Player chooses lizard"
    elif(player_choice =='scissors'):
        print "Player chooses scissors"
    
        
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    if(comp_number == 0):
        print "Computer chooses rock"
    elif(comp_number == 1):
        print "Computer chooses Spock"
    elif(comp_number == 2):
        print "Computer chooses paper"
    elif(comp_number == 3):
        print "Computer chooses lizard"
    elif(comp_number == 4):
        print "Computer chooses scissors"

    # compute difference of comp_number and player_number modulo five
    final_value = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if(final_value == 1 or final_value == 2):
        print "Computer wins!"
    elif(final_value == 3 or final_value == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
