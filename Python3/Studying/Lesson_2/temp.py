#!/usr/bin/env python3
# Set Default Variables
greetings = '''Hello, from here you can do a few things including:
    Send a "hello world message" [hello]
'''

#################################################################################
# Define the "hello" function
def print_hello():
    print('HELLO WERLD! My name is')

#################################################################################
def req_command():
    usr_CMD = "Empty"
    usr_NAME = "Empty"
    while usr_NAME == "Empty":
        usr_NAME = input('First, what is your name? : ')
    print(usr_NAME)
    while usr_CMD == "Empty":
        usr_CMD = input('What would you like to do? : ')
        if usr_CMD == 'hello':
            print_hello()
        else:
            print('Sorry, that command was not understood, please try again...')

#################################################################################
#say_HELLO = True
print(greetings)
req_command()
