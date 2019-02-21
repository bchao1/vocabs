#!/usr/bin/env python3

import os
import pickle
import requests
from . import utils
from . import cli
from . import config
import time
import random
import math
from termcolor import cprint
from bs4 import BeautifulSoup

class App:
    def __init__(self):
        self.root_url = "https://en.oxforddictionaries.com/"
        self.query_url = "https://en.oxforddictionaries.com/definition/{}"
        self.sess = requests.Session()
        self.myDict = {}
        if not os.path.exists(config.DICT_DIR):
            os.mkdir(config.DICT_DIR)
        if not os.path.exists(config.DICT_PATH):
            self.saveDict()
        self.loadDict()

    def internet_on(self):
        ''' Check internet connection. '''
        try:
            r = requests.get("https://www.google.com/", timeout = 1)
            return True
        except requests.exceptions.RequestException as e: 
            print("Internet is not connected. Please check your internet connection.")
            return False
    
    def soupify(self, url):
        r = self.sess.get(url)
        return BeautifulSoup(r.text, 'html.parser')

    def printIntro(self):
        utils.renderText(" Vocab ")
        cprint("A lightweight dictionary and vocabulary cli.", 'grey', 'on_white', end = '\n')
    
    def printHeader(self):
        print(" Your saved words: ", end = '')
        cprint(len(self.myDict), 'yellow', end = "\n\n")
    
    def printCount(self):
        knownCnt = sum([1 for word in self.myDict if self.myDict[word]["know"]])
        cprint(" Know       {0: >10} ".format(knownCnt), "white", "on_green")
        cprint(" Don't know {0: >10} ".format(len(self.myDict) - knownCnt), "white","on_red", end = "\n\n")

    def printSummary(self):
        self.printHeader()
        self.printCount()
    
    def printNotes(self, notes):
        cprint(" My Notes ", "red", "on_white")
        for i in range(len(notes)):
            cprint("{0: >5} ".format(i + 1), "magenta", end = '')
            print(notes[i])
        
    def launch(self, mode):
        if not self.internet_on():
            return

        self.printIntro()

        if mode == 'query':
            self.runQueryMode()
        elif mode == 'edit':
            self.runEditMode()
        elif mode == 'interactive':
            self.runInteractiveMode()
        elif mode == 'dict':
            self.runDictionaryMode()
        self.saveDict()
        self.end()
    
    def runDictionaryMode(self):
        print('\n', end = '')
        words = sorted(list(self.myDict.keys()))
        page, maxPage = 1, int(math.ceil(len(words) / 20))
        while True:
            idx = 20 * (page - 1)
            maxIdx = min(len(words) - 1, 20 * page - 1)
            lineCt = 0
            print("Page ", end = '')
            cprint("{}".format(page), "cyan")

            while idx <= maxIdx:
                print("{0: >20}".format(words[idx]), end = '')
                idx += 1
                if idx % 5 == 0 or idx == len(words):
                    print('\n', end = '')
                    lineCt += 1 
            
            s = input("Previous / Next / Quit / Word ['p'/'n'/'q'/<word>]: ")
            s = s.lower()
            if s == 'p' and page - 1 > 0:
                page -= 1
            elif s == 'n' and page + 1 <= maxPage:
                page += 1
            elif s in words[20 * (page - 1) : 20 * page]:
                cli.clearConsole(lineCt + 2)
                if not self.myDict[s]["def"]:
                    query = self.query_url.format(s)
                    r =  utils.parseQuery(self.sess.get(query).text)
                    self.myDict[s]["def"] = r
                    self.saveDict()
                utils.showQuery(self.myDict[s]["def"])
                print('\n', end = '')
                break
            elif s == 'q':
                break
            cli.clearConsole(lineCt + 2)
            cli.clearLine()

    def runInteractiveMode(self):
        self.printSummary()
        wordList = list(self.myDict.keys())
        if not wordList:
            print("No words in your dictionary!")
            return
        while True:
            idx = random.randint(0, len(wordList) - 1)
            cprint(" >> ", "cyan", end = '')
            print(wordList[idx])
            know = input("Know this word? ['y']['q' to quit]: ")
            know = know.lower()
            if know == 'q':
                break
            self.myDict[wordList[idx]]["know"] = True if know == 'y' else False
            _, lineCt = self.query(wordList[idx])
            print("Enter anything to continue...")
            c = cli.getch()
            cli.clearConsole(6 + lineCt)
            self.printCount()

    def runEditMode(self):
        ''' Edit saved words. '''
        self.printHeader()
        word = input("Edit word ['q' to quit]: ")
        word = word.lower()
        if word == 'q':
            return
        if word not in self.myDict:
            save = input("Add word to dictionary? ['y']: ")
            if save.lower() == 'y':
                query = self.query_url.format(word)
                r =  utils.parseQuery(self.sess.get(query).text)
                self.myDict[word] = {"def" : r, "notes" : [], "know" : False}
                self.saveDict()
            else:
                return
        else:
            if not self.myDict[word]["def"]:
                query = self.query_url.format(word)
                r =  utils.parseQuery(self.sess.get(query).text)
                self.myDict[word]["def"] = r
                self.saveDict()
        
        print("\n", end = '')
        utils.showQuery(self.myDict[word]["def"])
        print("\n", end = '')
        self.printNotes(self.myDict[word]["notes"])
        print("\n", end = '')
        self.addNotes(word)

    def runQueryMode(self):
        ''' Query mode of app. '''
        print('\n', end = '')
        while True:
            cli.clearLine()
            word = input("Enter Word to Query ['q' to quit]: ")
            word = word.lower()
            if word == 'q':
                break
            result, lineCnt = self.query(word)
            self.saveWord(word, result)
            if not result:
                cli.clearConsole(lineCnt + 1)
            else:
                cli.clearConsole(lineCnt + 2)

    def getWordOfTheDay(self):
        self.printIntro()
        soup = self.soupify(self.root_url)
        daily_word = soup.find("a", {"class":"linkword"}).text
        print('\n', end = '')
        cprint("Word of the day:", "magenta", "on_white", end = '')
        cprint(' ' + daily_word)
        result, _ = self.query(daily_word)
        self.saveWord(daily_word, result)
        return

    def query(self, word):
        ''' Query word from online dictionary or cached. '''
        if word in self.myDict and self.myDict[word]["def"]:
            # Retrieve from own dictionary
            r = self.myDict[word]["def"]
        else:
            # New query
            query = self.query_url.format(word)
            r =  utils.parseQuery(self.sess.get(query).text)
        return utils.showQuery(r)

    def saveDict(self):
        with open(config.DICT_PATH, "wb") as file:
            pickle.dump(self.myDict, file)
    
    def loadDict(self):
        with open(config.DICT_PATH, "rb") as file:
            self.myDict = pickle.load(file)

    def addNotes(self, word):
        while True:
            s = input("Enter notes (or enter index to delete) ['q' to quit]: ")
            cli.moveCursorUp(1)
            cli.clearLine()
            if s.lower() == 'q':
                return
            if s.isdigit():
                if int(s) > 0 and int(s) <= len(self.myDict[word]["notes"]):
                    cli.clearConsole(2 + len(self.myDict[word]["notes"]))
                    self.myDict[word]["notes"].pop(int(s) - 1)
                    self.printNotes(self.myDict[word]["notes"])
                    print("\n", end = '')
            else:
                self.myDict[word]["notes"].append(s)
                cli.clearConsole(1 + len(self.myDict[word]["notes"]))
                self.printNotes(self.myDict[word]["notes"])
                print("\n", end = '')
            self.saveDict()
        
    def saveWord(self, word, result):
        ''' Save word to word list. '''
        if not result:
            time.sleep(1)
        else:
            save = input("Save word? ['y'] : ")
            if save.lower() == 'y':
                self.myDict[word] = {"def" : result, "notes" : [], "know" : False}
            self.saveDict()

    def end(self):
        self.sess.close()
    
    def guard(self):
        r = input("Are you sure you want to reset the dictionary? (All saved words will be lost) ['y']: ")
        if r.lower() == 'y':
            self.reset()

    def feelingLucky(self):
        self.getWordOfTheDay()

    def loadWordList(self, wordlist):
        wordCt = 0
        try:
            with open(wordlist, 'r') as file:
                for line in file:
                    word = line.strip().lower()
                    if word not in self.myDict:
                        self.myDict[word] = {"def" : None, "notes" : [], "know" : False}
                        wordCt += 1
            self.saveDict()
            self.printIntro()
            cprint("{} ".format(wordCt), "yellow", end = '')
            print("new words added to local dictionary.\n")
        except:
            print("Path \"{}\" doesn't exist!".format(wordlist))

    def wordCount(self):
        self.printIntro()
        self.printHeader()

    def reset(self):
        ''' Reset cache dictionary. '''
        self.myDict = {}
        with open(config.DICT_PATH, "wb") as file:
            pickle.dump(self.myDict, file)