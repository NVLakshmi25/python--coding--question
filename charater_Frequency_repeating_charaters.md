Python String Programs – Character Frequency and String Repetition
You have shared two different Python problems:
1. Find the frequency of each character in a string.
2. Repeat a string a given number of times.
Let's understand both using simple English, dry runs, outputs, interview explanations, and complexity.
Part 1: Find Frequency of Characters in Python
1. Problem definition
What is character frequency?

Character frequency means counting how many times each character appears in a string.

Input:
s = "GeeksforGeeks"


Output:
{'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}


For example:
- G appears 2 times.
- e appears 4 times.
- k appears 2 times.
Why, purpose, where and when?
- Why: To know how many times each character appears.
- Purpose: Count repeated characters.
- Where: Text analysis, word processing, password analysis and data processing.
- When: When we need to count characters or identify repeated characters.
Method 1: Using a dictionary (Recommended for interviews)
s = "GeeksforGeeks"freq = {}for c in s:    if c in freq:        freq[c] += 1    else:        freq[c] = 1print(freq)



Output:
{'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}


Syntax:
if character in dictionary:    dictionary[character] += 1else:    dictionary[character] = 1



How does it work?
- freq = {} creates an empty dictionary.
- for c in s visits each character.
- if c in freq checks whether the character already exists.
- freq[c] += 1 increases its count.
- Otherwise, freq[c] = 1 adds it with an initial count of 1.
Dry run:
Character	Action	Dictionary
G	New character	{'G': 1}
e	New character	{'G': 1, 'e': 1}
e	Increase count	{'G': 1, 'e': 2}
k	New character	{'G': 1, 'e': 2, 'k': 1}
s	New character	{'G': 1, 'e': 2, 'k': 1, 's': 1}
f	New character	Add f: 1
o	New character	Add o: 1
r	New character	Add r: 1
G	Increase count	G: 2
e	Increase count	e: 3
e	Increase count	e: 4
k	Increase count	k: 2
s	Increase count	s: 2

Final result: {'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}

Interview explanation:

"I create an empty dictionary to store characters and their counts. Then I iterate through the string. If a character already exists, I increase its count by one. Otherwise, I add it to the dictionary with a count of one."

Complexity:
- Time: O(n) average — We visit each character once, and dictionary lookup/update takes O(1) average time.
- Space: O(k) — The dictionary stores each distinct character. Here, k is the number of unique characters.
Method 2: Using Counter() from collections
Python provides a built-in class called Counter to count elements.
from collections import Counters = "GeeksforGeeks"freq = Counter(s)print(dict(freq))



Output:
{'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}


Syntax:
Counter(iterable)



How does it work?
- Counter(s) automatically counts each character.
- dict(freq) converts the Counter object into a normal dictionary.
Dry run:
G → 1
e → 1
e → 2
k → 1
s → 1
f → 1
o → 1
r → 1
G → 2
e → 3
e → 4
k → 2
s → 2


Interview explanation:

"I use the Counter class from the collections module. It automatically counts how many times each character appears and returns a dictionary-like object."

Complexity:
- Time: O(n) average — It processes each character once.
- Space: O(k) — It stores the distinct characters and their counts.
Method 3: Using dictionary comprehension
s = "GeeksforGeeks"freq = {c: s.count(c) for c in s}print(freq)



Output:
{'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}


Syntax:
{key: value for item in iterable}



How does it work?
- for c in s visits each character.
- s.count(c) counts how many times that character occurs.
- {c: s.count(c)} stores the character and its count.
Dry run:
s.count('G') = 2
s.count('e') = 4
s.count('k') = 2
s.count('s') = 2
s.count('f') = 1
s.count('o') = 1
s.count('r') = 1


Interview explanation:

"I use dictionary comprehension to create a dictionary where each character is a key and its frequency is the value. The count() method calculates the frequency."

Complexity:
- Time: O(n²) worst case — s.count() scans the entire string for each distinct character.
- Space: O(k) — The dictionary stores unique characters.
Note: This is shorter, but less efficient than the first two methods.
Frequency methods – comparison
Method	Time	Space
Dictionary + loop	O(n) average	O(k)
Counter()	O(n) average	O(k)
Dictionary comprehension	O(n²) worst case	O(k)

Interview recommendation
 Practise dictionary + for loop first. It demonstrates your logic and is a common interview approach. Also learn Counter() as the easiest built-in solution.

Part 2: How to Repeat a String in Python
1. Problem definition
What is string repetition?

String repetition means creating multiple copies of the same string.

Input:
s = "Hello! "n = 3



Output:
Hello! Hello! Hello!


Why, purpose, where and when?
- Why: To repeat a word or sentence multiple times.
- Purpose: Generate repeated text without manually writing it.
- Where: Creating patterns, separators, reports and formatted output.
- When: When we need to repeat a string a specific number of times.
Method 1: Using multiplication operator * (Recommended)
s = "Hello! "r = s * 3print(r)



Output:
Hello! Hello! Hello!


Syntax:
string * number



How does it work?

The * operator repeats the string according to the given number.

Dry run:
s = "Hello! "

s * 1 = "Hello! "
s * 2 = "Hello! Hello! "
s * 3 = "Hello! Hello! Hello! "


Interview explanation:

"I use the multiplication operator to repeat a string. It repeats the given string the specified number of times and returns a new string."

Complexity:
- Time: O(n × k) — If the original string has n characters and we repeat it k times, the output contains n × k characters.
- Space: O(n × k) — Python creates a new string of that length.
Method 2: Using itertools.repeat()
import itertoolss = ''.join(itertools.repeat("Hello! ", 3))print(s)



Output:
Hello! Hello! Hello!


Syntax:
itertools.repeat(object, times)



How does it work?
- itertools.repeat("Hello! ", 3) generates the same string three times.
- "".join() combines those repeated strings into one string.
Dry run:
itertools.repeat("Hello! ", 3)

1 → Hello!
2 → Hello!
3 → Hello!

join() combines them.


Interview explanation:

"I use itertools.repeat() to generate the string multiple times. Then I use join() to combine the repeated values into one string."

Complexity:
- Time: O(n × k) — The final output contains n × k characters.
- Space: O(n × k) — The final string needs that much space. The repeat iterator itself uses O(1) auxiliary space.
Method 3: Using a for loop
s = ""for _ in range(4):    s += "Hello!"print(s)



Output:
Hello!Hello!Hello!Hello!


Syntax:
for _ in range(number):    statement



How does it work?
- s = "" creates an empty string.
- range(4) runs the loop four times.
- s += "Hello!" adds the string during each iteration.
- print(s) displays the final string.
Dry run:
Iteration	Value of s
Initially	""
1	"Hello!"
2	"Hello!Hello!"
3	"Hello!Hello!Hello!"
4	"Hello!Hello!Hello!Hello!"

Interview explanation:

"I initialize an empty string and use a for loop to repeat the given text. In each iteration, I append the text to the result."

Complexity of this exact code:
- Time: O((n × k) × k) worst case — Repeated string concatenation can copy the existing result on each iteration.
- Space: O(n × k) — The final result has n × k characters.
Better loop approach for interviews:
parts = []for _ in range(4):    parts.append("Hello!")result = "".join(parts)print(result)



Output:
Hello!Hello!Hello!Hello!


- Time: O(n × k) — Each string is collected and joined once.
- Space: O(n × k) — The list and final output store the repeated text.
Method 4: Using numpy.repeat()
import numpy as nps = np.repeat("Hello! ", 3)result = ''.join(s)print(result)



Output:
Hello! Hello! Hello!


Syntax:
numpy.repeat(array, repeats)



How does it work?
- np.repeat() creates an array containing repeated strings.
- join() combines the array elements into one string.
Dry run:
np.repeat("Hello! ", 3)

['Hello! ', 'Hello! ', 'Hello! ']

join()

'Hello! Hello! Hello! '


Interview explanation:

"I use NumPy's repeat function to create an array containing repeated strings. Then I use join to combine the array elements into a single string."

Complexity:
- Time: O(n × k) — It creates and combines the repeated text.
- Space: O(n × k) — The repeated array and final string require memory.
Note: NumPy is mainly useful for numerical and array operations. It is unnecessary for simple string repetition.
String repetition – comparison
Method	Time	Space
Multiplication *	O(n × k)	O(n × k)
itertools.repeat() + join()	O(n × k)	O(n × k)
Loop with +=	O(n × k²) worst case	O(n × k)
Loop with list + join()	O(n × k)	O(n × k)
numpy.repeat()	O(n × k)	O(n × k)

Interview recommendation
 Use the multiplication operator * for normal string repetition. It is simple, readable and efficient. Learn the loop method to demonstrate your logic.

Part 3: Interview questions and answers
Character frequency
Q1. What is character frequency?

It means counting how many times each character appears in a string.

Q2. Why do we use a dictionary?

A dictionary stores each character as a key and its frequency as a value.

Q3. Why do we write freq[c] += 1?

To increase the existing character count by one.

Q4. What happens if the character is not in the dictionary?

We add it with an initial count of 1.

Q5. What is the difference between Counter() and a normal dictionary?

Counter() automatically counts elements, whereas a normal dictionary requires us to write the counting logic.

Q6. What is the time complexity of the dictionary method?

O(n) average, because we process each character once.
String repetition
Q1. How do you repeat a string in Python?

Using the multiplication operator *.

Q2. What is the purpose of join()?

It combines multiple strings into a single string.

Q3. What does range(4) mean?

It generates four values: 0, 1, 2 and 3.

Q4. What is the difference between * and itertools.repeat()?

Both can repeat strings. The multiplication operator directly creates the repeated string, while itertools.repeat() generates an iterator.

Q5. What happens if we multiply a string by zero?

It returns an empty string.
print("Hello" * 0)



Output:
''


Q6. What happens if we multiply a string by a negative number?

It also returns an empty string.

Part 4: README.md – Complete revision notes
Python String Programs – Character Frequency and Repetition
1. Find Frequency of Characters
Problem
Count how many times each character appears in a string.

Input:
s = "GeeksforGeeks"
Output:
{'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}
Method 1: Dictionary + For Loop
s = "GeeksforGeeks"

freq = {}

for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)
- Time: O(n) average
- Space: O(k)
- Recommended for interviews.
Method 2: Counter()
from collections import Counter

s = "GeeksforGeeks"
freq = Counter(s)

print(dict(freq))
- Time: O(n) average
- Space: O(k)
- Best built-in solution.
Method 3: Dictionary Comprehension
s = "GeeksforGeeks"

freq = {c: s.count(c) for c in s}

print(freq)
- Time: O(n²) worst case
- Space: O(k)
- Short but less efficient.
Important concepts
- freq = {} creates an empty dictionary.
- c in freq checks whether a character exists.
- freq[c] += 1 increases the count.
- freq[c] = 1 initializes the count.
- Counter() automatically counts elements.

2. Repeat a String
Problem
Repeat a string a specified number of times.

Input:
s = "Hello! "
n = 3
Output:
Hello! Hello! Hello!
Method 1: Multiplication Operator
s = "Hello! "
r = s * 3

print(r)
- Time: O(n × k)
- Space: O(n × k)
- Recommended for normal Python programs and interviews.
Method 2: itertools.repeat()
import itertools

s = ''.join(itertools.repeat("Hello! ", 3))

print(s)
- Time: O(n × k)
- Space: O(n × k) including output.
Method 3: For Loop
s = ""

for _ in range(4):
    s += "Hello!"

print(s)
- Time: O(n × k²) worst case for repeated concatenation.
- Space: O(n × k).
Better Loop Method: List + join()
parts = []

for _ in range(4):
    parts.append("Hello!")

result = "".join(parts)

print(result)
- Time: O(n × k)
- Space: O(n × k).
Method 4: NumPy repeat()
import numpy as np

s = np.repeat("Hello! ", 3)
result = ''.join(s)

print(result)
- Time: O(n × k)
- Space: O(n × k).
Important concepts
- * repeats a string.
- range(k) runs a loop k times.
- append() adds an item to a list.
- join() combines strings.
- itertools.repeat() generates repeated values.

Interview questions
Character frequency
1. What is character frequency?
2. Why do we use a dictionary?
3. What does freq[c] += 1 mean?
4. What is the purpose of Counter?
5. What is the time complexity of the dictionary approach?
6. What happens when a character appears for the first time?
String repetition
1. How do you repeat a string in Python?
2. What does the multiplication operator do?
3. What is the purpose of join()?
4. What does range(4) return?
5. What happens when a string is multiplied by zero?
6. What is the difference between multiplication and itertools.repeat()?
Interview recommendations
Problem	Recommended method
Character frequency	Dictionary + for loop
Character frequency shortcut	Counter()
String repetition	Multiplication operator (*)
String repetition using logic	For loop + list + join()Remember: Understand the logic first, then practise writing the code without looking at notes.




Part 5: Test your understanding
Python mini quiz
0/4 answered

1. What does `freq[c] += 1` do?

Deletes a character

Increases its count by one

Creates an empty dictionary




2. What is the average time complexity of dictionary-based character counting?

O(n)

O(n²)

O(log n)




3. What is the output of `print('Hi' * 3)`?

Hi3

HiHiHi

Hi Hi Hi




4. Which method is best for simple string repetition?

numpy.repeat()

A dictionary

Multiplication operator (*)



Submit answers
My advice: For fresher interviews, practise the dictionary frequency program and string multiplication first. Be able to explain each line and dry-run the examples without looking at the solution