#! python3
# bulletPointAdder.py - Adding Bullets to Wiki Markup

import pyperclip

clipboard = pyperclip.paste()
rowlist = clipboard.split('\n')

for index,item in enumerate(rowlist):
    rowlist[index] = f'* {item}'

clipboard = '\n'.join(rowlist)

pyperclip.copy(clipboard)