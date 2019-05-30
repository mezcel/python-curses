# python-curses

A Python CLI/terminal application which cycles through a scriptural Rosary.
Displayed text content is  provided by a .json file.

* based on the [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) UI layout
* the navigation algorithm used in this version is simpler and easier to follow. (overall less bloat)
* just NAB english, I allready did the latin version in [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) and [electron-container](https://github.com/mezcel/electron-container)

### Libraries used:

```py
import os		## computer control
import curses		## cli ui
import json		## json parse
import datetime		## sys clock
import textwrap		## wraping centence strings
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

I just use Python 2.7 from [python.org](https://www.python.org/downloads/windows/).

For runtime convenience, install "with environment variables" selected.

Install curses library:
```ps1
pip install --upgrade pip
python -m pip install windows-curses
```
