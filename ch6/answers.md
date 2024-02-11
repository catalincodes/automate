1. What are escape characters? 
- These are characters that are used in case we want to use single quotes, double quotes, backslashes, new lines or tabs to a string.

2. What do the `\n` and `\t` escape characters represent? 
- New line and tab

3. How can you put a backslash character in a string?
- Just add two backslashes: `\\`

4. The string `"Howl's Moving Castle"` is a valid string. Why isn't it a problem that the single quote character in `Howl's` is not escaped?
- Because we've put the string in between double quotes. If you were to have put in single quotes you would have had a problem.

5. If you don't want to put `\n` in your string, how can you write a string with new lines in it?
- Using multiline strings `''' '''`

6. What do the following expressions evaluate to?
- 'Hello, world!'[1]    `e`
- 'Hello, world!'[0:5]  `Hello`
- 'Hello, world!'[:5]   `Hello`
- 'Hello, world!'[3:]...`lo, world!`

7. What do the following expressions evaluate to?
- 'Hello'.upper() `'HELLO'`
- 'Hello'.upper().isupper() `'True'`
- 'Hello'.upper().lower() `'hello'`

8. What do the following expressions evaluate to?
- 'Remember, remember, the fifth of November.'.split() `['Remember,','remember,',the','fifth','of','November']`
- '-'.join('There can be only one.'.split()) `'There-can-be-only-one`

9. What string methods can you use to right-justify, left-justify, and center a string?
- `rjust(n)`, `ljust(n)`, `center(n)` - where `n` is the number of characters in which to pad said string

10. How can you trim whitespace characters from the beginning or end of a string?
- `lstrip()`, `rstrip()` .. also `strip()` if you want both sides