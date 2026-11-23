Python Program to Count Vowels and Consonants in a String
Recommended for fresher interviews
 Beginner level 

1. Problem statement
Question: Given a string, count how many vowels and consonants it contains.

Definition:
- Vowels: a, e, i, o, u
- Consonants: Other English alphabet letters.
Example:

Input: "Hello World! 123"
- Vowels: e, o, o = 3
- Consonants: H, l, l, W, r, l, d = 7
Output:
Vowels: 3
Consonants: 7


Spaces, numbers, and special characters are ignored.
2. Why, purpose, how, where and when?
- Why? To understand string handling, loops, and conditional statements.
- Purpose: To count vowels and consonants in a given sentence.
- How? Check each character and classify it as a vowel or consonant.
- Where? String-processing programs, text analysis, and beginner coding interviews.
- When? When a problem asks you to count or classify letters in a string.
3. Recommended method: Using a for loop
Best choice for fresher interviews
This is the method I recommend because it is easy to understand, explain, and trace.

Syntax:
for char in text:    if condition:        # perform an action



Code:
text = "Hello World! 123"vowels = 0consonants = 0for char in text.lower():    if char.isalpha():        if char in "aeiou":            vowels += 1        else:            consonants += 1print("Vowels:", vowels)print("Consonants:", consonants)



Important built-in methods:
- lower() – converts letters to lowercase.
- isalpha() – checks whether a character is an alphabet letter.
- in – checks whether a character exists in "aeiou".
4. Dry run (step-by-step tracing)
Input: "Hello World! 123"
Character	Condition	Vowels	Consonants
H	Consonant	0	1
e	Vowel	1	1
l	Consonant	1	2
l	Consonant	1	3
o	Vowel	2	3
Space	Ignored	2	3
W	Consonant	2	4
o	Vowel	3	4
r	Consonant	3	5
l	Consonant	3	6
d	Consonant	3	7
! 123	Ignored	3	7

Output:
Vowels: 3
Consonants: 7


5. Other methods
Method 2: Using sum() and generator expressions

This is a shorter Python approach. It counts matching characters using conditions.
text = "Hello World! 123"lower_text = text.lower()vowels = sum(1 for c in lower_text if c in "aeiou")consonants = sum(    1 for c in lower_text    if c.isalpha() and c not in "aeiou")print("Vowels:", vowels)print("Consonants:", consonants)



Output:
Vowels: 3
Consonants: 7


Method 3: Using a set

A set stores the vowels. We check each character against it.
text = "Hello World! 123"vowel_set = {"a", "e", "i", "o", "u"}vowels = 0consonants = 0for char in text.lower():    if char in vowel_set:        vowels += 1    elif char.isalpha():        consonants += 1print("Vowels:", vowels)print("Consonants:", consonants)



Output:
Vowels: 3
Consonants: 7


Method 4: Using .count()

This method counts each vowel separately and subtracts the vowel count from the total alphabet count.
text = "Hello World! 123"lower_text = text.lower()vowels = sum(lower_text.count(v) for v in "aeiou")total_letters = sum(1 for c in lower_text if c.isalpha())consonants = total_letters - vowelsprint("Vowels:", vowels)print("Consonants:", consonants)



Output:
Vowels: 3
Consonants: 7


6. Time and space complexity
Let n be the number of characters in the input string.
Method	Time complexity	Extra space
For loop	O(n)	O(1)
Generator + sum()	O(n)	O(1)
Set + for loop	O(n)	O(1)
.count()	O(n)	O(1)

Why?
- Time O(n): The loop-based methods examine each character. The .count() method scans the string five times for vowels and once for alphabet letters; that is still O(n), because the number of scans is fixed.
- Space O(1): The methods use a fixed number of counters and variables, excluding the lowercase string created by lower().
- Space note: text.lower() creates a lowercase copy, which can take O(n) space. So the complete implementations using it can use O(n) additional space.
7. Which method should you follow?
I recommend Method 1: Simple for loop.

Why?
1. Easy to understand and explain.
2. Shows your knowledge of loops and conditions.
3. Handles spaces, numbers, and special characters correctly.
4. Uses one pass through the string.
5. Easy to debug during an interview.
8. Interview questions and answers
Q1. What are vowels and consonants?

Vowels are a, e, i, o, u. The remaining English alphabet letters are consonants.

Q2. Why do we use lower()?

To handle uppercase and lowercase letters in the same way.

Q3. Why do we use isalpha()?

To ignore spaces, numbers, and special characters.

Q4. Why do we use += 1?

To increase the counter by one whenever we find a vowel or consonant.

Q5. What is the time complexity?

O(n), because we check each character once.

Q6. Can we solve this without a loop?

Yes. We can use sum() with generator expressions or .count().
9. Interviewee explanation
If the interviewer asks you to explain your code, you can say:

"I initialize two counters, vowels and consonants, to zero. Then I convert the string into lowercase and iterate through each character using a for loop. First, I check whether the character is an alphabet using isalpha(). If it is a vowel, I increase the vowel counter. Otherwise, I increase the consonant counter. Finally, I print both counts. The time complexity is O(n), and the auxiliary space complexity is O(1), excluding the lowercase string."
10. README.md – Revision notes
Count Vowels and Consonants in Python
Problem
Count the number of vowels and consonants in a given string.
Example
Input:
"Hello World! 123"
Output:
Vowels: 3
Consonants: 7
Recommended approach: For loop
text = "Hello World! 123"

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
Important concepts
- lower() – converts text to lowercase.
- isalpha() – checks whether a character is a letter.
- in – checks whether a character belongs to the vowel string.
- += 1 – increases the counter by one.
Complexity
- Time: O(n) – checks each character once.
- Auxiliary space: O(1) – uses a fixed number of variables.
- Note: lower() creates a copy and can require O(n) space.
Interview explanation
Initialize two counters to zero. Iterate through each character. Check whether it is an alphabet letter. If it is a vowel, increase the vowel counter; otherwise, increase the consonant counter. Finally, print both counts.
Interview tip
For a fresher interview, prefer the simple for-loop method because it is easy to explain and debug.




Practice question: How would you modify this program to count each vowel separately, such as a = 2, e = 3, i = 1, o = 4, and u = 0?