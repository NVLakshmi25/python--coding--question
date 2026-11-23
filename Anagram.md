Python Interview Preparation: Check Whether Two Strings Are Anagrams
Let's understand this problem using simple English, multiple Python methods, dry runs, outputs, and interview questions.
Recommended for interviews: collections.Counter
My recommendation is to learn Counter() first, followed by the sorted() method. Both are easy to explain, and Counter() directly demonstrates your understanding of character frequency.
1. Understand the problem statement
Problem: Given two strings, check whether both strings contain exactly the same characters with the same frequency, even if their order is different.

Definition: An anagram is a word or string formed by rearranging the characters of another string without adding, removing, or changing any character.

Example:
s1 = "listen"s2 = "silent"



Output:
Yes


Why?

Both strings contain:
- l → 1 time
- i → 1 time
- s → 1 time
- t → 1 time
- e → 1 time
- n → 1 time
The order is different, but the characters and their frequencies are the same.
Another example
s1 = "hello"s2 = "world"



Output:
No


Because both strings do not contain the same characters.
2. Basic interview questions
Question	Simple answer
What is an anagram?	Two strings with the same characters and frequencies.
Why do we check anagrams?	To verify whether two strings contain the same character combinations.
What is character frequency?	How many times a character appears in a string.
Does the order matter?	No, the order can be different.
Does the number of characters matter?	Yes, both strings must have equal character counts.
Where is it used?	Word games, text processing and string comparison problems.
When do we use it?	When we need to compare two strings based on their characters rather than their order.

3. Method 1: Using collections.Counter() (Recommended)
Best beginner-friendly interview approach
Definition: Counter() is a Python class from the collections module. It counts how many times each character appears in a string.

Why use it?
- Automatically counts characters.
- No need to write manual counting logic.
- Easy to understand and explain.
- Directly compares character frequencies.
Syntax
from collections import CounterCounter(string)



Complete program
from collections import Counters1 = "listen"s2 = "silent"if Counter(s1) == Counter(s2):    print("Yes")else:    print("No")



Output:
Yes


Dry run (step-by-step tracing)
Input:
s1 = "listen"s2 = "silent"



Step 1: Count characters in the first string.
Counter(s1)



Result:
{'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}



Step 2: Count characters in the second string.
Counter(s2)



Result:
{'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}



Step 3: Compare both counters.
Counter(s1) == Counter(s2)



Result:
True



Step 4: Print the result.
Yes


Important: Dictionary order does not matter when comparing the character-frequency mappings.
Complexity
- Time: O(n + m) — We count the characters in both strings once. Here n and m are their lengths.
- Space: O(k) — We store the unique character counts. k represents the number of distinct characters.
For strings containing a fixed character set, this extra space is bounded by that character set.

4. Method 2: Using sorted()
Definition: The sorted() function arranges characters in ascending order. If both sorted strings are equal, they are anagrams.

Why use it?
- Very simple code.
- No need for additional modules.
- Easy for beginners to understand.
Syntax
sorted(string)



Complete program
s1 = "listen"s2 = "silent"if sorted(s1) == sorted(s2):    print("Yes")else:    print("No")



Output:
Yes


Dry run
Step 1: Sort the first string.
sorted("listen")



Output:
['e', 'i', 'l', 'n', 's', 't']



Step 2: Sort the second string.
sorted("silent")



Output:
['e', 'i', 'l', 'n', 's', 't']



Step 3: Compare both lists.
['e', 'i', 'l', 'n', 's', 't'] == ['e', 'i', 'l', 'n', 's', 't']



Result:
True



Final output:
Yes


Complexity
- Time: O(n log n) — Sorting both strings takes O(n log n) time when their lengths are equal.
- Space: O(n) — sorted() creates new lists containing the characters.
5. Method 3: Using Array Frequency (ord())
Definition: We use an array of 26 elements to count lowercase English letters from a to z.

Why use it?

It avoids sorting and provides linear-time performance. However, it is suitable only when the input contains lowercase English letters.
Important syntax
freq = [0] * 26



Creates an array containing 26 zeros.
ord(ch) - 97



Converts a lowercase character into an array index.

For example:
Character	ord()	Index
a	97	0
b	98	1
c	99	2
z	122	25

Complete program
s1 = "listen"s2 = "silent"if len(s1) != len(s2):    print("No")else:    freq = [0] * 26    for i in range(len(s1)):        freq[ord(s1[i]) - 97] += 1        freq[ord(s2[i]) - 97] -= 1    if all(x == 0 for x in freq):        print("Yes")    else:        print("No")



Output:
Yes


Dry run
Input:
s1 = "listen"s2 = "silent"



Initially, all 26 frequency values are zero.

For each position, we increase the first string's character count and decrease the second string's character count.
Index	s1[i]	s2[i]	Frequency update
0	l	s	l +1, s -1
1	i	i	i +1, i -1
2	s	l	s +1, l -1
3	t	e	t +1, e -1
4	e	n	e +1, n -1
5	n	t	n +1, t -1

All character counts become zero.
all(x == 0 for x in freq)



Result:
True



Final output:
Yes


Complexity
- Time: O(n) — We traverse both strings once and check a fixed-size array of 26 elements.
- Space: O(1) — The array always contains 26 elements, regardless of input size.
Interview caution: This method assumes lowercase English letters. It needs changes for uppercase letters, spaces, or special characters.
6. Method 4: Using Character Removal
Definition: Convert the second string into a list and remove each matching character from it.

If all characters from the first string can be removed, both strings are anagrams.
Complete program
s1 = "listen"s2 = "silent"characters = list(s2)for ch in s1:    if ch in characters:        characters.remove(ch)    else:        print("No")        breakelse:    print("Yes")



Output:
Yes


Dry run
Initially:
characters = ['s', 'i', 'l', 'e', 'n', 't']



Now check each character from s1.
Character	Action	Remaining characters
l	Remove l	s, i, e, n, t
i	Remove i	s, e, n, t
s	Remove s	e, n, t
t	Remove t	e, n
e	Remove e	n
n	Remove n	Empty

All characters are successfully removed.

Output:
Yes


What is the purpose of for...else?

The else block executes when the loop finishes normally without encountering break.
Complexity
- Time: O(n²) — Membership checking and removing elements from a list can each take O(n) time.
- Space: O(n) — We create a list containing the characters of the second string.
This method is useful for understanding list operations, but I would not recommend it for interviews when better approaches are available.

7. Comparison of all four methods
Method	Time	Space	Suitable for
Counter()	O(n)	O(k)	General character counting
sorted()	O(n log n)	O(n)	Simple solutions
Frequency array	O(n)	O(1)	Lowercase English letters
Character removal	O(n²)	O(n)	Learning list operations

Assumption: Both strings have equal length n for the comparison above.

My recommendation from a recruiter/interviewer point of view:
1. Learn Counter() first because it clearly demonstrates character-frequency logic.
2. Learn sorted() as an alternative because it is easy to write.
3. Understand the frequency-array approach for optimized solutions when the character set is restricted.
4. Avoid character removal for performance-sensitive interviews.
8. Important edge cases (interview preparation)
Always test your program with different inputs.
Input 1	Input 2	Expected output	Reason
"listen"	"silent"	Yes	Same characters
"hello"	"world"	No	Different characters
"aabb"	"bbaa"	Yes	Same frequency
"aabb"	"abbb"	No	Different frequency
"abc"	"ab"	No	Different lengths
""	""	Yes	Both are empty

Important: The basic solutions are case-sensitive and consider spaces as characters. For example, "Listen" and "silent" are not anagrams unless you normalize the case first.

9. Interviewer and interviewee explanation
Interviewer: How do you check whether two strings are anagrams?

Interviewee:

"I would use Python's Counter function from the collections module.

First, I count the frequency of each character in both strings using Counter.

Then I compare both frequency mappings. If they are equal, both strings are anagrams. Otherwise, they are not anagrams.

This approach takes O(n) time and O(k) extra space, where k is the number of unique characters."
Possible follow-up questions
Q1. Why do you use Counter()?

It automatically counts how many times each character appears.

Q2. Why is sorting not always the best approach?

Sorting takes O(n log n) time, whereas Counter takes O(n) time.

Q3. What happens if string lengths are different?

They cannot be anagrams, so we return No immediately.

Q4. Does character frequency matter?

Yes. Both strings must have exactly the same frequency for every character.

Q5. Can we solve this without using built-in functions?

Yes. We can use a frequency array or a dictionary and count characters manually.

Q6. What is the difference between Counter() and set()?
- Counter() stores characters and their frequencies.
- set() stores only unique characters and removes duplicates.
For example:
from collections import Counters = "aabb"print(Counter(s))# {'a': 2, 'b': 2}print(set(s))# {'a', 'b'}




10. README.md – Python interview notes
You can save the following as anagram_string/README.md in your Python practice repository.
Check Whether Two Strings Are Anagrams – Python
1. Problem Statement
Given two strings, check whether they contain the same characters with the same frequency, regardless of their order.

Example:
s1 = "listen"
s2 = "silent"
Output:
Yes
2. Definition
An anagram is a word or string formed by rearranging the characters of another string without changing the character count.
3. Recommended Method – collections.Counter()
Counter is a Python class that counts the frequency of each character.
Code
from collections import Counter

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


s1 = "listen"
s2 = "silent"

if is_anagram(s1, s2):
    print("Yes")
else:
    print("No")
Output:
Yes
4. Dry Run
Input:
s1 = "listen"
s2 = "silent"
Character frequencies:
Counter(s1)
# {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}

Counter(s2)
# {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
Comparison:
Counter(s1) == Counter(s2)
# True
Final output: Yes
5. Other Approaches
Method 1: Using sorted()
s1 = "listen"
s2 = "silent"

print("Yes" if sorted(s1) == sorted(s2) else "No")
Method 2: Using Frequency Array
s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("No")
else:
    freq = [0] * 26

    for i in range(len(s1)):
        freq[ord(s1[i]) - 97] += 1
        freq[ord(s2[i]) - 97] -= 1

    print("Yes" if all(x == 0 for x in freq) else "No")
Note: This implementation supports only lowercase English letters.
Method 3: Using Character Removal
s1 = "listen"
s2 = "silent"

characters = list(s2)

for ch in s1:
    if ch in characters:
        characters.remove(ch)
    else:
        print("No")
        break
else:
    print("Yes")
6. Complexity Comparison
Method	Time Complexity	Space Complexity
Counter()	O(n)	O(k)
sorted()	O(n log n)	O(n)
Frequency Array	O(n)	O(1)
Character Removal	O(n²)	O(n)7. Important Interview Questions
1. What is an anagram?
2. Why do we use Counter()?
3. What is character frequency?
4. Why do we compare character counts?
5. Why is sorting less efficient than Counter?
6. What is the difference between set() and Counter()?
7. What happens if string lengths are different?
8. Can we solve this without sorting?
9. What is the time complexity?
10. What is the space complexity?
8. Interview Explanation
"I use the Counter function from Python's collections module. It counts the frequency of each character in both strings. Then I compare the two frequency mappings. If they are equal, the strings are anagrams. Otherwise, they are not anagrams."
9. Summary
- Anagrams contain the same characters.
- Character frequencies must match.
- Character order does not matter.
- Counter() counts character frequencies.
- sorted() compares sorted characters.
- Frequency arrays provide an efficient solution for a fixed alphabet.
- Character removal is less efficient.
Recommended interview approach: collections.Counter()

Remember: Understand the logic, perform the dry run, and explain the complexity instead of memorizing the code.




11. Practice question for you
Try this yourself without looking at the solution.
Question: Are these two strings anagrams?
s1 = "aabbcc"s2 = "abcabc"



1. What is the output?

Yes

No


2. Why?

Both strings have the same character frequencies.

Both strings have the same character order.

Only the string lengths are equal.

Check my answer

Next learning goal: Understand character frequency using Counter(), dictionaries, and loops. These concepts will help you solve many Python string interview problems.