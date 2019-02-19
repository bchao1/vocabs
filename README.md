# Vocab
<p align=center><img src="./asset/dict.jpg" width="400"/></p>

***
> A lightweight online dictionary integration to the command line. No browsers. No paperbooks.
***

<p align=center><img src="./asset/demo.gif" width="500"/></p>

## Features
- Directly query words from the command line.
- Save words to your local dictionary.
- Add notes to saved words.
- Interactive word game to hone your vocabulary skills.
## Requirements
`Python` >= 3.6 and the following libraries are required.
```python
BeautifulSoup
pyfiglet
termcolor
requests
```
## Run
- Clone the git repository `./Vocab`.
- In `./Vocab` directory, type `./vocab`.
- Enjoy!

## Usage
### Query Mode
```
$ ./vocab -m query
```
<img src="./asset/query.gif" width="500"/>

### Dictionary Mode
```
$ ./vocab -m dict
```
<img src="./asset/dict.gif" width="500"/>

### Edit mode
```
$ ./vocab -m edit
```
<img src="./asset/edit.gif" width="500"/>

### Interactive Mode
```
$ ./vocab -m interactive
```
<img src="./asset/interactive.gif" width="500"/>

### Load Word List
```
$ ./vocab -f ./asset/gre.txt
```
<img src="./asset/file.gif" width="500"/>

### Count Total Words
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