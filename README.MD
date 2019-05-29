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