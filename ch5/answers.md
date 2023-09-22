1. What does the code for an empty dictionary look like?
- {}

2. What does the diactionary value with a key 'foo' and a value 42 look like?
- {'foo':42}

3. What is the main difference between a dictionary and a list?
- The main difference is that a list is ordered, where the keys are 0, 1, 2, etc. whereas a dictionary is unordered.

4. What if you try to access spam['foo'] if spam is {'bar': 100}
- You get an error claiming that they key does not exist.

5. If a dictionary is stored in spam, what is the difference between the expressions "'cat' in spam" and "'cat' in spam.keys()"?
- "'cat' in spam" will check for 'cat' in both the keys and the values. "'cat' in spam.keys()" will only search for it in the dictionary's keys.

6. If a dictionary is stored in spam, what is the difference between the expressions "'cat' in spam" and "'cat' in spam.values()"?
- "'cat' in spam" will check for 'cat' in both the keys and the values. "'cat' in spam.values()" will only search for in the dictionary's values.

7. What is the shortcut key for the following code? 
- spam.setdefault('color', 'black')

8. What module and function can be used to "pretty print" dictionary values?
- pprint
