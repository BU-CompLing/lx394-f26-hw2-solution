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

### Problem 1e

The code `a.join(b)` creates a string with all the items in `b` concatenated together, separated by `a`. 

`a.join(b)` still works if `b` is a `set[str]`, but no guarantees can be made about which order the items of `b` will appear in the concatenated string.

`a.join(b)` _does not_ work if `b == range(10)`. It only works if `b` is a collection of strings.

### Problem 1f

`break` terminates the most recently started `for` loop. 

### Problem 1g

The function `word_tokenize` splits up a string into tokens, represented as a `list[str]`.

### Problem 2a

```python
'\x80\x99', 'McKinley', 'Thatâ', 'Iâ', 'Itâ'
```

### Problem 2b

In the Latin-1 encoding, `'â'` [is represented as](https://cs.stanford.edu/people/miles/iso8859.html) E2 in hexadecimal or 11100010 in binary. In UTF-8, this would be the first byte in a 3-byte character.

Based on the concordance for `'\x80\x99'` in Donald Trump's 2025 inauguration speech, it seems that each occurrence of an apostrophe has been replaced by `'â\x80\x99'`. A likely explanation for this is that the apostrophe is represented by a 3-byte character in UTF-8. The first byte is 11100010 (which is `'â'` in Latin-1), but the other two bytes do not have any meaning in Latin-1, so Python simply prints them as a description of the two bytes.

In fact, [it turns out](https://www.cogsci.ed.ac.uk/~richard/utf-8.cgi?input=e2+80+99&mode=bytes) that E2 80 99 is the hexadecimal UTF-8 representation of the character `'’'` (`RIGHT SINGLE QUOTATION MARK`).

### Problem 2d

Both speeches contain keywords that reflect the political priorities of each new president. For Trump, these include drill, Hispanic, hurricane, illegally, and Deal; for Biden, these include virus, uniting, pandemic, protesters, marching, and demonization.

Biden's keywords include names of other politicians, such as Pence, McConnell, Pelosi, Schumer, and Kamala. The only politicians appearing among Trump's keywords are himself and vice president (Trump and Vance), as well as former president William McKinley. On the other hand, Biden's keywords include mentions of Saint Augustine, referring to his Catholic heritage.

Biden's keywords contain noticeably more numbers than Trump's keywords: 108, 11, hundreds, Millions. There are also keywords related to finance and the economy, such as mortgage, accounting, inequity, and joblessness. The only number among Trump's keywords is billions.

### Problem 2e
- `'CAP'` refers to words starting with a capital letter.
- `'NNP'` refers to proper nouns.
- `'VBD'` refers to past-tense verbs.
- `'PRIV'` refers to private verbs.

### Problem 2g

Key feature analysis shows that Trump's 2025 inaugural address makes prolific use of universal quantifiers: nobody, everybody, everything, QUPR (quantifying pronouns), everyone, anything. Trump's speech is also characterized by its use of interjections (UH), amplifiers (AMP), and second-person pronouns (you, SPP2). These key features suggest that Trump's speech has an overall "confrontational" style.

In contrast, Biden's speech is must less confrontational and much more conciliatory. Biden's key features include hedge words (HDG) and contractions (CONT), as well as question marks (QUES) and the pronouns "us" and "we." These features make Biden's speech more "conversational" in style, engaging the audience in dialogue as an equal and casual participant.

