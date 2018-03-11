#!/usr/bin/env python3
# Import libraries
import os

# Set Default Variables
greetings = '''Hello, from here you can do a few things including:
    Send a "hello world message" [hello]
'''

#################################################################################
# Define the "hello" function
def print_hello(usr_NAME):
    os.system('clear')
    print('HELLO WERLD!')
    print('My name is ', usr_NAME)        # TODO: @stephanie why does this break

#################################################################################
def req_command():
    usr_CMD = "Empty"
    usr_NAME = "Empty"
    while usr_NAME == "Empty":
        usr_NAME = input('First, what is your name? : ')
    print('Your name is:', usr_NAME)      # TODO: @stephanie why does this work
    while usr_CMD == "Empty":
        usr_CMD = input('What would you like to do {0}? : '.format(usr_NAME))
        if usr_CMD == 'hello':
            print_hello(usr_NAME)
        else:
            print('Sorry, that command was not understood, please try again...')

#################################################################################
#say_HELLO = True
print(greetings)
req_command()
