#!/usr/bin/env python3
# Import libraries
import os

#################################################################################
# Define the "hello" function
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
    print('HELLO WERLD!', end=' ')
    print('My name is ', usr_NAME)

#################################################################################
def req_command(usr_NAME):
    usr_CMD = "Empty"
    while usr_NAME == "Empty":
        usr_NAME = input('First, what is your name? : ')
    print('Your name is:', usr_NAME)
    while usr_CMD == "Empty":
        usr_CMD = input('What would you like to do {0}? : '.format(usr_NAME))
        if usr_CMD == 'hello world':
            print_hello_world(usr_NAME)
        elif usr_CMD == 'hello human':
            friend_NAME = "Empty"
            while friend_NAME == "Empty":
                friend_NAME = input('Hi Friend; what is your name? : ')
            print_hello_usr(usr_NAME, friend_NAME)
        else:
            print('Sorry, that command was not understood, please try again...')

#################################################################################
# Leading function to define base variables etc.
# Set Default Variables
def main():
    usr_NAME = "Empty"
    greetings = '''Hello, from here you can do a few things including:
    Send a "hello world message"  [hello world]
    Send a "hello human message"  [hello human]
    '''
    print(greetings)
    req_command(usr_NAME)

#################################################################################
# Start Program
main()
