import pypandoc

content = r"""# Reverse Each Word in a Sentence – Python

## 1. Problem statement

Given a sentence, reverse the letters of **each word**, but keep the word order unchanged.

**Example**

```python
sentence = "Hello World"
# Output: olleH dlroW
```

This is different from reversing the whole sentence or changing the order of words.

## 2. Recommended method: `for` loop + slicing + `join()`

**Recommendation:** For a fresher interview, learn and explain the `for` loop method first. It makes your logic clear: split the sentence, reverse each word, store the result, and join the words. After that, you can mention list comprehension as a shorter Pythonic version.

```python
sentence = "Hello World"

words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print(result)
```

**Output**
```text
olleH dlroW
```

### Syntax and definitions

- `sentence.split()` – splits a string into a list of words. With no argument, it treats consecutive whitespace as one separator.
- `word[::-1]` – returns the characters of `word` in reverse order.
- `list.append(value)` – adds one item to the end of a list.
- `" ".join(words)` – combines strings from an iterable, placing one space between them.

**Slice syntax:** `string[start:stop:step]`

In `word[::-1]`, the start and stop are omitted, and `step = -1` means move backwards through the string.

### Dry run

Input: `"Hello World"`

| Step | `word` | `word[::-1]` | `reversed_words` |
|---|---|---|---|
| Start | — | — | `[]` |
| 1 | `"Hello"` | `"olleH"` | `["olleH"]` |
| 2 | `"World"` | `"dlroW"` | `["olleH", "dlroW"]` |

Finally:

```python
" ".join(["olleH", "dlroW"])
```

Result: `"olleH dlroW"`

### Why use this method?

- The steps are easy to understand and explain.
- It is beginner-friendly and shows the problem-solving logic.
- It avoids putting the entire solution into one line.

### Complexity

Let `n` be the total number of characters in the sentence.

- **Time:** `O(n)` – splitting, reversing all characters, and joining process the sentence's characters a constant number of times.
- **Space:** `O(n)` – the word list, reversed words, and result require space proportional to the input.

## 3. Other methods

### Method 2: List comprehension

```python
sentence = "Hello World"

result = " ".join([word[::-1] for word in sentence.split()])
print(result)
```

**Output**
```text
olleH dlroW
```

**How it works:** The list comprehension loops through each word, reverses it, and creates a new list. `join()` combines the reversed words.

**Complexity:** Time `O(n)`, space `O(n)`.

**When to use:** Use it when you are comfortable with Python and want concise, readable code.

### Method 3: `map()` and `lambda`

```python
sentence = "Hello World"

result = " ".join(map(lambda word: word[::-1], sentence.split()))
print(result)
```

**Output**
```text
olleH dlroW
```

**How it works:**
- `lambda word: word[::-1]` is a small anonymous function that reverses one word.
- `map(function, iterable)` applies that function to every word.
- `join()` combines the results.

**Complexity:** Time `O(n)`, space `O(n)` for the split words and final output. `map()` itself produces an iterator.

**When to use:** Use it when you understand functional-style Python. It is not necessary for a beginner interview answer.

### Method 4: `reversed()`

```python
sentence = "Hello World"

result = " ".join("".join(reversed(word)) for word in sentence.split())
print(result)
```

**Output**
```text
olleH dlroW
```

**How it works:** `reversed(word)` gives the characters in reverse order. The inner `join()` turns those characters back into a string; the outer `join()` combines the words.

**Complexity:** Time `O(n)`, space `O(n)` overall for the output and intermediate data.

**When to use:** Use it if the interviewer asks you to reverse characters without slicing.

## 4. Important note: spaces

`split()` without an argument treats multiple spaces, tabs, and newlines as separators and `join()` puts one normal space between words.

```python
sentence = "Hello   World"
print(" ".join(word[::-1] for word in sentence.split()))
```

Output:
```text
olleH dlroW
```

If exact spaces must be preserved, use `split(" ")` and join with `" "`:

```python
sentence = "Hello   World"
result = " ".join(word[::-1] for word in sentence.split(" "))
print(result)
```

Output:
```text
olleH   dlroW
```

This preserves repeated ordinary spaces. Tabs and newlines need a different whitespace-preserving approach.

## 5. Interview questions

**Q1. What is the difference between reversing each word and reversing a sentence?**

Reversing each word changes the letters inside each word but keeps the word order. Reversing a sentence may reverse the whole character sequence or the word order, depending on the requirement.

**Q2. Why do we use `split()`?**

To separate the sentence into individual words so that we can reverse each word separately.

**Q3. What does `[::-1]` mean?**

It is slicing with a step of `-1`, which reads the string from the end to the beginning.

**Q4. Why do we use `append()`?**

To store each reversed word in the result list.

**Q5. Why do we use `join()`?**

To combine the reversed words into one sentence with spaces between them.

**Q6. What is the time and space complexity?**

Time is `O(n)` because the characters are processed a constant number of times. Space is `O(n)` because we create lists and a result string proportional to the input.

**Q7. Can we solve it in one line?**

Yes. List comprehension with slicing and `join()` can solve it in one line.

## 6. Interviewee explanation (natural English)

“I will first split the sentence into words. Then I will use a loop to visit each word and reverse it using `[::-1]`. I will store every reversed word in a new list. Finally, I will use `join()` to combine the words with spaces. This keeps the original word order and reverses only the letters in each word. The time and space complexities are both `O(n)`.”

## 7. Quick summary

- **Best method to explain first in an interview:** `for` loop + slicing + `append()` + `join()`.
- **Short and Pythonic method:** list comprehension + slicing + `join()`.
- **Alternative approaches:** `map()` with `lambda`, or `reversed()`.
- **Time complexity:** `O(n)`.
- **Space complexity:** `O(n)`.
- Always confirm whether the question expects normalised spaces or exact whitespace preservation.
"""
pypandoc.convert_text(content, 'md', format='md', outputfile='/mnt/data/reverse_each_word_python_README.md', extra_args=['--standalone'])
print("Created README.")

Reverse Each Word in a Sentence – Python
This is a common Python coding interview question. The important point is to understand the difference between reversing each word and reversing the entire sentence.
1. Problem statement
Question: Given a sentence, reverse every individual word without changing the original order of the words.

Example:
Input
"Hello World"




Output
"olleH dlroW"



Each word is reversed, but the word order stays the same.

2. Recommended method – For loop + slicing
Best for fresher interviews
I recommend this method because the interviewer can easily understand your logic and problem-solving approach.
Code
sentence = "Hello World"words = sentence.split()reversed_words = []for word in words:    reversed_words.append(word[::-1])result = " ".join(reversed_words)print(result)



Output:
olleH dlroW


Syntax and definitions
Syntax	Definition
split()	Divides a sentence into words.
[::-1]	Reverses a string using slicing.
append()	Adds an item to a list.
join()	Combines multiple strings into one string.

Dry run (step-by-step tracing)
Input:
sentence = "Hello World"



Step 1: Split the sentence
words = sentence.split()



Result:
["Hello", "World"]



Step 2: Create an empty list
reversed_words = []



Step 3: Iterate through each word
Iteration	Word	Reversed word	List
1	Hello	olleH	["olleH"]
2	World	dlroW	["olleH", "dlroW"]

Step 4: Join the reversed words
result = " ".join(reversed_words)



Result:
"olleH dlroW"



Step 5: Print the result
olleH dlroW


3. Why, what, how, where and when?
Question	Simple explanation
What?	Reverse the letters of every word.
Why?	To transform each word independently.
Purpose?	To practise strings, slicing, loops and lists.
How?	Split → Loop → Reverse → Append → Join.
Where?	Python coding interviews and string manipulation problems.
When?	When a problem asks to reverse individual words without changing their order.

4. Other methods
Method 2: List comprehension
Most Pythonic
sentence = "Hello World"result = " ".join(    [word[::-1] for word in sentence.split()])print(result)



Output:
olleH dlroW


How does it work?
- sentence.split() creates a list of words.
- word[::-1] reverses each word.
- List comprehension creates a new list.
- join() combines the reversed words.
When to use? When you want shorter and cleaner Python code.
Method 3: Map and Lambda
sentence = "Hello World"result = " ".join(    map(lambda word: word[::-1], sentence.split()))print(result)



Output:
olleH dlroW


How does it work?
- lambda creates a small anonymous function.
- map() applies that function to every word.
- join() combines the results.
When to use? When you understand functional programming concepts in Python.
Method 4: Using reversed()
sentence = "Hello World"result = " ".join(    "".join(reversed(word))    for word in sentence.split())print(result)



Output:
olleH dlroW


How does it work?
- reversed(word) reads the characters backwards.
- Inner join() converts the reversed characters into a string.
- Outer join() combines all the words.
When to use? When the interviewer asks you to reverse a string without using slicing.
5. Time and space complexity
Let n represent the total number of characters in the sentence.
Method	Time complexity	Space complexity
For loop	O(n)	O(n)
List comprehension	O(n)	O(n)
Map + Lambda	O(n)	O(n)
reversed()	O(n)	O(n)

Why O(n) time?

We process each character a constant number of times while splitting, reversing and joining the words. Therefore, the time complexity is O(n).

Why O(n) space?

We create additional lists and a new output string. Their total storage grows proportionally to the input size. Therefore, space complexity is O(n).
6. Important interview questions
Q1. Why do we use split()?

To divide a sentence into individual words.

Q2. What does [::-1] mean?

It is string slicing with a negative step. It reads the characters from the end to the beginning.

Q3. Why do we use append()?

To add each reversed word into a new list.

Q4. Why do we use join()?

To combine all reversed words into a single sentence.

Q5. Does this program change the original sentence?

No. Python strings are immutable. We create a new result string.

Q6. What is the difference between a loop and list comprehension?

A loop uses multiple statements to perform the operation. List comprehension performs the same operation in a shorter expression.

Q7. What is the complexity?

Time complexity is O(n), and space complexity is O(n).
7. Interviewee explanation – Natural English
You can explain the solution like this:
"First, I will split the sentence into individual words using split().

Then, I will use a for loop to iterate through each word and reverse it using string slicing [::-1].

I will store each reversed word in a new list using append().

Finally, I will use join() to combine all the reversed words into a single sentence.

The time complexity is O(n), and the space complexity is O(n)."
 Copy answer

8. Final revision summary
Remember this execution flow:
split() – Separate words


for loop – Visit each word


[::-1] – Reverse each word


append() – Store reversed words


join() – Combine the words


My recommendation:
- First learn the for-loop method.
- Practise the dry run.
- Learn list comprehension as an alternative.
- Remember O(n) time and O(n) space.

README file:  Download Reverse Each Word in a Sentence – README.md

9. Test your understanding
Python interview practice
0/4 answered

Q1. Which method separates a sentence into individual words?

join()

split()

append()




Q2. What does word[::-1] do?

Sorts the word

Reverses the word

Removes the word




Q3. Why do we use join()?

To combine strings

To reverse a list

To count characters




Q4. What is the time complexity?

O(1)

O(n)

O(n²).

------------------------------------------------
Reverse Each Word in a Sentence -- Python
1. Problem statement
Given a sentence, reverse the letters of each word, but keep the
word order unchanged.

Example
sentence = "Hello World"
# Output: olleH dlroW
This is different from reversing the whole sentence or changing the
order of words.
2. Recommended method: for loop + slicing + join()
Recommendation: For a fresher interview, learn and explain the for
loop method first. It makes your logic clear: split the sentence,
reverse each word, store the result, and join the words. After that, you
can mention list comprehension as a shorter Pythonic version.
sentence = "Hello World"

words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print(result)
Output
olleH dlroW
Syntax and definitions
- sentence.split() -- splits a string into a list of words. With no
  argument, it treats consecutive whitespace as one separator.
- word[::-1] -- returns the characters of word in reverse order.
- list.append(value) -- adds one item to the end of a list.
- " ".join(words) -- combines strings from an iterable, placing one
  space between them.
Slice syntax: string[start:stop:step]

In word[::-1], the start and stop are omitted, and step = -1 means
move backwards through the string.
Dry run
Input: "Hello World"

  Step    word      word[::-1]   reversed_words
  Start   ---         ---            []
1       "Hello"   "olleH"      ["olleH"]
2       "World"   "dlroW"      ["olleH", "dlroW"]

Finally:
" ".join(["olleH", "dlroW"])
Result: "olleH dlroW"
Why use this method?
- The steps are easy to understand and explain.
- It is beginner-friendly and shows the problem-solving logic.
- It avoids putting the entire solution into one line.
Complexity
Let n be the total number of characters in the sentence.
- Time: O(n) -- splitting, reversing all characters, and joining
  process the sentence's characters a constant number of times.
- Space: O(n) -- the word list, reversed words, and result
  require space proportional to the input.
3. Other methods
Method 2: List comprehension
sentence = "Hello World"

result = " ".join([word[::-1] for word in sentence.split()])
print(result)
Output
olleH dlroW
How it works: The list comprehension loops through each word,
reverses it, and creates a new list. join() combines the reversed
words.

Complexity: Time O(n), space O(n).

When to use: Use it when you are comfortable with Python and want
concise, readable code.
Method 3: map() and lambda
sentence = "Hello World"

result = " ".join(map(lambda word: word[::-1], sentence.split()))
print(result)
Output
olleH dlroW
How it works: - lambda word: word[::-1] is a small anonymous
function that reverses one word. - map(function, iterable) applies
that function to every word. - join() combines the results.

Complexity: Time O(n), space O(n) for the split words and final
output. map() itself produces an iterator.

When to use: Use it when you understand functional-style Python. It
is not necessary for a beginner interview answer.
Method 4: reversed()
sentence = "Hello World"

result = " ".join("".join(reversed(word)) for word in sentence.split())
print(result)
Output
olleH dlroW
How it works: reversed(word) gives the characters in reverse
order. The inner join() turns those characters back into a string; the
outer join() combines the words.

Complexity: Time O(n), space O(n) overall for the output and
intermediate data.

When to use: Use it if the interviewer asks you to reverse
characters without slicing.
4. Important note: spaces
split() without an argument treats multiple spaces, tabs, and newlines
as separators and join() puts one normal space between words.
sentence = "Hello   World"
print(" ".join(word[::-1] for word in sentence.split()))
Output:
olleH dlroW
If exact spaces must be preserved, use split(" ") and join with " ":
sentence = "Hello   World"
result = " ".join(word[::-1] for word in sentence.split(" "))
print(result)
Output:
olleH   dlroW
This preserves repeated ordinary spaces. Tabs and newlines need a
different whitespace-preserving approach.
5. Interview questions
Q1. What is the difference between reversing each word and reversing a
sentence?

Reversing each word changes the letters inside each word but keeps the
word order. Reversing a sentence may reverse the whole character
sequence or the word order, depending on the requirement.

Q2. Why do we use split()?

To separate the sentence into individual words so that we can reverse
each word separately.

Q3. What does [::-1] mean?

It is slicing with a step of -1, which reads the string from the end
to the beginning.

Q4. Why do we use append()?

To store each reversed word in the result list.

Q5. Why do we use join()?

To combine the reversed words into one sentence with spaces between
them.

Q6. What is the time and space complexity?

Time is O(n) because the characters are processed a constant number of
times. Space is O(n) because we create lists and a result string
proportional to the input.

Q7. Can we solve it in one line?

Yes. List comprehension with slicing and join() can solve it in one
line.
6. Interviewee explanation (natural English)
"I will first split the sentence into words. Then I will use a loop to
visit each word and reverse it using [::-1]. I will store every
reversed word in a new list. Finally, I will use join() to combine the
words with spaces. This keeps the original word order and reverses only
the letters in each word. The time and space complexities are both
O(n)."
7. Quick summary
- Best method to explain first in an interview: for loop +
  slicing + append() + join().
- Short and Pythonic method: list comprehension + slicing +
  join().
- Alternative approaches: map() with lambda, or reversed().
- Time complexity: O(n).
- Space complexity: O(n).
- Always confirm whether the question expects normalised spaces or
  exact whitespace preservation.

  <!-- ------------------------------------------------- -->

  
