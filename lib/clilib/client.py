import sys
from .charDef import *
from . import utils
from termcolor import cprint

class BulletCli:
    def __init__(self, bullets = [], indent = 0, color = "cyan"):
        self.bullets = bullets
        self.pos = 0
        self.indent = indent
        self.color = color
    
    def renderBullets(self):
        for i in range(len(self.bullets)):
            self.printBullet(i)
            utils.forceWrite('\n')
            
    def printBullet(self, idx):
        utils.forceWrite(' ' * self.indent)
        if idx == self.pos:
            cprint("● ", self.color, end = '')
        else:
            utils.forceWrite("  ")
        utils.forceWrite(self.bullets[idx])
        utils.moveCursorHead()

    def moveBullet(self, up = True):
        if up:
            if self.pos - 1 < 0:
                return
            else:
                utils.clearLine()
                old_pos = self.pos
                self.pos -= 1
                self.printBullet(old_pos)
                utils.moveCursorUp(1)
                self.printBullet(self.pos)
        else:
            if self.pos + 1 >= len(self.bullets):
                return
            else:
                utils.clearLine()
                old_pos = self.pos
                self.pos += 1
                self.printBullet(old_pos)
                utils.moveCursorDown(1)
                self.printBullet(self.pos)

    def launch(self):
        self.renderBullets()
        utils.moveCursorUp(len(self.bullets))
        while True:
            c = utils.getchar()
            i = c if c == UNDEFINED_KEY else ord(c)
            if i == NEWLINE_KEY:
                utils.moveCursorDown(len(self.bullets) - self.pos)
                return self.bullets[self.pos]
            elif i == ARROW_UP_KEY:
                self.moveBullet()
            elif i == ARROW_DOWN_KEY:
                self.moveBullet(up = False)
                

if __name__ == "__main__":
    cli = BulletCli(["apple", "banana", "orange", "watermelon", "strawberry"], indent = 4)
    result = cli.launch()
    print(result)