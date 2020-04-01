## module-version

This is the same app, but I broke it down into modules.

There was no need (functional or performance) to do this, but I wanted to compartmentalize the resources used in this app

---

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

I just use Python 2.7 from [python.org](https://www.python.org/downloads/windows/), but it also works on Python 3.7

For runtime convenience, install "with environment variables" selected.

Install curses library:

```sh
## python package
pip install --upgrade pip
python -m pip install windows-curses
```