#!/usr/bin/env python3
# Import libraries
import os

#################################################################################
# Define the "hello" function
# TODO: clean up print to screen lines
def print_hello_usr(usr_NAME, friend_NAME):
    os.system('clear')
    print('Hello', end=' ')
    print(friend_NAME, end='. ')
    print('How are you?', end=' ')
    print('My name is ', usr_NAME)

#################################################################################
# Define the "hello" function
def print_hello_world(usr_NAME):
    os.system('clear')
    print('>>  HELLO WERLD!', end=' ')
    print('My name is', usr_NAME, end='<<   ;)')       # BUG_1.2 - variable usr_NAME fails "not defined"

#################################################################################
# Ask friend what their name is
def ask_friend_name(friend_NAME):
    os.system('clear')
    friend_NAME = "None"
    if friend_NAME == "None":                              # TODO: change to while loop + add sanity check
        friend_NAME = input('Hi Friend; what is your name? : ')
        return friend_NAME

#################################################################################
# Ask friend what their name is
def ask_usr_name(usr_NAME):
    os.system('clear')
    if usr_NAME == "None":                                 # TODO: change to while loop + add sanity check
        usr_NAME = input('First, what is your name? : ')
        return usr_NAME                              # BUG_1.1 - attempting to return variable 'usr_NAME'

#################################################################################
def req_command(usr_CMD, usr_NAME):

    if usr_CMD == "None":                                  # TODO: change to while loop + add sanity check
        usr_CMD = input('What would you like to do {0}? : '.format(usr_NAME))

        if usr_CMD == 'hello world':                       # TODO: change to while loop + add sanity check

            ask_usr_name(usr_NAME)                   # Get User Name
            print_hello_world(usr_NAME)              # Print Salutations + User Name

        elif usr_CMD == 'hello human':

            ask_usr_name(usr_NAME)                   # Get User Name
            ask_friend_name()                        # Get Friend Name

            print_hello_usr(usr_NAME, friend_NAME)   # Print Salutations + User Name

        else:
            print('Sorry, that command was not understood, please try again...')

#################################################################################
# Leading function to define base variables etc.
# Set Default Variables
def main():
    os.system('clear')
    greetings = '''Hello, from here you can do a few things including:
    Send a "hello world message"  [hello world]
    Send a "hello human message"  [hello human]
    '''

    # Set Default value of usr_NAME
    try:
        usr_NAME
    except NameError:
        usr_NAME = "None"

    # Set Default value of usr_CMD
    usr_CMD = "None"

    print(greetings)
    req_command(usr_CMD, usr_NAME)

#################################################################################
# Start Program
main()
