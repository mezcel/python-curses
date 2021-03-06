# python-curses

A Python CLI/terminal application which cycles through a scriptural Rosary. Displayed text content is  provided by a .json file.
* Scripture quotes are taken from [usccb.org](http://usccb.org/bible/books-of-the-bible/index.cfm). Text readings are stored within the ```module-version/rosaryJSON-nab.json``` file.

* Visual UI/UX layout based on [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal).
* Light weight (lighter and less complicated than my other rosary apps)
    * I did make a [modular-version](https://github.com/mezcel/python-curses/tree/master/module-version) of this same app, just for jollies and compartmentalization of imported python library packages.

### Libraries used:

```py
import os		## computer control
import curses		## cli ui
import json		## json parse
import datetime		## sys clock
import textwrap		## wrapping sentence strings
import platform		## identify which python version
```

---

## Install Python Platform

[https://www.python.org/downloads](https://www.python.org/downloads/)

There are some differences between Python v2.x and Python v3.x regarding parsing ```.json```, so I included both techniques within the code.

### Debian & WLS

```sh
## Linux package
sudo apt-get install python-pip python3 python3-pip

## python package
pip install term
```

### Arch

```sh
## Linux package
sudo pacman -S --needed python python2

## python package
pip install term
```

### Win10

I just use [Python 2.7.x](https://www.python.org/downloads/release/python-2717/) from [python.org](https://www.python.org/downloads/windows/), but it also works on the latest Python 3.7.x

For runtime convenience, install "with environment variables" selected.

Install curses library:

```sh
## python package
pip install --upgrade pip
python -m pip install windows-curses
```

---

## Demo

[Animated Demo](https://asciinema.org/a/315411)

[![asciicast](https://asciinema.org/a/315411.svg)](https://asciinema.org/a/315411)

---

## Package a standalone executable

* [distutils](https://docs.python.org/3/distutils/builtdist.html), python3

* [pyinstaller](https://pypi.org/project/PyInstaller/), linux

* [py2exe](https://pypi.org/project/py2exe/), win10