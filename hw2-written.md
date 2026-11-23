# HW 2 Solution

### Problem 1a

- 0- means that this byte is a one-byte (ASCII) character.
- 10- means that this byte is part of a multi-byte character, but it is not the first byte in that character.
- 110-, 1110-, and 11110- mean that this is the first byte in a two-, three-, or four-byte character, respectively.

### Problem 1b

UTF-8's "morphosyntax" helps the computer parse UTF-8 bytes into characters by making it easy to identify character boundaries. For example, it is easy to tell that the UTF-8 binary code
```
11101000 10101111 10101101 11101000 10101000 10000000 11100101 10101101 10100110
```
contains three characters, because there are 9 bytes in total and 6 of them begin with 10-. The prefixes also tell the computer how many 10- bytes to expect after each character boundary. If the wrong number of 10- bytes is encountered, then we know that the UTF-8 code is corrupt.

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

`break` terminates the most recently started active `for` loop. 

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

Biden's keywords include names of other politicians, such as Pence, McConnell, Pelosi, Schumer, and Kamala. The only politicians appearing among Trump's keywords are himself and his vice president (Trump and Vance), as well as former president William McKinley. On the other hand, Biden's keywords include mentions of Saint Augustine, referring to his Catholic heritage.

Biden's keywords contain noticeably more numbers than Trump's keywords: 108, 11, hundreds, Millions. There are also keywords related to finance and the economy, such as mortgage, accounting, inequity, and joblessness. The only number among Trump's keywords is billions.

### Problem 3e

- The top five keywords of the nomination acceptance speeches are: `"'s", "n't", "'re", "''", '``'`
- The top five keywords of the inaugural addresses are: `'"', 's', '."', 'cannot', 'object'`

You can find these keywords using the following code:
```python
nomination_fd = FreqDist(nomination_acceptance.words())
inaugural_fd = FreqDist(inaugural.words())
ref_fd = nomination_fd + inaugural_fd

print(hw1.freq_ratio(nomination_fd, ref_fd).most_common(5))
print(hw1.freq_ratio(inaugural_fd, ref_fd).most_common(5))
```

### Problem 3f

- The top five keywords of the DNC speeches are: `'doors', 'Booo', 'Kamala', 'corporations', 'Covenant'`
- The top five keywords of the RNC speeches are: `'Nobody', 'Boo-o-o', 'judges', 'broad', 'recently'`

You can find these keywords using the following code:

```python
# Identify DNC and RNC speeches
dnc_files = [f for f in nomination_acceptance.fileids() if f.endswith("DNC.html")]
rnc_files = [f for f in nomination_acceptance.fileids() if f.endswith("RNC.html")]

# Get Keywords
dnc_fd = FreqDist(nomination_acceptance.words(dnc_files))
rnc_fd = FreqDist(nomination_acceptance.words(rnc_files))

print(hw1.freq_ratio(dnc_fd, nomination_fd).most_common(5))
print(hw1.freq_ratio(rnc_fd, nomination_fd).most_common(5))
```

### Problem 3g

#### Inaugural Addresses vs. Nomination Acceptance Speeches

Many of the top keywords for the nomination acceptance speeches are subword tokens like 's, n't, 're, '', ``, 've, 'm, 'll, ca, and wo. These keywords seem to reflect differences in tokenization between the nomination acceptance speeches and the inaugural addresses.

More substantively, the nomination acceptance speeches are characterized by the use of names like Mr., Joe, and Kennedy, as well as second-person pronouns (yourself, you, your). These are mostly absent from the keywords of the inaugural addresses. Instead, the inaugural addresses are characterized by mentions of government departments and principles of political philosophy (Executive, commerce, sections, subjects, suffrage, commercial, predecessor). This suggests that nomination acceptance speeches generally have a more "casual" tone, whereas inaugural addresses generally have a more "formal" or "serious" tone. 

#### DNC vs. RNC Speeches

The DNC keywords reveal a focus on class politics (corporations, middle-class, 80th, wealthiest, enriched, minimum, rewarded) as well as the rights of underprivileged people (belong, disabilities, Rights). The RNC keywords reveal little about the Republican Party's policy preferences, apart from isolated mentions of political issues (Ford, aliens, NAFTA). 

For both parties, the second keyword is some variation of "boo," reflecting the energy and [collective effervescence](https://en.wikipedia.org/wiki/Collective_effervescence) of nominating conventions.
