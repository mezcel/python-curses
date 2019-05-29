# python-curses 

A Python CLI/terminal application which cycles through a scriptural Rosary. 
Displayed text content is  provided by a .json file.

* based on the [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) UI layout
* the navigation algorithm used in this version is simpler and easier to follow. (overall less bloat)
* just NAB english, I allready did the latin version in [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) and [electron-container](https://github.com/mezcel/electron-container)

### Libraries used:

```py
import os
import curses
import json
import datetime
```

---

## Install Python

### Debian & WLS

```sh
sudo apt-get install python-pip python3 python3-pip
```

### Arch
```sh
sudo pacman -S --needed python python2
```

### Win10

I just use Python 2.7 from [python.org](https://www.python.org/downloads/windows/). I think all the cool kids are on v3, idk

Install "with Environment Variables" when the installer makes it abaile to do so. If not... you will manually have to do all of that stuff.

Install curses library:
```ps1
pip install --upgrade pip
python -m pip install windows-curses
```