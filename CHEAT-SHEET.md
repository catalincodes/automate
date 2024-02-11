# PYTHON CHEAT-SHEET

`len(string/list)` - number of elements in an array

`str(someVariable)`   --> casts a variable to a string
`int(someVariable)`   --> casts a variable into an int 
`float(someVariable)` --> casts a variable into a float

`if / elif / else` - `else if` looks weird - I know

`for i in range(n):` - for loop
`for i in range(start, end, step):`

`def functionName():`
`  return None` - same as return null in other langs

`def someFuntion():`
`  global someGlobalVariable` -  makes it so that you can modify a global declared variable

`try:`
`except: ZeroDivisionError`, or some other exception

`array[start:end]` - note that end is not inclusive
`del array[index]` - deletes the element at that index
`someVar in array` or `someVar not in array` - determine if someVar is in (or not in) array

`array = ['val1', 'val2', 'val3']`
`val1,val2,val3 = array` - each val gets placed in the right variable

`for index,item in enumerate(array):` - provides a for-loop that works well with arrays

`random.choice(array)` - gets a random value from the array
`array.index('element')` - gets the 1st occurrence of 'element' in array
`array.append('element')` - adds element at end of list
`array.insert(n, 'element')` - adds element at position n
`array.remove('element')` - removes the 1st occurrence of 'element'
`array.sort()` - sorts a list
`array.sort(reverse=true)` - sorts a list in reverse order

`print('Start of text ' + \`
`      'end of text')`

`(1,2,3)` - is a tuple -  it is immutable

`list(tuple([1,2,3])` - converting an array to a tuple and back again

`id(object)` - returns its memory address

`copy(object)` - returns a copy of the object with different memory address

`dict.keys()` - returns all the keys
`dict.values()` - returns all the values
`dict.items()` - returns tuples of key-value pairs

`for k,v in array.items():` - gives us key,value pairs to work with

`dict.get('key', defaultValue)` - gets the value for the 'key' or a defaultValue if 'key' does not exist
`dict.setDefault('key', defaultValue)` - if there is no value, it sets it to the default value else it leaves it alone

`r('c:\timey-wimey)` - raw string `c:\timey-wimey`, without the r in front, `\t` gets interpreted as a tab

```python
"""This is how
you make multiline comments
in Python
"""
```
`in` and `not in` - you can use `in` and `not in` with strings to find if a substring is present

`f('2+3 is {2+3}')` - This is called an f-string. It's basic string interpolation.

`upper(), lower()` - convert a string to uppercase or lowercase, respectively

`isupper(), islower()` - returns true if all characters in a string are uppercase or lowercase, respectively

`isalpha()` - is it a non-blank string made of letters (no numbers)

`isalnum()` - is it a non-blank string made of letters and numbers (alphanumeric)

`isdecimal()` - is it a non-blank string made of numbers (no letters)

`isspace()` - is it a non-blank string made of spaces, tabs and newlines

`istitle()` - is it a non-blank string with title case: `Such As This 123 Title`

`startswith(arg), endswith(arg)` - returns true if it stars or ends with `arg`

`val.join(listArg)` - Used like : `', '.join(['rats', 'dogs', 'cats'])` - this will result in `'rats, dogs, cats'

`val.split()` - Commonly used when parsing a file it returns a list of strings
```python
'My name is Simon'.split()
#['My','name','is','Simon']
```
One can also do `.split('\n')` if reading a file to split the file into an array of text rows.

`before, sep, after = 'Hello, world!'.partition(' ')` will result in `before` containing `'Hello,'` and `after` containing `'world!'`

`rjust(val), ljust(val), center(val)` - justifies to the left or right or center a text within the number of spaces passed as an argument

`strip(), rstrip(), lstrip()` - remove whitespaces from sides, right-side or left-side of a string

If you pass a series of characters in a string as parameters it will remove them as well.

`ord(), chr()` - convert characters to and from their unicode value.

`pyperclip.copy(arg)` - copies argument into the clipboard

`var = pyperclip.paste()` - retrieves clipboard string for storing
