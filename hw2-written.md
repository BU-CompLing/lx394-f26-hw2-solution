# HW 2 Solution

### Problem 1a

- 0- means that this byte is a one-byte (ASCII) character.
- 10- means that this byte is part of a multi-byte character, but it is not the first byte in that character.
- 110-, 1110-, and 11110- mean that this is the first byte in a two-, three-, or four-byte character, respectively.

### Problem 1b

UTF-8's "morphosyntax" helps the computer parse UTF-8 bytes into characters by making it easy to identify character boundaries. For example, it is easy to tell that the UTF-8 binary code
```
01011001 11000011 10111010 01101100 11000011 10111001
```
contains four characters, because there are 6 bytes in total and 2 of them begin with 10-. The prefixes also tell the computer how many 10- bytes to expect after each character boundary. If the wrong number of 10- bytes is encountered, then we know that the UTF-8 code is corrupt.

### Problem 1d

The `try`–`except` block allows code to continue running after triggering a runtime error. By default, the code in a `try` block always runs. If it triggers an error, then instead of crashing the program, the code in the `except` block is run instead.

A `try`–`except` block can specify what kinds of errors trigger the `except` block. For example, in the following code snippet:
```python
try:
    raise NotImplementedError
    print(5 / 0)
except ZeroDivisionError:
    print("I tried to divide by zero!")
```
the code actually crashes with a `NotImplementedError` because the `except` block is only triggered by a `ZeroDivisionError`.
