# 📚 vocabs
<p align=center>
<img src="./asset/dict.jpg" width="400"/>
<br>
<a target="_blank"><img src="https://img.shields.io/badge/platform-linux-lightgrey.svg"></a>
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
<a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
<a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
<a target="_blank"><img src="https://img.shields.io/badge/status-adding features-red.svg"></a>
</p>

***
> 📚 A lightweight online dictionary integration to the command line. No browsers. No paperbacks.
***

<p align=center><img src="./asset/gifs/demo.gif" width="1000"/></p>

## Setting Up
```shell
$ pip install vocabs
```

## Features
> 📆 Word of the Day!

> 📈 Trending words! 

> ❓ Directly query words from the command line.

> 📓 Save words to your local dictionary.

> 📝 Add notes to saved words.

> 🎮 Interactive word game to hone your vocabulary skills.

## So how is this different from `dict` ?

<p align=center>
<img src="./asset/gifs/dicthello.gif" width="400">
<img src="./asset/gifs/vocabhello.gif" width="400">
</p>

`dict` is the client for DICT, or the Dictionary Server Protocol on Unix-like platforms. It is used to query natural language dictionaries without firing up a bloaty browser, which tremendously slows down your workflow.

`Vocab` aims to do the same as `dict`, only with some differences:

- Less verbose result (since `Vocab` only uses one source).
- Can save words to local client dictionary pickle file.
- Can add notes to a saved word.
- Includes a interactive word-quiz feature.
- With colors 🎨!

All in all, `Vocab` is a great tool for fast word queries with easy-to-read definitions, and a good support for ESL users.

## Requirements
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a> and the following libraries are required.

> <a target="_blank"><img src="https://img.shields.io/badge/python-beautifulsoup4%20%7C%20requests%20%7C%20termcolor-blue.svg">

> <a target="_blank"><img src="https://img.shields.io/badge/platform-linux-lightgrey.svg"></a> <a target="_blank"><img src="https://img.shields.io/badge/python-tty%20%7C%20termios-blue.svg"></a>

## Running
🔥 Launch `vocab` anywhere on your terminal.
```shell
$ vocab
```


## Usage
```
$ vocab

Options:
    --mode, -m ['query', 'edit', 'dict', 'interactive']
    --file, -f <path to word list>
    --reset, -r
    --count, -c
    --lucky, -l
    --trend, t
```
### Feeling Lucky
> 📆 Word of the Day.
```
$ vocab -l
```
<img src="./asset/gifs/lucky.gif" width="600"/>

### Trending Words
> 📈 Shows a list of frequently searched words.
```
$ vocab -t
```
<img src="./asset/gifs/trending.gif" width="600"/>

### Query Mode
> ❓ Directly search and save unknown words **from the command line**.
```
$ vocab -m query
```
<img src="./asset/gifs/query.gif" width="600"/>

### Dictionary Mode
> 📓 Scroll though pages to search for saved words.
```
$ vocab -m dict
```
<img src="./asset/gifs/dict.gif" width="600"/>

### Edit mode
> ✏️ Edit your save words and add notes.
```
$ vocab -m edit
```
<img src="./asset/gifs/edit.gif" width="600"/>

### Interactive Mode
> 🎮 Test your vocabulary skills with the interactive mode.
```
$ vocab -m interactive
```
<img src="./asset/gifs/interactive.gif" width="600"/>

### Load Word List
> 📜 Load a list of words from to your local dictionary.
```
$ vocab -f <path to file>
```
<img src="./asset/gifs/file.gif" width="600"/>

### Count Total Words
> 🔢 Count number of words saved in your local dictionary.
```
$ vocab -c
```
<img src="./asset/gifs/count.gif" width="600"/>

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
