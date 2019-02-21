import sys
from .charDef import *
from .utils import getchar, mybeep

class BetterInput:
    def __init__(self):
        self.buffer = []
        self.pos = 0
        
    def put(self, c):
        sys.stdout.write(c)
        sys.stdout.flush()

    def moveCursor(self, pos):
        if pos < 0 or pos > len(self.buffer):
            mybeep()
            return False
        if self.pos <= pos:
            while self.pos != pos:
                self.put(self.buffer[self.pos])
                self.pos += 1
        else:
            while self.pos != pos:
                self.put("\b")
                self.pos -= 1
        return True

    def insertChar(self, c):
        self.buffer.insert(self.pos, c)
        self.put(''.join(self.buffer[self.pos:]))
        self.put("\b" * (len(self.buffer) - self.pos - 1))
        self.pos += 1

    def getInput(self):
        ret = ''.join(self.buffer).strip()
        self.buffer = []
        return ret

    def deleteChar(self):
        if self.pos == len(self.buffer):
            mybeep()
            return
        self.buffer.pop(self.pos)
        self.put(''.join(self.buffer[self.pos:]) + ' ')
        self.put("\b" * (len(self.buffer) - self.pos + 1))

    def input(self, q):
        self.put(q)
        while True:
            c = getchar()
            i = c if c == UNDEFINED_KEY else ord(c)

            if i == NEWLINE_KEY:
                self.put('\n')
                return self.getInput()
            elif i == LINE_BEGIN_KEY or i == HOME_KEY:
                return
            elif i == LINE_END_KEY or i == END_KEY:
                return
            elif i == BACK_SPACE_KEY:
                if self.moveCursor(self.pos - 1):
                    self.deleteChar()
            elif i == DELETE_KEY:
                self.deleteChar()
            elif i == ARROW_UP_KEY:
                return
            elif i == ARROW_DOWN_KEY:
                return
            elif i == ARROW_RIGHT_KEY:
                self.moveCursor(self.pos + 1)
            elif i == ARROW_LEFT_KEY:
                self.moveCursor(self.pos - 1)
            elif i == PG_UP_KEY:
                return
            elif i == PG_DOWN_KEY:
                return
            elif i == TAB_KEY:
                return
            elif i == UNDEFINED_KEY:
                return
            else:
                self.insertChar(c)