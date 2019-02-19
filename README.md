# Vocab
<p align=center>
<img src="./asset/dict.jpg" width="400"/>
<br>
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
<a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
<a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

***
> A lightweight online dictionary integration to the command line. No browsers. No paperbooks.
***

<p align=center><img src="./asset/demo.gif" width="800"/></p>

## Features
- Directly query words from the command line.
- Save words to your local dictionary.
- Add notes to saved words.
- Interactive word game to hone your vocabulary skills.
## Requirements
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a> and the following libraries are required.
- beautifulsoup4
- pyfiglet
- termcolor
- requests
- (Linux compatible) tty, termios

## Run
- Clone the git repository `./Vocab`.
- In `./Vocab` directory, type `./vocab`.
- Enjoy the experience!

## Usage
### Query Mode
> Directly search and save unknown words **from the command line**.
```
$ ./vocab -m query
```
<img src="./asset/query.gif" width="500"/>

### Dictionary Mode
> Scroll though pages to search for saved words.
```
$ ./vocab -m dict
```
<img src="./asset/dict.gif" width="500"/>

### Edit mode
> Edit your save words and add notes.
```
$ ./vocab -m edit
```
<img src="./asset/edit.gif" width="500"/>

### Interactive Mode
> Test your vocabulary skills with the interactive mode.
```
$ ./vocab -m interactive
```
<img src="./asset/interactive.gif" width="500"/>

### Load Word List
> Load a list of words from to your local dictionary.
```
$ ./vocab -f <path to file>
```
<img src="./asset/file.gif" width="500"/>

### Count Total Words
> Count number of words saved in your local dictionary.
```
$ ./vocab -c
```
<img src="./asset/count.gif" width="500"/>

### Reset Local Dictionary
```
$ ./vocab -r
```
### Help
```
$ ./vocab -h
```

## Todo
- Synonyms / Antonyms.
- Full command line support (left, right keys, autofill).
- Search history (up, down keys).