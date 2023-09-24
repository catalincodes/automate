# PYTHON CHEAT-SHEET

`len(string/list)` - number of elements in an array

str(someVariable)   -->-\                              /--> a string

int(someVariable)   -->-||---> Cast a variable into ->-|--> an int 

float(someVariable) -->-/                              \--> a float

if / elif / else - `else if` looks weird - I know

for i in range(n): - for loop
for i in range(start, end, step):

def functionName():
  return None - same as return null in other langs

def someFuntion():
  global someGlobalVariable -  makes it so that you can modify a global declared variable

try:
except: ZeroDivisionError, or some other exception

array[start:end] - note that end is not inclusive
del array[index] - deletes the element at that index
`someVar in array` or `someVar not in array` - determine if someVar is in (or not in) array

array = ['val1', 'val2', 'val3']
val1,val2,val3 = array - each val gets placed in the right variable

for index,item in enumerate(array): - provides a for-loop that works well with arrays

random.choice(array) - gets a random value from the array
array.index('element') - gets the 1st occurrence of 'element' in array
array.append('element') - adds element at end of list
array.insert(n, 'element') - adds element at position n
array.remove('element') - removes the 1st occurrence of 'element'
array.sort() - sorts a list
array.sort(reverse=true) - sorts a list in reverse order

print('Start of text ' + \
      'end of text')

(1,2,3) - is a tuple -  it is immutable

list(tuple([1,2,3]) converting an array to a tuple and back again

id(object) - returns its memory address

copy(object) - returns a copy of the object with different memory address

dict.keys - returns all the keys
dict.values - returns all the values
dict.items - returns tuples of key-value pairs

for k,v in array.items() - gives us key,value pairs to work with

dict.get('key', defaultValue) - gets the value for the 'key' or a defaultValue if does not exist
dict.setDefault('key', defaultValue) - if there is no value, it sets it to the default value else
it leaves it alone


