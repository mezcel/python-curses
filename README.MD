# python-curses

A Python CLI/terminal application which cycles through a scriptural Rosary.
Displayed text content is  provided by a .json file.

* Visual layout based on [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal).
* Light weight (lighter and less complicated than my other rosary apps)
    * I did make a [modular-version](https://github.com/mezcel/python-curses/tree/master/module-version) of this same app, just for jollies

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

There are some differences between Python v2.x and Python v3.x regarding parsing ```.json```, so I included both techniques within the code.

### Debian & WLS

```sh
sudo apt-get install python-pip python3 python3-pip
```

### Arch

```sh
sudo pacman -S --needed python python2
```

### Win10

I just use Python 2.7 from [python.org](https://www.python.org/downloads/windows/), but it also works on Python 3.7

For runtime convenience, install "with environment variables" selected.

Install curses library:

```sh
pip install --upgrade pip
python -m pip install windows-curses
```

---

## Standalone executable

* [distutils](https://docs.python.org/3/distutils/builtdist.html), python3

* [pyinstaller](https://pypi.org/project/PyInstaller/), linux

* [py2exe](https://pypi.org/project/py2exe/), win10
