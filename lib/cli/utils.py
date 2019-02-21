import sys
import tty, termios
import string
from .charDef import *

def mybeep():
    print(chr(BEEP_CHAR), end = '')

def mygetc():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getchar():
    c = mygetc()
    if ord(c) == LINE_BEGIN_KEY or \
       ord(c) == LINE_END_KEY   or \
       ord(c) == TAB_KEY        or \
       ord(c) == NEWLINE_KEY:
       return c
    
    elif ord(c) == BACK_SPACE_KEY:
        return c
    
    elif ord(c) == ESC_KEY:
        combo = mygetc()
        if ord(combo) == MOD_KEY_INT:
            key = mygetc()
            if ord(key) >= MOD_KEY_BEGIN - MOD_KEY_FLAG and ord(key) <= MOD_KEY_END - MOD_KEY_FLAG:
                if ord(mygetc()) == MOD_KEY_DUMMY:
                    return chr(ord(key) + MOD_KEY_FLAG)
                else:
                    return UNDEFINED_KEY
            elif ord(key) >= ARROW_KEY_BEGIN - ARROW_KEY_FLAG and ord(key) <= ARROW_KEY_END - ARROW_KEY_FLAG:
                return chr(ord(key) + ARROW_KEY_FLAG)
            else:
                return UNDEFINED_KEY
        else:
            mybeep()
            return getchar()

    else:
        if c in string.printable:
            return c
        else:
            return UNDEFINED_KEY

    return UNDEFINED_KEY