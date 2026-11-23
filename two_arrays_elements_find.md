Find Common Elements in Two Arrays – Python Interview Preparation
Recommended for interviews: Hash Set approach
I'll explain this problem in simple English, with Python code, dry runs, outputs, complexity, and interview-ready answers.
1. Problem statement
What is the problem asking?

We are given two arrays. We need to find the elements that are present in both arrays.

Example 1:
arr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]



Output:
[3, 4, 5]


Why?
- 3 is present in both arrays.
- 4 is present in both arrays.
- 5 is present in both arrays.
- 1, 2 are only in the first array.
- 6, 7 are only in the second array.
Therefore, the common elements are [3, 4, 5].
2. Important definitions
Term	Simple definition
Array/List	Stores multiple elements in one variable.
Common elements	Elements present in both arrays.
Brute force	Solving a problem using straightforward comparisons.
Set	Collection of unique elements.
Intersection	Finds elements present in both sets.
Hash map	Stores data in key-value pairs.
Time complexity	Measures how execution time grows with input size.
Space complexity	Measures how extra memory usage grows.

3. Method 1: Brute Force (Using nested loops)
Beginner-friendly
What?

Compare every element in the first array with every element in the second array.

Why?

It helps us understand the basic logic without depending on advanced concepts.

Syntax:
for item in arr1:    for value in arr2:        if item == value:            # Common element



Code:
arr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]common = []for item in arr1:    for value in arr2:        if item == value:            if item not in common:                common.append(item)            breakprint(common)



Output:
[3, 4, 5]


Dry run (Tracing)
First array item	Comparison result	Action
1	No match	Skip
2	No match	Skip
3	Found in arr2	Add 3
4	Found in arr2	Add 4
5	Found in arr2	Add 5

Final result: [3, 4, 5]

Complexity:
- Time: O(n × m) – two loops compare elements.
- Auxiliary space: O(k) – stores common elements.
Here, n and m are the lengths of the two arrays, and k is the number of unique common elements.
4. Method 2: List Comprehension
What?

List comprehension is a short way to create a new list using a loop and condition.

Why?

It reduces the number of lines of code.

Syntax:
result = [expression for item in iterable if condition]



Code:
arr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]common = [item for item in arr1 if item in arr2]print(common)



Output:
[3, 4, 5]


Dry run
- item = 1 → Not in arr2 → Skip.
- item = 2 → Not in arr2 → Skip.
- item = 3 → Present → Add.
- item = 4 → Present → Add.
- item = 5 → Present → Add.
Final result: [3, 4, 5]

Complexity:
- Time: O(n × m) – list membership takes O(m) in the worst case.
- Auxiliary space: O(k) – stores matching elements.
Note: This method can return duplicates if the first array contains repeated common values.
5. Method 3: Using Sets (Recommended)
Best choice for most interviews
What?

A set is a collection that stores only unique elements.

Why?

Searching for an element in a set takes O(1) average time, which is generally faster than searching in a list.

Syntax:
set1 = set(arr1)set2 = set(arr2)result = set1.intersection(set2)



Code:
arr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]set2 = set(arr2)common = []for item in arr1:    if item in set2 and item not in common:        common.append(item)print(common)



Output:
[3, 4, 5]


Dry run
First, convert arr2 into a set.
set2 = {3, 4, 5, 6, 7}



Now check each element in arr1.
item	Is item in set2?	Result
1	No	Skip
2	No	Skip
3	Yes	Add 3
4	Yes	Add 4
5	Yes	Add 5

Final result:
[3, 4, 5]



Complexity:
- Time: O(n + m) average.
- Auxiliary space: O(m + k).
Why O(n + m)?
1. Creating a set from arr2 takes O(m) average time.
2. Traversing arr1 takes O(n) iterations.
3. Each set lookup takes O(1) average time.
4. Checking the result list for duplicates can take O(k), so for a strict O(n + m) guarantee, use another set to track already-added values.
More optimized interview version:
def find_common(arr1, arr2):    lookup = set(arr2)    added = set()    result = []    for num in arr1:        if num in lookup and num not in added:            result.append(num)            added.add(num)    return resultarr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]print(find_common(arr1, arr2))



Output:
[3, 4, 5]


This version preserves the order of the first array and avoids duplicate results.
6. Method 4: Using Set Intersection
What?

Set intersection directly finds the elements available in both sets.

Why?

Python already provides a built-in operation for this problem.

Syntax:
set1.intersection(set2)# Orset1 & set2



Code:
arr1 = [1, 2, 3, 4, 5]arr2 = [3, 4, 5, 6, 7]common = list(set(arr1) & set(arr2))print(common)



Output:
[3, 4, 5]


Note: Set output order is not guaranteed. It also removes duplicates.

Complexity:
- Time: O(n + m) average.
- Auxiliary space: O(n + m) for the converted sets and result.
7. Method 5: Using Hash Map (Frequency Counter)
What?

A hash map stores elements as keys and their frequencies as values.

Why?

This method is useful when the question asks us to consider duplicate occurrences, not just unique common elements.

Syntax:
frequency_map[num] = frequency_map.get(num, 0) + 1



Code:
def find_common(arr1, arr2):    frequency = {}    for num in arr1:        frequency[num] = frequency.get(num, 0) + 1    result = []    for num in arr2:        if frequency.get(num, 0) > 0:            result.append(num)            frequency[num] -= 1    return resultarr1 = [1, 2, 2, 3, 4]arr2 = [2, 2, 2, 3, 5]print(find_common(arr1, arr2))



Output:
[2, 2, 3]


Dry run
Initially:
frequency = {1: 1, 2: 2, 3: 1, 4: 1}



arr2 element	Frequency before	Action
2	2	Add 2, decrease to 1
2	1	Add 2, decrease to 0
2	0	Skip
3	1	Add 3, decrease to 0
5	0	Skip

Final result: [2, 2, 3]

Complexity:
- Time: O(n + m) average.
- Auxiliary space: O(n + k).
Important: This method returns the common elements according to their minimum frequency in the two arrays.
8. Method 6: Sorting + Two Pointers
What?

Sort both arrays and use two pointers to compare their elements.

Why?

It is useful when we want to understand the two-pointer technique or when the arrays are already sorted.

Code:
def find_common(arr1, arr2):    a = sorted(arr1)    b = sorted(arr2)    i = j = 0    result = []    while i < len(a) and j < len(b):        if a[i] == b[j]:            if not result or result[-1] != a[i]:                result.append(a[i])            i += 1            j += 1        elif a[i] < b[j]:            i += 1        else:            j += 1    return resultprint(find_common(    [1, 2, 3, 4, 5],    [3, 4, 5, 6, 7]))



Output:
[3, 4, 5]


Complexity:
- Time: O(n log n + m log m) – sorting both arrays.
- Auxiliary space: O(n + m) – sorted copies and result.
9. Comparison of all methods
Method	Time complexity	Extra space	Best use
Brute force	O(n × m)	O(k)	Beginners
List comprehension	O(n × m)	O(k)	Short code
Hash set	O(n + m) average	O(m + k)	Interviews
Set intersection	O(n + m) average	O(n + m)	Quick solution
Hash map	O(n + m) average	O(n + k)	Duplicate counting
Sorting + two pointers	O(n log n + m log m)	O(n + m)	Sorted arrays

Here, n and m are array lengths, and k is the number of unique common elements.
10. Interview questions (Q&A)
Q1. What are common elements?

They are the elements that are present in both arrays.

Q2. Which approach do you recommend?

I recommend the hash set approach because it provides fast searching and avoids unnecessary comparisons.

Q3. Why do we use sets?

Sets store unique elements and provide O(1) average-time lookup.

Q4. What is the difference between a set and a dictionary?

A set stores unique values, whereas a dictionary stores key-value pairs.

Q5. What if duplicate elements are present?

We can use a frequency hash map to count occurrences and find common elements according to their frequency.

Q6. Does set intersection preserve order?

No. If we need the original order, we should iterate through the first array and check elements using a set.
11. Interviewee explanation (Speak this answer)
Recommended answer
"I am given two arrays, and I need to find the elements that are present in both arrays.

First, I convert the second array into a set because searching in a set takes O(1) average time.

Then, I iterate through the first array and check whether each element exists in that set.

If the element exists, I add it to the result. I also use another set to avoid duplicates.

The average time complexity is O(n + m), and the auxiliary space complexity is O(m + k).

This approach is efficient and easy to understand."
12. Final recommendation – What should you practise?
My suggested learning order:
1. Brute force – understand the logic.
2. List comprehension – understand Python shortcuts.
3. Hash set – understand optimized searching.
4. Hash map – understand frequency counting.
5. Two pointers – understand array traversal techniques.
For your fresher Python interviews, make Method 3 (Hash Set) your main solution. Also practise explaining brute force first, followed by how the set approach improves performance.
13. Summary
- Problem: Find elements present in both arrays.
- Beginner approach: Nested loops.
- Pythonic approach: List comprehension.
- Recommended approach: Hash set.
- Duplicate-counting approach: Hash map.
- Average optimized time: O(n + m).
- Interview concept: Set, hashing, membership checking and time complexity.

----------------------------

# Reverse Each Word in a Sentence – Python

## Problem
Reverse every word in a sentence without changing the order of the words.

### Example
Input:
```python
"Hello World"
```

Output:
```text
olleH dlroW
```

## Method 1: For Loop

```python
sentence = "Hello World"
words = sentence.split()
result = []

for word in words:
    result.append(word[::-1])

output = " ".join(result)
print(output)
```

## Method 2: List Comprehension

```python
sentence = "Hello World"
result = " ".join(
    [word[::-1] for word in sentence.split()]
)
print(result)
```

## Method 3: Map and Lambda

```python
sentence = "Hello World"
result = " ".join(
    map(lambda word: word[::-1], sentence.split())
)
print(result)
```

## Method 4: Reversed

```python
sentence = "Hello World"
result = " ".join(
    "".join(reversed(word))
    for word in sentence.split()
)
print(result)
```

## Complexity

| Method | Time | Auxiliary Space |
|---|---|---|
| For loop | O(n) | O(n) |
| List comprehension | O(n) | O(n) |
| Map and lambda | O(n) | O(n) |
| Reversed | O(n) | O(n) |

## Important Python Concepts

- `split()` – separates a sentence into words.
- `[::-1]` – reverses a string.
- `append()` – adds an item to a list.
- `join()` – combines strings.
- `map()` – applies a function to each item.
- `lambda` – creates an anonymous function.
- `reversed()` – returns an iterator in reverse order.

## Interview Recommendation

Start with the for-loop approach because it clearly explains your logic. Then demonstrate list comprehension as a concise Python alternative.

Practice tip: First practise writing Method 1 without looking at the answer. Then try explaining Method 2 in your own words. This will help you demonstrate both problem-solving and Python knowledge in a fresher interview.

-------------------------------------------------------------

# Reverse Each Word in a Sentence – Python

## Problem
Reverse every word in a sentence without changing the order of the words.

### Example
Input:
```python
"Hello World"
```

Output:
```text
olleH dlroW
```

## Method 1: For Loop

```python
sentence = "Hello World"
words = sentence.split()
result = []

for word in words:
    result.append(word[::-1])

output = " ".join(result)
print(output)
```

## Method 2: List Comprehension

```python
sentence = "Hello World"
result = " ".join(
    [word[::-1] for word in sentence.split()]
)
print(result)
```

## Method 3: Map and Lambda

```python
sentence = "Hello World"
result = " ".join(
    map(lambda word: word[::-1], sentence.split())
)
print(result)
```

## Method 4: Reversed

```python
sentence = "Hello World"
result = " ".join(
    "".join(reversed(word))
    for word in sentence.split()
)
print(result)
```

## Complexity

| Method | Time | Auxiliary Space |
|---|---|---|
| For loop | O(n) | O(n) |
| List comprehension | O(n) | O(n) |
| Map and lambda | O(n) | O(n) |
| Reversed | O(n) | O(n) |

## Important Python Concepts

- `split()` – separates a sentence into words.
- `[::-1]` – reverses a string.
- `append()` – adds an item to a list.
- `join()` – combines strings.
- `map()` – applies a function to each item.
- `lambda` – creates an anonymous function.
- `reversed()` – returns an iterator in reverse order.

## Interview Recommendation

Start with the for-loop approach because it clearly explains your logic. Then demonstrate list comprehension as a concise Python alternative.

Practice tip: First practise writing Method 1 without looking at the answer. Then try explaining Method 2 in your own words. This will help you demonstrate both problem-solving and Python knowledge in a fresher interview.

-----------------------------------------------------------------
Reverse Each Word in a Sentence – Python
1. Problem statement
What is the task?

Given a sentence, reverse the characters in each word without changing the order of the words.

Example:
sentence = "Hello World"



Output:
olleH dlroW


The word Hello becomes olleH, and World becomes dlroW.

Important: We reverse each word, not the order of the words.
2. Basic definitions
Term	Meaning
Sentence	A group of words
split()	Divides a string into a list of words
Slicing [::-1]	Reverses a string
join()	Combines multiple strings into one string
List comprehension	A short way to create a list
map()	Applies a function to every item

3. Why, how, where and when?
- Why? To practise strings, loops, slicing and list operations.
- Purpose? To reverse every word while keeping the sentence's word order.
- How? Split the sentence, reverse each word, and join the words.
- Where? Python coding interviews and string-manipulation problems.
- When? When a problem asks you to reverse each word individually.
4. Method 1: Using a for loop
Best for beginners
sentence = "Hello World"words = sentence.split()result = []for word in words:    result.append(word[::-1])output = " ".join(result)print(output)



Output:
olleH dlroW


Syntax:
for item in collection:    # perform an operation



Dry run:
1. sentence.split() creates ["Hello", "World"].
2. First iteration: Hello[::-1] gives olleH.
3. Second iteration: World[::-1] gives dlroW.
4. result becomes ["olleH", "dlroW"].
5. " ".join(result) produces "olleH dlroW".
Complexity:
- Time: \(O(n)\), where \(n\) is the total number of characters. Each character is processed a constant number of times.
- Auxiliary space: \(O(n)\), for the words, reversed words and result.
5. Method 2: Using list comprehension
Recommended for interviews
sentence = "Hello World"result = " ".join([word[::-1] for word in sentence.split()])print(result)



Output:
olleH dlroW


Syntax:
[expression for item in collection]



How does it work?
- sentence.split() separates the words.
- word[::-1] reverses each word.
- List comprehension creates a list of reversed words.
- " ".join() combines them with spaces.
Dry run:
Word	Reversed word
Hello	olleH
World	dlroW

Final list: ["olleH", "dlroW"]

Final output: olleH dlroW

Complexity:
- Time: \(O(n)\) – each character is processed.
- Auxiliary space: \(O(n)\) – stores the split words and reversed result.
6. Method 3: Using map() and lambda
sentence = "Hello World"result = " ".join(map(lambda word: word[::-1], sentence.split()))print(result)



Output:
olleH dlroW


Definitions:
- map() applies a function to every item in an iterable.
- lambda creates a small anonymous function.
- word[::-1] reverses each word.
Syntax:
map(function, iterable)lambda arguments: expression



Dry run:
1. split() produces ["Hello", "World"].
2. map() applies the lambda to each word.
3. Hello becomes olleH.
4. World becomes dlroW.
5. join() combines the results.
Complexity:
- Time: \(O(n)\).
- Auxiliary space: \(O(n)\) for the output and intermediate string data.
7. Method 4: Using reversed()
sentence = "Hello World"result = " ".join(    "".join(reversed(word))    for word in sentence.split())print(result)



Output:
olleH dlroW


How does it work?
- reversed(word) returns the characters in reverse order.
- "".join() combines those characters into a reversed word.
- The outer " ".join() combines the reversed words.
Complexity:
- Time: \(O(n)\).
- Auxiliary space: \(O(n)\) for the generated words and final output.
8. Method 5: Preserve multiple spaces
Normally, split() removes extra spaces and join() puts single spaces between words.

If you want to preserve the original spaces, use split(" ").
sentence = "Hello   World"result = " ".join(    word[::-1] for word in sentence.split(" "))print(result)



Output:
olleH   dlroW


This preserves the three spaces between the words.

Complexity:
- Time: \(O(n)\).
- Auxiliary space: \(O(n)\).
9. Complexity comparison
Method	Time	Auxiliary space
For loop	\(O(n)\)	\(O(n)\)
List comprehension	\(O(n)\)	\(O(n)\)
map() + lambda	\(O(n)\)	\(O(n)\)
reversed()	\(O(n)\)	\(O(n)\)
Preserve spaces	\(O(n)\)	\(O(n)\)

Here, \(n\) represents the total number of characters. These are typical complexity estimates, excluding the input string itself.
10. Which method should you choose in an interview?
My recommendation: Method 1 – for loop for explaining your logic, then Method 2 – list comprehension as the Pythonic alternative.

From a recruiter's perspective:
- The for loop makes your logic easy to follow.
- It shows that you understand iteration, slicing and lists.
- List comprehension shows that you know Python's concise syntax.
- Both have linear time complexity, so the shorter version does not offer a meaningful speed advantage.
11. Interview questions and answers
Q1. What is the difference between split() and join()?

split() divides a string into a list. join() combines strings into one string.

Q2. What does [::-1] mean?

It is Python slicing syntax that returns a string in reverse order.

Q3. Does split() preserve multiple spaces?

No. split() without an argument treats consecutive whitespace as one separator. Use split(" ") when you need to preserve repeated spaces.

Q4. What is the difference between reversing each word and reversing word order?
- Reverse each word: "Hello World" → "olleH dlroW"
- Reverse word order: "Hello World" → "World Hello"
Q5. Which method would you choose and why?

I would choose the for loop because it is easy to understand and explain. I can also use list comprehension to write the same logic more concisely.
12. Interviewee explanation
You can say this in your interview:
First, I split the sentence into individual words using the split() method. Then I iterate through each word and reverse it using Python slicing [::-1]. I store the reversed words in a list. Finally, I use the join() method to combine them into a single sentence. The time complexity is O(n), because we process each character, and the auxiliary space complexity is O(n), because we store the reversed words.