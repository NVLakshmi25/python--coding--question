Python: Character Frequency and Finding Repeating Characters
Your examples cover two related interview problems:
1. Count the frequency of every character in a string.
2. Find only repeating characters whose frequency is greater than 1.
Let's understand both with simple English, code, dry runs, outputs and interview explanations.
Part 1: Count Character Frequency
1. Problem definition
Character frequency means counting how many times each character appears in a string.

Input:
text = "banana"



Output:
{'b': 1, 'a': 3, 'n': 2}


Why, purpose, where and when?
- Why: To identify how frequently each character appears.
- Purpose: Count repeated and unique characters.
- Where: Text processing, data analysis and word processing.
- When: When an interviewer asks you to count characters or find duplicates.
Method 1: Using collections.Counter() – Easiest
from collections import Countertext = "banana"freq = dict(Counter(text))print(freq)



Output:
{'b': 1, 'a': 3, 'n': 2}


Syntax:
Counter(iterable)



How does it work?

Counter() automatically counts how many times each character appears.

Dry run:
b → 1
a → 1
n → 1
a → 2
n → 2
a → 3


Final result:
{'b': 1, 'a': 3, 'n': 2}



Interview explanation:

"I use the Counter class from the collections module. It automatically counts the frequency of each character and returns a dictionary-like object."

Complexity:
- Time: O(n) average — It processes each character once.
- Space: O(k) — It stores only unique characters and their counts.
Method 2: Using dictionary .get() – Recommended
text = "banana"freq = {}for char in text:    freq[char] = freq.get(char, 0) + 1print(freq)



Output:
{'b': 1, 'a': 3, 'n': 2}


Syntax:
dictionary.get(key, default_value)



How does .get() work?
- If the key exists, it returns its current value.
- If the key does not exist, it returns the default value.
For example:
freq.get('a', 0)



If a is not present, it returns 0.

Then:
freq[char] = freq.get(char, 0) + 1



It gets the existing count, adds 1 and updates the dictionary.

Dry run:
Character	freq.get(char, 0)	Updated dictionary
b	0	{'b': 1}
a	0	{'b': 1, 'a': 1}
n	0	{'b': 1, 'a': 1, 'n': 1}
a	1	{'b': 1, 'a': 2, 'n': 1}
n	1	{'b': 1, 'a': 2, 'n': 2}
a	2	{'b': 1, 'a': 3, 'n': 2}

Interview explanation:

"I create an empty dictionary and iterate through the string. I use the get() method to retrieve the current count. If the character is new, it returns zero. Then I add one and update its frequency."

Complexity:
- Time: O(n) average — One loop with O(1) average dictionary operations.
- Space: O(k) — Only unique characters are stored.
Method 3: Using if-else loop – Beginner-friendly
text = "banana"freq = {}for char in text:    if char in freq:        freq[char] += 1    else:        freq[char] = 1print(freq)



Output:
{'b': 1, 'a': 3, 'n': 2}


How does it work?
- freq = {} creates an empty dictionary.
- if char in freq checks whether the character exists.
- freq[char] += 1 increases its count.
- else adds a new character with count 1.
Dry run:
b → New → 1
a → New → 1
n → New → 1
a → Exists → 2
n → Exists → 2
a → Exists → 3


Interview explanation:

"I use a dictionary to store characters and their frequencies. I check whether each character already exists. If it exists, I increase its count; otherwise, I initialize its count to one."

Complexity:
- Time: O(n) average — Each character is processed once.
- Space: O(k) — The dictionary stores unique characters.
Method 4: Using defaultdict(int)
from collections import defaultdicttext = "banana"freq = defaultdict(int)for char in text:    freq[char] += 1print(dict(freq))



Output:
{'b': 1, 'a': 3, 'n': 2}


Syntax:
defaultdict(int)



How does it work?
- defaultdict(int) automatically gives new keys a default value of 0.
- So we can directly use freq[char] += 1.
- We don't need an if-else condition.
Dry run:
b → 0 + 1 = 1
a → 0 + 1 = 1
n → 0 + 1 = 1
a → 1 + 1 = 2
n → 1 + 1 = 2
a → 2 + 1 = 3


Interview explanation:

"I use defaultdict with int as its default factory. Whenever a new character appears, its initial count is automatically zero. Then I increment the count."

Complexity:
- Time: O(n) average.
- Space: O(k).
Method 5: Dictionary comprehension with .count()
text = "banana"freq = {    char: text.count(char)    for char in set(text)}print(freq)



Output:
{'b': 1, 'a': 3, 'n': 2}


How does it work?
- set(text) gets unique characters.
- text.count(char) counts each character.
- Dictionary comprehension stores the character and count.
Dry run:
Unique characters: {'b', 'a', 'n'}

b → text.count('b') = 1
a → text.count('a') = 3
n → text.count('n') = 2


Interview explanation:

"I first get the unique characters using set(). Then I use count() to calculate the frequency of each character and store the results in a dictionary."

Complexity:
- Time: O(n × k), worst case O(n²) — count() scans the complete string for every unique character.
- Space: O(k) for the resulting dictionary, excluding temporary storage.
Comparison: Character frequency
Method	Time	Space
Counter()	O(n)	O(k)
.get() loop	O(n)	O(k)
if-else loop	O(n)	O(k)
defaultdict	O(n)	O(k)
Comprehension + count	O(n × k)	O(k)


Part 2: Find Repeating Characters in a String
1. Problem definition
Find only the characters that appear more than once in a string.

Input:
text = "programming"



Output:
{'r': 2, 'g': 2, 'm': 2}


What is the difference?
- Character frequency returns all characters and their counts.
- Repeating characters returns only characters whose count is greater than 1.
Method 1: Using if-else loop (Recommended for learning logic)
text = "programming"counts = {}for char in text:    if char in counts:        counts[char] += 1    else:        counts[char] = 1repeating = {    char: count    for char, count in counts.items()    if count > 1}print(repeating)



Output:
{'r': 2, 'g': 2, 'm': 2}


How does it work?
1. Count every character using a dictionary.
2. Use counts.items() to access each character and its frequency.
3. Use if count > 1 to select repeated characters.
Dry run:

First, count the characters:
p → 1
r → 1
o → 1
g → 1
r → 2
a → 1
m → 1
m → 2
i → 1
n → 1
g → 2


Dictionary:
{    'p': 1, 'r': 2, 'o': 1, 'g': 2,    'a': 1, 'm': 2, 'i': 1, 'n': 1}



Now apply the condition count > 1:
Character	Count	Repeating?
p	1	No
r	2	Yes
o	1	No
g	2	Yes
a	1	No
m	2	Yes
i	1	No
n	1	No

Final result:
{'r': 2, 'g': 2, 'm': 2}



Interview explanation:

"First, I count the frequency of every character using a dictionary. Then I filter the dictionary and select only the characters whose frequency is greater than one."

Complexity:
- Time: O(n + k), which is O(n) — One traversal to count and another to filter unique dictionary entries.
- Space: O(k) — The frequency dictionary and repeating-character result store up to k unique characters.
Method 2: Using .get() method
text = "programming"counts = {}for char in text:    counts[char] = counts.get(char, 0) + 1repeating = {    char: count    for char, count in counts.items()    if count > 1}print(repeating)



Output:
{'r': 2, 'g': 2, 'm': 2}


How does it work?

The .get() method counts each character. Then the dictionary comprehension filters the repeated characters.

Interview explanation:

"I use get() to count the characters without writing an if-else condition. After counting, I select only those characters whose frequency is greater than one."

Complexity:
- Time: O(n) average.
- Space: O(k).
Method 3: Using Counter()
from collections import Countertext = "programming"counts = Counter(text)repeating = {    char: count    for char, count in counts.items()    if count > 1}print(repeating)



Output:
{'r': 2, 'g': 2, 'm': 2}


How does it work?
- Counter(text) counts all characters.
- counts.items() gives each character and its frequency.
- count > 1 selects repeated characters.
Interview explanation:

"I use Counter to automatically calculate character frequencies. Then I filter the result to get only characters that appear more than once."

Complexity:
- Time: O(n) average.
- Space: O(k).
Comparison: Finding repeating characters
Method	Time	Space
if-else + dictionary	O(n)	O(k)
.get() + dictionary	O(n)	O(k)
Counter() + filtering	O(n)	O(k)

Interview recommendation
My recommendation is to practise these two approaches:
1. .get() method: Best balance of simple code and efficient logic without imports.
2. Counter(): Best shortcut for real-world Python programs.
For interviews, understand the if-else method too, because it shows that you understand how dictionary counting works.

Part 3: Important interview questions and answers
Q1. What is character frequency?

It is the number of times a character appears in a string.

Q2. What is the purpose of a dictionary in this problem?

It stores each character as a key and its frequency as a value.

Q3. What is the difference between get() and if-else?

Both can count characters. get() provides a default value if a key is missing, so the code becomes shorter.

Q4. What does freq.get(char, 0) mean?

It returns the current count. If the character is not present, it returns zero.

Q5. What is defaultdict(int)?

It is a dictionary that automatically assigns zero to a new key when using int as its default factory.

Q6. What does counts.items() return?

It provides the dictionary's key-value pairs.

Q7. What does count > 1 mean?

It selects characters that appear more than once.

Q8. What is the time complexity of character counting?

O(n) average, because we process each character once.

Q9. What is the difference between Counter() and defaultdict()?

Counter() directly counts elements. defaultdict() provides a default value for missing keys, and we update the counts ourselves.

Q10. Is Python character counting case-sensitive?

Yes. For example, 'A' and 'a' are treated as different characters.

Part 4: README.md – Complete revision notes
Python Interview Problem: Character Frequency and Repeating Characters
1. Character Frequency
Problem
Count how many times each character appears in a string.

Input:
text = "banana"
Output:
{'b': 1, 'a': 3, 'n': 2}
Method 1: Counter()
from collections import Counter

text = "banana"
freq = dict(Counter(text))

print(freq)
- Time: O(n)
- Space: O(k)
- Best for simple real-world counting.
Method 2: Dictionary get()
text = "banana"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)
- Time: O(n) average
- Space: O(k)
- Recommended for interviews.
Method 3: If-else loop
text = "banana"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
- Time: O(n) average
- Space: O(k)
- Best for understanding dictionary logic.
Method 4: defaultdict()
from collections import defaultdict

text = "banana"
freq = defaultdict(int)

for char in text:
    freq[char] += 1

print(dict(freq))
- Time: O(n) average
- Space: O(k)
Method 5: Dictionary comprehension
text = "banana"

freq = {
    char: text.count(char)
    for char in set(text)
}

print(freq)
- Time: O(n × k), worst case O(n²)
- Space: O(k)
- Not recommended for large strings.

2. Find Repeating Characters
Problem
Find characters that appear more than once.

Input:
text = "programming"
Output:
{'r': 2, 'g': 2, 'm': 2}
Method 1: If-else + Dictionary
text = "programming"
counts = {}

for char in text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

repeating = {
    char: count
    for char, count in counts.items()
    if count > 1
}

print(repeating)
- Time: O(n)
- Space: O(k)
Method 2: get() + Dictionary
text = "programming"
counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

repeating = {
    char: count
    for char, count in counts.items()
    if count > 1
}

print(repeating)
- Time: O(n) average
- Space: O(k)
- Recommended interview approach.
Method 3: Counter()
from collections import Counter

text = "programming"
counts = Counter(text)

repeating = {
    char: count
    for char, count in counts.items()
    if count > 1
}

print(repeating)
- Time: O(n) average
- Space: O(k)
- Short and readable.

3. Important Python Syntax
Syntax	Meaning
freq = {}	Creates an empty dictionary
freq.get(char, 0)	Gets count or returns zero
freq[char] += 1	Increases frequency
Counter(text)	Automatically counts elements
defaultdict(int)	Gives new keys a default value of zero
counts.items()	Returns key-value pairs
count > 1	Checks for repeated characters4. Complexity
- n = total number of characters.
- k = number of unique characters.
Method	Time	Space
Counter	O(n)	O(k)
get()	O(n) average	O(k)
if-else	O(n) average	O(k)
defaultdict	O(n) average	O(k)
count() comprehension	O(n × k)	O(k)5. Interview Questions
1. What is character frequency?
2. Why do we use a dictionary?
3. What is the difference between get() and if-else?
4. What is Counter()?
5. What is defaultdict(int)?
6. What does counts.items() return?
7. How do you find repeating characters?
8. What does count > 1 mean?
9. What is the time complexity of character counting?
10. Is Python character counting case-sensitive?
6. Interview Recommendation
Practise these methods in this order:
1. If-else loop – understand the basic logic.
2. get() method – write shorter and efficient code.
3. Counter() – learn the built-in shortcut.
Important: Character frequency counts all characters. Finding repeating characters filters the frequency dictionary to keep only counts greater than one.




Part 5: One important interview practice
Try this small variation:

Question: Find only the repeating characters in "mississippi" and their frequencies.

Expected output:
{'i': 4, 's': 4, 'p': 2}



Also remember: the examples count uppercase and lowercase separately, and they include spaces and punctuation unless you explicitly remove or normalize them.