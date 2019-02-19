# 📚 Vocab
<p align=center>
<img src="./asset/dict.jpg" width="400"/>
<br>
<a target="_blank"><img src="https://img.shields.io/badge/platform-linux-lightgrey.svg"></a>
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
<a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
<a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

***
> 📚 A lightweight online dictionary integration to the command line. No browsers. No paperbacks.
***

<p align=center><img src="./asset/demo.gif" width="800"/></p>

## Features
> ❓ Directly query words from the command line.

> 📓 Save words to your local dictionary.

> 📝 Add notes to saved words.

> 🎮 Interactive word game to hone your vocabulary skills.

## So how is this different from `dict` ?
`dict` is the client for DICT, or the Dictionary Server Protocol on Unix-like platforms. It is used to query natural language dictionaries without firing up a bloaty brower, which tremendously slows down your workflow.

`Vocab` aims to do the same as `dict`, only with some differneces:

- Less verbose result (since `Vocab` only uses one source).
- Can save words to local client dictionary pickle file.
- Can add notes to a saved word.
- Includes a interactive word-quiz feature.

All in all, `Vocab` is a great tool for fast word queries with easy-to-read definitions, and a good support for ESL users.

## Requirements
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a> and the following libraries are required.

> <a target="_blank"><img src="https://img.shields.io/badge/python-beautifulsoup4%20%7C%20requests%20%7C%20termcolor-blue.svg">

> <a target="_blank"><img src="https://img.shields.io/badge/platform-linux-lightgrey.svg"></a> <a target="_blank"><img src="https://img.shields.io/badge/python-tty%20%7C%20termios-blue.svg"></a>

## Setting up
- Clone the git repository `Vocab`.
- In `/Vocab/lib/config.py`, modify `DICT_PATH` to the ABSOLUTE PATH of the local dictionary file on your computer.
- In root, type `vi ~/.bashrc`. Append the following at the end of the bashrc file : `export PATH=$PATH/<ABSOLUTE PATH to git repo>`

## Running
🔥 Launch `vocab` anywhere on your terminal.


## Usage
### Query Mode
> ❓ Directly search and save unknown words **from the command line**.
```
$ vocab -m query
```
<img src="./asset/query-cropped.gif" width="600"/>

### Dictionary Mode
> 📓 Scroll though pages to search for saved words.
```
$ vocab -m dict
```
<img src="./asset/dict-cropped.gif" width="600"/>

### Edit mode
> ✏️ Edit your save words and add notes.
```
$ vocab -m edit
```
<img src="./asset/edit-cropped.gif" width="600"/>

### Interactive Mode
> 🎮 Test your vocabulary skills with the interactive mode.
```
$ vocab -m interactive
```
<img src="./asset/interactive-cropped.gif" width="600"/>

### Load Word List
> 📜 Load a list of words from to your local dictionary.
```
$ vocab -f <ABSOLUTE path to file>
```
<img src="./asset/file-cropped.gif" width="600"/>

### Count Total Words
> 🔢 Count number of words saved in your local dictionary.
```
$ vocab -c
```
<img src="./asset/count-cropped.gif" width="600"/>

### Reset Local Dictionary
```
$ vocab -r
```
### Help
```
$ vocab -h
```

## Todo
- Synonyms / Antonyms.
- Full command line support (left, right keys, autofill).
- Search history (up, down keys).
