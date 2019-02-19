#!/usr/bin/env python3

import os
import sys
import tty, termios

from termcolor import cprint
rows, columns = os.popen('stty size', 'r').read().split()

# Basic cli operations
def puts(s, indent = 4):
    ''' Print string with indent. '''

    print(" " * indent + s)

def moveCursorLeft(n):
    ''' Move cursor left n columns. '''

    sys.stdout.write("\033[{}D".format(n))

def moveCursorRight(n):
    ''' Move cursor right n columns. '''
    
    sys.stdout.write("\033[{}C".format(n))
    
def moveCursorUp(n):
    ''' Move cursor up n rows. '''

    sys.stdout.write("\033[{}A".format(n))

def moveCursorDown(n):
    ''' Move cursor down n rows. '''

    sys.stdout.write("\033[{}B".format(n))
    
def clearLine():
    ''' Clear content of one line on the console. '''

    print(" " * int(columns), end = '')
    print("\b" * int(columns), end = '')
    moveCursorLeft(int(columns)) # Move cursor to beginning of line
    
def clearConsole(n):
    ''' Clear n console rows (bottom up). ''' 

    for _ in range(n):
        clearLine()
        moveCursorUp(1)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


