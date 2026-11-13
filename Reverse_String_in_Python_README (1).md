# Reverse a String in Python

## 1. Problem statement

**Given a string, return a new string with its characters in reverse
order.**

Example:

``` python
text = "ABCDEF"
# Output: "FEDCBA"
```

The first character becomes the last, and the last character becomes the
first.

## 2. Important definition

A **string** is a sequence of characters. In Python, strings are
**immutable**: we cannot change their characters in place. So, we create
and return a new reversed string.

## 3. Method 1 --- Slicing (shortest method)

### Syntax

``` python
string[::-1]
```

-   `start`: where slicing begins
-   `stop`: where slicing ends (the stop position is not included)
-   `step`: how many positions to move
-   `-1`: move from right to left

### Code

``` python
text = "ABCDEF"
result = text[::-1]
print(result)  # FEDCBA
```

### Dry run

  Step   Character taken   Result
  ------ ----------------- --------
  1      F                 F
  2      E                 FE
  3      D                 FED
  4      C                 FEDC
  5      B                 FEDCB
  6      A                 FEDCBA

**Why use it?** It is short and easy when we simply need a reversed
copy.

## 4. Method 2 --- `reversed()` with `join()`

### Definition

-   `reversed()` returns an iterator that gives characters from last to
    first.
-   `"".join(...)` combines those characters into one string.
-   The empty string is the separator; here, it adds nothing between
    characters.

### Syntax and code

``` python
result = "".join(reversed(text))
```

``` python
text = "ABCDEF"
result = "".join(reversed(text))
print(result)  # FEDCBA
```

### Dry run

`reversed(text)` gives: `F → E → D → C → B → A`

`"".join(...)` combines them:

`F + E + D + C + B + A = "FEDCBA"`

**Why use it?** It clearly communicates reverse iteration and avoids
building a reversed string just to iterate over it.

## 5. Method 3 --- `for` loop

### Idea

Read each character from left to right, and place it at the beginning of
the result.

### Code

``` python
def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result

print(reverse_string("ABCD"))  # DCBA
```

### Dry run

  Loop    `char`   `result = char + result`
  ------- -------- --------------------------
  Start   ---      `""`
  1       A        `"A"`
  2       B        `"BA"`
  3       C        `"CBA"`
  4       D        `"DCBA"`

**Why use it?** It helps explain the logic without using a reverse
shortcut.

## 6. Method 4 --- `while` loop

### Idea

Start at the last index and move backwards until index `0`.

### Code

``` python
def reverse_string(text):
    result = ""
    index = len(text) - 1

    while index >= 0:
        result += text[index]
        index -= 1

    return result

print(reverse_string("ABCD"))  # DCBA
```

### Dry run

For `"ABCD"`, the indexes are `0:A`, `1:B`, `2:C`, `3:D`.

  `index`   `text[index]`   `result`
  --------- --------------- ----------
  3         D               D
  2         C               DC
  1         B               DCB
  0         A               DCBA

Then `index` becomes `-1`; the condition `index >= 0` is false, so the
loop stops.

## 7. Method 5 --- Recursion

### Definition

**Recursion** means a function calls itself.

A recursive solution needs: - **Base case:** the condition that stops
further calls. - **Recursive case:** the part that calls the function
again with a smaller input.

### Code

``` python
def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]

print(reverse_string("ABCD"))  # DCBA
```

### Dry run

The function calls become:

``` text
reverse_string("ABCD")
reverse_string("BCD") + "A"
reverse_string("CD")  + "B" + "A"
reverse_string("D")   + "C" + "B" + "A"
"D" + "C" + "B" + "A"
"DCBA"
```

**When use it?** To understand recursive problem-solving. For long
strings, recursion can hit Python's recursion limit, so it is usually
not the practical choice here.

## 8. Method 6 --- `reduce()` (alternative)

### Definition

`reduce()` repeatedly combines items and keeps one accumulated result.
It is imported from `functools`.

``` python
from functools import reduce

text = "ABCD"
result = reduce(lambda a, b: b + a, text)
print(result)  # DCBA
```

### Dry run

  Character added   Accumulated result
  ----------------- --------------------
  A                 A
  B                 BA
  C                 CBA
  D                 DCBA

This is an alternative technique; beginners usually find slicing or
loops easier to read.

## 9. Important difference: reverse vs reverse sorting

These operations do different jobs.

``` python
text = "CAB"

print(text[::-1])                       # BAC
print("".join(sorted(text, reverse=True)))  # CAB
```

-   **Reverse:** changes the order of the existing characters.
-   **Reverse sorting:** arranges characters in descending sorted order.

`sorted()` returns a list, so `join()` is used to make it a string
again.

## 10. Common interview questions

**Q1. Can we reverse a Python string in place?**\
No. Strings are immutable. We create a new reversed string.

**Q2. What does `[::-1]` mean?**\
It uses a step of `-1`, so it reads the string from right to left.

**Q3. What does `reversed()` return?**\
It returns an iterator, not a string. Use `"".join(reversed(text))` to
build a string.

**Q4. Why do we use `len(text) - 1` in the `while` loop?**\
Because Python indexes start at `0`, so the last index is one less than
the string length.

**Q5. What is the base case in recursion?**\
When the string has zero or one character, return it as it is.

**Q6. Does reversing a string change the original string?**\
No. These methods create a new result; the original string remains
unchanged.

## 11. Interview explanation (natural English)

"If I need to reverse a string in Python, I can use different methods.
The simplest method is slicing with `[::-1]`, which reads the string
from right to left. I can also use `reversed()` with `join()`. If the
interviewer asks me not to use a shortcut, I can solve it using a `for`
loop or a `while` loop. Python strings are immutable, so I create a new
string instead of changing the original one."

## 12. Quick summary

  Method                    Main idea                         Best use
  ------------------------- --------------------------------- ------------------------
  Slicing `[::-1]`          Read right to left                Quick solution
  `reversed()` + `join()`   Iterator + combine                Clear Python approach
  `for` loop                Prepend each character            Explain basic logic
  `while` loop              Start at last index               Practice index tracing
  Recursion                 Function calls itself             Learn recursion
  `reduce()`                Combine characters cumulatively   Alternative approach

**Remember:** reversing is not the same as sorting in reverse order.
