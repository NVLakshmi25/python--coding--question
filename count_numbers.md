Python Program to Count Words in a Sentence
1. Problem statement
Given a sentence, write a Python program to count the total number of words.

Example:
text = "Python is easy and fun to learn"



Output: 7
2. Definition, purpose, and usage
- What: Count the total number of words in a given sentence.
- Why: To understand how many words are present in a text.
- Purpose: Text analysis, document processing, and word-count applications.
- How: Split the sentence into words and count them.
- Where: Text editors, search engines, document tools, and NLP applications.
- When: Whenever we need to calculate the number of words in a string.
3. Different methods
Method 1: Using split() and len()
Best for fresher interviews
Logic:
1. split() divides the sentence into a list of words.
2. len() returns the number of elements in that list.
Syntax:
words = text.split()count = len(words)



Complete code:
text = "Python is easy and fun to learn"words = text.split()word_count = len(words)print("Word Count:", word_count)



Output:
Word Count: 7


Dry run:

After split():
words = ["Python", "is", "easy", "and", "fun", "to", "learn"]



Step	Word	Count
1	Python	1
2	is	2
3	easy	3
4	and	4
5	fun	5
6	to	6
7	learn	7

Finally, len(words) returns 7.

Why does it work?

split() separates words using whitespace by default. It also handles multiple spaces, tabs, and newlines. len() counts the resulting list elements.

Complexity:
- Time: \(O(n)\) — Python scans the sentence to split it and count the resulting words.
- Space: \(O(n)\) — split() creates a new list containing the words.
Method 2: Using a for loop
Logic: Split the sentence and increase the counter by one for every word.
text = "Python is easy and fun to learn"word_count = 0for word in text.split():    word_count += 1print("Word Count:", word_count)



Output:
Word Count: 7


Dry run:
Iteration	Word	word_count
1	Python	1
2	is	2
3	easy	3
4	and	4
5	fun	5
6	to	6
7	learn	7

- Time: \(O(n)\) — the sentence is split and every word is visited.
- Space: \(O(n)\) — the split operation creates a list.
Method 3: Using Regular Expressions (re)
Logic: Use re.findall() to extract words and ignore punctuation.
import retext = "Hello, world! Welcome to Python 3."words = re.findall(r'\b\w+\b', text)word_count = len(words)print("Word Count:", word_count)



Output:
Word Count: 6


Extracted words:
['Hello', 'world', 'Welcome', 'to', 'Python', '3']



Important syntax:
- re – Python regular expression module.
- findall() – finds all matching patterns.
- \b – word boundary.
- \w+ – one or more word characters (letters, digits, or underscore).
- Time: \(O(n)\) for typical use.
- Space: \(O(n)\) — stores all matched words in a list.
Note: This pattern counts 3 as a word and treats underscores as word characters.
Method 4: Using collections.Counter
Logic: Counter counts how many times each word appears.
from collections import Countertext = "Python is simple, yet powerful and simple."words = text.split()word_frequencies = Counter(words)print("Total Words:", len(words))print("Word Frequencies:", word_frequencies)



Output:
Total Words: 7
Word Frequencies: Counter({
    'Python': 1,
    'is': 1,
    'simple,': 1,
    'yet': 1,
    'powerful': 1,
    'and': 1,
    'simple.': 1
})


- Time: \(O(n)\) average — counts each word.
- Space: \(O(n)\) — stores word frequencies.
Important: simple, and simple. are treated as different words because punctuation is not removed. Also, uppercase and lowercase words are treated separately.
Method 5: Using a for loop without split()
Logic: Check each character. Whenever a new word starts, increase the count.
text = "  Count   these words  "word_count = 0in_word = Falsefor char in text:    if not char.isspace() and not in_word:        word_count += 1        in_word = True    elif char.isspace():        in_word = Falseprint("Word Count:", word_count)



Output:
Word Count: 3


Dry run:
Character/event	in_word	word_count
Leading spaces	False	0
C (new word)	True	1
Space	False	1
t (new word)	True	2
Space	False	2
w (new word)	True	3
Trailing spaces	False	3

- Time: \(O(n)\) — checks each character once.
- Space: \(O(1)\) — uses only two variables, without creating a word list.
4. Method comparison
Method	Time	Extra space	Best use
split() + len()	O(n)	O(n)	Simple word count
for loop + split()	O(n)	O(n)	Understanding loops
Regular expressions	O(n) typical	O(n)	Extracting words
Counter()	O(n) average	O(n)	Word frequencies
Character loop	O(n)	O(1)	Manual logic

5. Which method should you follow in interviews?
My recommendation is Method 1: split() + len().

Why?
1. Simple and readable code.
2. Easy to explain to an interviewer.
3. Handles multiple spaces, tabs, and newlines.
4. Requires very little code.
5. Efficient for normal word-count problems.
However, if the interviewer says, "Don't use built-in methods like split()", use Method 5 to demonstrate your own logic.
6. Interview questions and answers
Q1. What does split() do?

It divides a string into a list of words based on whitespace.

Q2. What does len() do?

It returns the number of elements in a list or the number of characters in a string.

Q3. Does split() handle multiple spaces?

Yes. By default, it handles multiple spaces, tabs, and newlines.

Q4. What is the difference between split() and split(" ")?
- split() handles consecutive whitespace as one separator and ignores leading/trailing whitespace.
- split(" ") splits only at ordinary space characters and may produce empty strings.
Q5. Does punctuation affect word counting?

With split(), punctuation stays attached to words. For example, "Hello," is counted as one word. Regex can extract words separately.

Q6. What is the difference between Counter() and len(split())?

len(split()) gives the total number of words. Counter() gives the frequency of each individual word.

Q7. What is the time complexity?

O(n), because the sentence needs to be processed to identify its words.
7. Interviewee explanation
You can say this in your interview:
To count the number of words in a sentence, I use Python's split() and len() methods.

First, split() divides the sentence into a list of words based on whitespace.

Then, len() counts the number of elements in that list.

Finally, I get the total number of words.

The time complexity is O(n), and the space complexity is O(n), because split() creates a new list.

8. README.md revision notes
Python Program to Count Words in a Sentence
1. Definition
Count the total number of words present in a given sentence.

Example:
text = "Python is easy and fun to learn"
Output: 7
2. Recommended Method: split() + len()
text = "Python is easy and fun to learn"

words = text.split()
word_count = len(words)

print("Word Count:", word_count)
Output:
Word Count: 7
3. Dry Run
After splitting:
['Python', 'is', 'easy', 'and', 'fun', 'to', 'learn']
len(words) returns 7.
4. Other Methods
1. split() + len() – simplest method.
2. for loop – counts each word.
3. re.findall() – extracts words using patterns.
4. collections.Counter() – counts individual word frequencies.
5. Character loop – counts words without creating a list.
5. Complexity
Method	Time	Space
split() + len()	O(n)	O(n)
For loop + split()	O(n)	O(n)
Regex	O(n) typical	O(n)
Counter	O(n) average	O(n)
Character loop	O(n)	O(1)6. Important Concepts
- split() – divides a sentence into words.
- len() – returns the number of elements.
- for – iterates through elements.
- Counter() – counts word frequencies.
- re.findall() – extracts matching words.
- isspace() – checks whether a character is whitespace.
7. Interview Tip
Prefer len(text.split()) for a normal word-count problem.

If the interviewer asks you to avoid split(), use the character-loop method.
8. Practice Questions
1. Count words in "Hello Python World".
2. Count words when multiple spaces are present.
3. Count words in an empty string.
4. Count words containing punctuation.
5. Find the frequency of each word.
6. Count words without using split().




Remember: For a fresher interview, understand how split() creates a list and how len() counts its elements. Also practise the character-loop approach to demonstrate your logic without relying on split().
