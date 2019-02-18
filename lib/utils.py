from bs4 import BeautifulSoup
from termcolor import cprint
from pyfiglet import Figlet
from . import cli

def parseQuery(r):
    soup = BeautifulSoup(r, "html.parser")
    defs = soup.find_all("section", {"class" : "gramb"})
    result = []
    for d in defs:
        pos = d.find("h3", {"class" : "ps pos"}).find("span", {"class" : "pos"}).text
        meaning = d.find("ul", {"class" : "semb"}).find("p").find("span", {"class" : "ind"}).text
        example = d.find("ul", {"class" : "semb"}).find("div", {"class" : "trg"}).find_all("div", {"class" : "exg"}, recursive = False)
        example = list(map(lambda html : html.find("em").text, example))
        result.append((pos, meaning, example))
    return result

def showQuery(r):
    lineCt = 0
    if not r:
        print("Word not found!")
        lineCt += 1
    else:
        for pos, meaning, example in r:
            cprint(pos, 'yellow', end = ' ')
            cprint(meaning, 'cyan')
            lineCt += 1
            for i in range(len(example)):
                cli.puts(str(i + 1) + '. ' + example[i])
                lineCt += 1
    return r, lineCt

def renderText(s):
    f = Figlet(font = 'slant')
    print(f.renderText(s), end = '')
