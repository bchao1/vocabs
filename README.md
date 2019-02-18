# Vocab
<p align=center><img src="./asset/dict.jpg" width="400"/></p>

***
> A lightweight online dictionary integration to the command line. No browsers. No paperbooks.
***

![hello](./asset/demo.gif)
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
### Query mode
```
$ ./vocab
$ ./vocab -m query
```
### Edit mode
```
$ ./vocab -m edit
```
### Interactive mode
```
$ ./vocab -m interactive
```
### Reset local dictionary
```
$ ./vocab -r
```