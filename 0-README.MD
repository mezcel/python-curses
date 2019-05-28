# python-curses

### A python Rosary terminal app

* based on [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal)
* just NAB english, I allready did the latin version in [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) and [electron-container](https://github.com/mezcel/electron-container)
* no extra content yet (feast days, web scrap daily mass, theme decoration, audio, refference guide), like in [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) and [electron-container](https://github.com/mezcel/electron-container)

#### Scratch-pad preparations:

* preparing some script for a python app

* a python learning application using curses

* Debugging: Tagged out Mysteries I have not updated the Json for yet. [ ```"rosaryBeadID": 0,``` though ```"rosaryBeadID": 78,``` ]

---

Chars to watch out for when using strings in ```.json``` processed by ```python```:

```json
/* I get errors if I don't escape them:
	single quotes and apostrophes, u'\u2019'
	[ , u'\u201c'
	]
	double quotes
*/

/* Fix:
	\'
	\\'
	\\\[
	\\\]
	\"
*/

```

---

Simplified navigational calculations by defining position within json. I allready did it the 'monstrosity' alogrithm way in [jq-tput-terminal](https://github.com/mezcel/jq-tput-terminal) and [electron-container](https://github.com/mezcel/electron-container)

```json
{
	"rosaryBead": [
			{
				"rosaryBeadID": 0,
				"beadIndex": 0,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 1,
				"scriptureIndex": 0,
				"messageIndex": 0,

				/* additional new meta */

				"loopBody": 1,	/* 1 = yes, used to flag intro and outros */
				"smallbeadPercent": 1,	/* 1 to 10 */
				"mysteryPercent" 1,		/* 1 to 50 */
			}
}
```
