Remove Duplicates in Python – List and String
There are two related problems:
1. List: Remove repeated numbers and keep only the first occurrence.
2. String: Remove repeated characters and keep only the first occurrence.
The important point is: preserve the original order while removing duplicates.
Part 1: Remove duplicates from a list
1. Problem definition
Given a list containing repeated elements, create a new list containing only unique elements.

Input:
a = [1, 2, 2, 3, 4, 4, 5]



Output:
[1, 2, 3, 4, 5]


Why, purpose, where and when?
- Why: To avoid repeated values.
- Purpose: Keep only unique elements.
- Where: Removing duplicate customer IDs, email addresses, product IDs or records.
- When: When a list should contain each value only once.
Method 1: Using dict.fromkeys()
a = [1, 2, 2, 3, 4, 4, 5]res = list(dict.fromkeys(a))print(res)



Output:
[1, 2, 3, 4, 5]


Syntax:
dict.fromkeys(iterable)



How does it work?
- Dictionary keys cannot contain duplicate keys.
- dict.fromkeys(a) creates keys from the list elements.
- list() converts those keys back into a list.
- Dictionary insertion order is preserved in modern Python.
Dry run:
Input element	Dictionary keys
1	1
2	1, 2
2	1, 2 (duplicate ignored)
3	1, 2, 3
4	1, 2, 3, 4
4	1, 2, 3, 4 (duplicate ignored)
5	1, 2, 3, 4, 5

Interview explanation:

"I use dict.fromkeys() to remove duplicates because dictionary keys are unique. It also preserves the insertion order. Finally, I convert the dictionary keys into a list."

Complexity:
- Time: O(n) average — Each element is processed once.
- Space: O(n) — The dictionary stores the unique elements.
Method 2: Using set()
a = [1, 2, 2, 3, 4, 4, 5]res = list(set(a))print(res)



Output: The list contains the unique values, but their order is not guaranteed.

Syntax:
set(iterable)



How does it work?
- set() stores only unique elements.
- list() converts the set back into a list.
Dry run:
Input:  [1, 2, 2, 3, 4, 4, 5]
Set:    {1, 2, 3, 4, 5}
Output: [1, 2, 3, 4, 5]  # one possible order


Interview explanation:

"I convert the list into a set because a set automatically removes duplicate values. Then I convert it back into a list."

Complexity:
- Time: O(n) average.
- Space: O(n) — The set stores unique elements.
Important: Don't use this method when original order matters.
Method 3: Using a for loop
a = [1, 2, 2, 3, 4, 4, 5]res = []for x in a:    if x not in res:        res.append(x)print(res)



Output:
[1, 2, 3, 4, 5]


Syntax to understand:
- res = [] — Creates an empty list.
- for x in a — Visits each element.
- if x not in res — Checks whether the element is already present.
- res.append(x) — Adds the element if it is new.
Dry run:
x	Is x already in res?	Updated res
1	No	[1]
2	No	[1, 2]
2	Yes	[1, 2]
3	No	[1, 2, 3]
4	No	[1, 2, 3, 4]
4	Yes	[1, 2, 3, 4]
5	No	[1, 2, 3, 4, 5]

Interview explanation:

"I create an empty list and iterate through the original list. Before adding an element, I check whether it already exists in the result list. If it does not exist, I append it. This removes duplicates and preserves the original order."

Complexity:
- Time: O(n²) worst case — x not in res may scan the result list for every element.
- Space: O(n) — The result list stores unique elements.
Method 4: Using list comprehension
a = [1, 2, 2, 3, 4, 4, 5]res = [][res.append(x) for x in a if x not in res]print(res)



Output:
[1, 2, 3, 4, 5]


How does it work?

It uses the same logic as the for loop, but combines the loop and condition into one expression.

Dry run: Same as Method 3. Each element is checked, and only new elements are appended.

Interview explanation:

"I use list comprehension to iterate through the list and append only elements that are not already present in the result."

Complexity:
- Time: O(n²) worst case — It performs the same membership checks as the loop method.
- Space: O(n) — The result list stores unique elements. The comprehension also creates a temporary list of return values from append().
Note: This is less readable than a normal loop. I recommend the normal for loop instead.

Part 2: Remove duplicate characters from a string
1. Problem definition
Given a string, remove repeated characters while keeping the first occurrence of each character in its original order.

Input:
s = "geeksforgeeks"



Output:
geksfor


Why, purpose, where and when?
- Why: To remove repeated characters.
- Purpose: Create a string containing unique characters.
- Where: Text processing, cleaning user input, removing repeated symbols.
- When: When each character should appear only once.
Method 1: Using dict.fromkeys()
s = "geeksforgeeks"res = "".join(dict.fromkeys(s))print(res)



Output:
geksfor


Syntax:
"".join(iterable)



How does it work?
- A string is iterable, so Python processes one character at a time.
- dict.fromkeys(s) creates unique character keys.
- "".join() combines those characters into a string.
Dry run:
Character	Result
g	g
e	ge
e	ge (duplicate ignored)
k	gek
s	geks
f	geksf
o	geksfo
r	geksfor
g, e, e, k, s	No changes

Interview explanation:

"I use dict.fromkeys() to remove duplicate characters. Since dictionary keys are unique and maintain insertion order, the first occurrence of each character is preserved. Then I use join() to create the final string."

Complexity:
- Time: O(n) — Each character is processed once, on average.
- Space: O(n) — The dictionary stores unique characters, and the output string also needs space.
Method 2: Using OrderedDict.fromkeys()
from collections import OrderedDicts = "geeksforgeeks"res = "".join(OrderedDict.fromkeys(s))print(res)



Output:
geksfor


How does it work?

OrderedDict stores unique keys while explicitly maintaining insertion order.

Dry run: It follows the same character-by-character process as Method 1.

Interview explanation:

"I use OrderedDict.fromkeys() to remove repeated characters while preserving their original order. Finally, I use join() to convert the keys into a string."

Complexity:
- Time: O(n) average.
- Space: O(n).
Important: In modern Python (3.7+), normal dictionaries preserve insertion order. So dict.fromkeys() is usually enough; OrderedDict is generally unnecessary for this problem.
Method 3: Using a for loop with a set
s = "geeksforgeeks"seen = set()res = ""for char in s:    if char not in seen:        seen.add(char)        res += charprint(res)



Output:
geksfor


Syntax to understand:
- seen = set() — Stores characters already visited.
- char not in seen — Checks whether a character is new.
- seen.add(char) — Stores the character in the set.
- res += char — Adds the character to the result string.
Dry run:
Character	In seen?	res after processing
g	No	g
e	No	ge
e	Yes	ge
k	No	gek
s	No	geks
f	No	geksf
o	No	geksfo
r	No	geksfor
g, e, e, k, s	Yes	geksfor

Interview explanation:

"I use a set to track characters that I have already visited. If a character is not present in the set, I add it to the set and result. This preserves the original order."

Complexity of the exact code above:
- Time: O(n²) worst case — Set lookups are O(1) average, but res += char repeatedly creates new strings and copies existing characters.
- Space: O(n) — The set and result string store unique characters.
Better version for interviews:

Use a list to collect characters and join() once at the end.
s = "geeksforgeeks"seen = set()res = []for char in s:    if char not in seen:        seen.add(char)        res.append(char)result = "".join(res)print(result)



Output:
geksfor


- Time: O(n) average.
- Space: O(n).
This is the version I recommend if you want to demonstrate your own logic.
Method 4: Using list comprehension with slicing
s = "geeksforgeeks"res = "".join([    char for i, char in enumerate(s)    if char not in s[:i]])print(res)



Output:
geksfor


Syntax:
enumerate(iterable)



It gives both the index and the character.

How does it work?
- i represents the character's index.
- char represents the current character.
- s[:i] gives all characters before the current position.
- char not in s[:i] checks whether this is the first occurrence.
- "".join() combines the selected characters.
Dry run:
Index	Character	Previous characters	Keep?
0	g	""	Yes
1	e	g	Yes
2	e	ge	No
3	k	gee	Yes
4	s	geek	Yes
5	f	geeks	Yes
6	o	geeksf	Yes
7	r	geeksfo	Yes
8–12	g, e, e, k, s	Already appeared	No

Interview explanation:

"I use enumerate() to get each character's index. Then I check whether the character exists in the substring before that index. If it does not exist, I keep it."

Complexity:
- Time: O(n²) — It repeatedly creates and searches previous substrings.
- Space: O(n²) worst case for temporary slices, in addition to the output.
Part 3: Comparison and interview recommendation
List methods
Method	Time	Space	Preserves order?
dict.fromkeys()	O(n)	O(n)	Yes
set()	O(n) average	O(n)	No guarantee
Normal loop	O(n²)	O(n)	Yes
List comprehension	O(n²)	O(n)	Yes

String methods
Method	Time	Space	Preserves order?
dict.fromkeys()	O(n) average	O(n)	Yes
OrderedDict	O(n) average	O(n)	Yes
Set + string concatenation	O(n²)	O(n)	Yes
Set + list + join()	O(n) average	O(n)	Yes
Slicing + comprehension	O(n²)	O(n)	Yes

Space complexity here means auxiliary space, including the output where appropriate. These are average-case hash lookup complexities.
Which methods should you follow for interviews?
Recommended
Problem	Best method to practise
Remove duplicates from a list	for loop with seen set
Remove duplicates from a string	for loop with seen set and join()
Simple Python solution	dict.fromkeys()

Why do I recommend the set-based loop?
- It demonstrates your own programming logic.
- It preserves the original order.
- It has O(n) average time complexity.
- It is useful for many interview problems involving duplicates.
Part 4: Important interview questions
Q1. What is a duplicate?

A duplicate is an element or character that appears more than once.

Q2. What is the difference between a list and a set?

A list allows duplicate values and maintains order. A set stores unique values but does not guarantee insertion order.

Q3. Why do we use seen = set()?

To track the elements that have already appeared.

Q4. What is the purpose of append()?

It adds an element to the end of a list.

Q5. What is the purpose of join()?

It combines multiple strings into one string.

Q6. Why is dict.fromkeys() useful?

It removes duplicate keys and preserves insertion order.

Q7. What is the time complexity of removing duplicates using a set?

O(n) average, because set membership checking and insertion take O(1) average time per element.

Q8. Does set() preserve the original order?

No. Do not depend on set iteration order to preserve the original list order.

Q9. Why is the normal loop with if x not in res O(n²)?

Because checking whether an element exists in a list can take O(n), and we perform that check for every element.

Part 5: README.md – Complete revision notes
Remove Duplicates in Python
1. Remove Duplicates from a List
Problem
Remove repeated elements and preserve the first occurrence.

Input:
a = [1, 2, 2, 3, 4, 4, 5]
Output:
[1, 2, 3, 4, 5]
Method 1: dict.fromkeys()
a = [1, 2, 2, 3, 4, 4, 5]
res = list(dict.fromkeys(a))
print(res)
- Time: O(n) average
- Space: O(n)
- Preserves order.
Method 2: set()
a = [1, 2, 2, 3, 4, 4, 5]
res = list(set(a))
print(res)
- Time: O(n) average
- Space: O(n)
- Does not guarantee original order.
Method 3: Normal for loop
a = [1, 2, 2, 3, 4, 4, 5]
res = []

for x in a:
    if x not in res:
        res.append(x)

print(res)
- Time: O(n²) worst case
- Space: O(n)
- Preserves order.
Method 4: List comprehension
a = [1, 2, 2, 3, 4, 4, 5]
res = []
[res.append(x) for x in a if x not in res]
print(res)
- Time: O(n²) worst case
- Space: O(n)
- Preserves order.
- Normal for loop is more readable.
Recommended list solution: Set + for loop
a = [1, 2, 2, 3, 4, 4, 5]

seen = set()
res = []

for x in a:
    if x not in seen:
        seen.add(x)
        res.append(x)

print(res)
- Time: O(n) average
- Space: O(n)
- Preserves order.

2. Remove Duplicate Characters from a String
Problem
Remove repeated characters and preserve the first occurrence.

Input:
s = "geeksforgeeks"
Output:
geksfor
Method 1: dict.fromkeys()
s = "geeksforgeeks"
res = "".join(dict.fromkeys(s))
print(res)
- Time: O(n) average
- Space: O(n)
- Preserves order.
Method 2: OrderedDict
from collections import OrderedDict

s = "geeksforgeeks"
res = "".join(OrderedDict.fromkeys(s))
print(res)
- Time: O(n) average
- Space: O(n)
- Preserves order.
- Normal dictionaries already preserve insertion order in Python 3.7+.
Method 3: Set + for loop + list + join
s = "geeksforgeeks"

seen = set()
res = []

for char in s:
    if char not in seen:
        seen.add(char)
        res.append(char)

result = "".join(res)
print(result)
- Time: O(n) average
- Space: O(n)
- Recommended for interviews.
Method 4: enumerate() + slicing
s = "geeksforgeeks"

res = "".join([
    char for i, char in enumerate(s)
    if char not in s[:i]
])

print(res)
- Time: O(n²)
- Space: O(n) auxiliary
- Preserves order.
- Less efficient because it repeatedly creates and searches slices.

Important Python concepts
Concept	Meaning
set()	Stores unique elements
dict.fromkeys()	Creates unique dictionary keys
append()	Adds an element to a list
add()	Adds an element to a set
join()	Combines strings
enumerate()	Returns index and element
in	Checks membership
not in	Checks absenceInterview questions
1. What are duplicate elements?
2. What is the difference between list and set?
3. Why do we use a set to track visited elements?
4. Does set preserve insertion order?
5. What is the difference between append() and add()?
6. What does join() do?
7. What is the time complexity of the set-based approach?
8. Why is list membership slower than set membership?
9. How can we remove duplicates without using set()?
10. How can we remove duplicate characters while preserving order?
Interview recommendation
Practise the set-based for-loop approach for both lists and strings. Also understand dict.fromkeys() as a short built-in solution.




Part 6: Quick interview practice
Try these questions without looking at the notes.
Mini quiz
0/4 answered

1. What is the output of list(set([1, 2, 2, 3]))?

[1, 2, 2, 3]

A list containing 1, 2, 3 (order not guaranteed)

[1, 2, 2, 3, 3]




2. Which data structure is best for tracking already-seen elements efficiently?

List

Set

String




3. Why do we use ''.join(res) for the string solution?

To sort characters

To combine characters into one string

To remove spaces




4. What is the average time complexity of the set-based loop?

O(n²)

O(log n)

O(n)