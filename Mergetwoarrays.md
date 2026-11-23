Merge Two Lists in Python
1. Problem statement
What is the task?

Given two lists, combine all elements of the second list with the first list to create one list.

Example:
a = [1, 2, 3]b = [4, 5, 6]



Output:
[1, 2, 3, 4, 5, 6]


The elements of the second list are added after the elements of the first list.
2. Basic definitions
Term	Meaning
List	A collection of elements in Python
Merge	Combine elements from multiple lists
Concatenation	Joining two lists together
append()	Adds one item to the end of a list
extend()	Adds all items from an iterable to a list
Iterator	An object that provides items one at a time
Unpacking *	Expands the elements of an iterable

3. Why, how, where and when?
- Why? To combine data stored in separate lists.
- Purpose? To create one list containing elements from both lists.
- How? Use +, extend(), unpacking, loops or chain().
- Where? Data processing, Python applications and coding interviews.
- When? When you need to combine two or more collections.
4. Method 1: Using + operator
Recommended for most interviews
a = [1, 2, 3]b = [4, 5, 6]c = a + bprint(c)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
new_list = list1 + list2



How does it work?

The + operator concatenates both lists and creates a new list. The original lists remain unchanged.

Dry run:
Step	Operation	Result
1	a	[1, 2, 3]
2	b	[4, 5, 6]
3	a + b	[1, 2, 3, 4, 5, 6]
4	Store in c	Merged list

Complexity:
- Time: \(O(n+m)\) – Python copies all elements from both lists.
- Auxiliary space: \(O(n+m)\) – a new list is created.
5. Method 2: Using extend()
Best when modifying an existing list
a = [1, 2, 3]b = [4, 5, 6]a.extend(b)print(a)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
list1.extend(list2)



How does it work?

extend() adds every element from b to the end of a. It modifies the original list a.

Dry run:
- Initially, a = [1, 2, 3].
- b = [4, 5, 6].
- a.extend(b) adds 4, then 5, then 6.
- Final a = [1, 2, 3, 4, 5, 6].
Important interview question: append() vs extend()
a = [1, 2, 3]b = [4, 5, 6]a.append(b)print(a)



Output:
[1, 2, 3, [4, 5, 6]]


append() adds the entire list as one element. extend() adds its individual elements.

Complexity:
- Time: \(O(m)\) – it adds each element of the second list.
- Auxiliary space: \(O(1)\) auxiliary space, excluding the storage needed to grow the existing list. Python may occasionally allocate additional internal capacity.
6. Method 3: Using unpacking operator *
a = [1, 2, 3]b = [4, 5, 6]c = [*a, *b]print(c)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
new_list = [*list1, *list2]



How does it work?
- *a unpacks the elements of a.
- *b unpacks the elements of b.
- Both sets of elements are placed into a new list.
Dry run:
*a  →  1, 2, 3
*b  →  4, 5, 6

c   →  [1, 2, 3, 4, 5, 6]


Complexity:
- Time: \(O(n+m)\) – copies all elements.
- Auxiliary space: \(O(n+m)\) – creates a new list.
7. Method 4: Using a for loop
Good for demonstrating basic logic
a = [1, 2, 3]b = [4, 5, 6]result = []for item in a:    result.append(item)for item in b:    result.append(item)print(result)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
for item in collection:    result.append(item)



Dry run:

First loop:
Item	Result
1	[1]
2	[1, 2]
3	[1, 2, 3]

Second loop:
Item	Result
4	[1, 2, 3, 4]
5	[1, 2, 3, 4, 5]
6	[1, 2, 3, 4, 5, 6]

Complexity:
- Time: \(O(n+m)\) – each element is appended once.
- Auxiliary space: \(O(n+m)\) – the new result list stores all elements.
8. Method 5: Using list comprehension
a = [1, 2, 3]b = [4, 5, 6]result = [item for item in a + b]print(result)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
[expression for item in iterable]



How does it work?
- a + b first creates a combined list.
- The list comprehension iterates through that list.
- Each item is added to result.
Complexity:
- Time: \(O(n+m)\).
- Auxiliary space: \(O(n+m)\), including the temporary combined list and result list.
Note: This method is unnecessary when you only want to merge lists. Use list comprehension when you also need to transform or filter elements.
9. Method 6: Using itertools.chain()
from itertools import chaina = [1, 2, 3]b = [4, 5, 6]result = list(chain(a, b))print(result)



Output:
[1, 2, 3, 4, 5, 6]


Syntax:
from itertools import chainiterator = chain(list1, list2)



How does it work?
- chain(a, b) gives elements from a, followed by elements from b.
- It produces an iterator, not a list.
- list() converts that iterator into a list.
Complexity:
- Time: \(O(n+m)\) when fully consumed.
- Auxiliary space: \(O(1)\) for the iterator itself; \(O(n+m)\) when converted to a list because the result must be stored.
10. Complexity comparison
Here, n is the length of the first list and m is the length of the second list.
Method	Time	Extra space	Modifies original?
+ operator	O(n+m)	O(n+m)	No
extend()	O(m)	O(1)*	Yes
* unpacking	O(n+m)	O(n+m)	No
For loop	O(n+m)	O(n+m)	No
List comprehension	O(n+m)	O(n+m)	No
chain() iterator	O(n+m)	O(1)*	No

*Excludes the output or internal list growth. For chain(), O(1) is iterator overhead; converting it to a list requires O(n+m) space.
11. Which method should you choose in an interview?
My recommendation: Learn the for loop first, and use the + operator as your main answer when the interviewer simply asks to merge two lists.
- + is simple, readable and creates a new list.
- extend() is best when you want to modify the first list.
- for loop demonstrates your understanding of iteration and append().
- chain() is useful when processing large iterables without immediately creating a list.
There is no need to use a complicated method for a simple merging problem.
12. Interview questions and answers
Q1. What is list merging?

Combining elements from two or more lists into one list.

Q2. What is the difference between + and extend()?

+ creates a new list, whereas extend() modifies the existing list.

Q3. What happens if we use append() instead of extend()?

The entire second list is added as a single nested element.

Q4. Does merging remove duplicate elements?

No. Normal list merging keeps duplicates.

Example:
[1, 2] + [2, 3]



Output: [1, 2, 2, 3]

Q5. What does chain() return?

It returns an iterator, not a list.

Q6. Which method would you choose?

I would use + because it is simple and creates a new list without modifying the original lists.
13. Interviewee explanation
You can say:
I am given two lists, and I need to combine their elements into a single list. I can use the plus operator to concatenate both lists. It creates a new list and keeps the original lists unchanged. The time complexity is O(n + m), because Python copies all elements from both lists. The extra space complexity is also O(n + m), because a new list is created. If I need to modify the first list directly, I can use the extend() method.
----------------------------------

# Merge Two Lists in Python

## Problem Statement
Given two lists, combine all elements into one list.

### Example
Input:
```python
a = [1, 2, 3]
b = [4, 5, 6]
```

Output:
```text
[1, 2, 3, 4, 5, 6]
```

## Methods

### 1. Using + operator
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
```

### 2. Using extend()
```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
```

### 3. Using unpacking
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c)
```

### 4. Using for loop
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = []

for item in a:
    result.append(item)

for item in b:
    result.append(item)

print(result)
```

### 5. Using list comprehension
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = [item for item in a + b]
print(result)
```

### 6. Using itertools.chain()
```python
from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]

result = list(chain(a, b))
print(result)
```

## Complexity Comparison

| Method | Time | Extra Space |
|---|---|---|
| + operator | O(n+m) | O(n+m) |
| extend() | O(m) | O(1)* |
| Unpacking | O(n+m) | O(n+m) |
| For loop | O(n+m) | O(n+m) |
| List comprehension | O(n+m) | O(n+m) |
| chain() iterator | O(n+m) | O(1)* |

*Excludes output storage and internal list growth. Converting chain() to a list requires O(n+m) space.*

## Important Concepts
- `+`: Concatenates lists.
- `extend()`: Adds individual elements.
- `append()`: Adds one item.
- `*`: Unpacks iterable elements.
- `chain()`: Creates an iterator over multiple iterables.

## Interview Recommendation
Use the `+` operator for simple list merging.
Understand the for-loop approach to explain the logic.
Use `extend()` when modifying the first list.

## Key Point
Merging lists does not automatically remove duplicate elements.

Practice task: Try merging [10, 20, 30] and [30, 40, 50]. Check whether the duplicate 30 remains in the output.

<!-- ----------------------------------------- -->
Merge Two Arrays in Python – Interview Preparation
1. Problem statement
What is the task?

Given two arrays, combine all their elements into a single array while maintaining their original order.

In Python, we commonly use lists as arrays.

Example:
array1 = [1, 3, 5]array2 = [2, 4, 6]



Output:
[1, 3, 5, 2, 4, 6]


Notice that the elements are combined, but they are not sorted.
2. Basic definitions
Term	Meaning
Array	A collection of elements
Python list	An ordered, mutable collection
Merge	Combine two collections
append()	Add one item to a list
extend()	Add all elements from another iterable
Concatenation	Joining two lists
Unpacking *	Expanding elements into another list
Iterator	Provides elements one at a time

3. Why, how, where and when?
- Why? To combine data from two separate collections.
- Purpose? To create one collection containing all elements.
- How? Use a loop, +, extend(), unpacking or itertools.chain().
- Where? Data processing, record management and coding interviews.
- When? When a problem asks you to combine two arrays or lists.
4. Method 1: Using a for loop
Best for understanding the logic
array1 = [1, 3, 5]array2 = [2, 4, 6]for num in array2:    array1.append(num)print(array1)



Output:
[1, 3, 5, 2, 4, 6]


Syntax:
for item in iterable:    list.append(item)



How does it work?

The loop visits each element in array2 and adds it to array1 using append().

Dry run:
Iteration	num	array1
Initially	—	[1, 3, 5]
1	2	[1, 3, 5, 2]
2	4	[1, 3, 5, 2, 4]
3	6	[1, 3, 5, 2, 4, 6]

Complexity:
- Time: \(O(m)\) – the loop visits every element in array2 once.
- Auxiliary space: \(O(1)\) – no separate result list is created, although array1 grows to hold the new elements.
Here, m is the length of array2.
5. Method 2: Using + operator
Recommended for simple interview questions
array1 = [7, 9, 11]array2 = [8, 10, 12]merged = array1 + array2print(merged)



Output:
[7, 9, 11, 8, 10, 12]


Syntax:
merged = list1 + list2



How does it work?

The + operator combines both lists and creates a new list. The original lists remain unchanged.

Dry run:
array1 = [7, 9, 11]
array2 = [8, 10, 12]

array1 + array2

merged = [7, 9, 11, 8, 10, 12]


Complexity:
- Time: \(O(n+m)\) – all elements from both lists are copied.
- Auxiliary space: \(O(n+m)\) – a new list stores all elements.
6. Method 3: Using extend()
Best for modifying an existing list
array1 = ['a', 'b', 'c']array2 = ['d', 'e', 'f']array1.extend(array2)print(array1)



Output:
['a', 'b', 'c', 'd', 'e', 'f']


Syntax:
list1.extend(list2)



How does it work?

extend() adds all elements of array2 to the end of array1.

Dry run:
Before:
array1 = ['a', 'b', 'c']

After:
array1.extend(array2)

array1 = ['a', 'b', 'c', 'd', 'e', 'f']


Complexity:
- Time: \(O(m)\) – each element of the second list is added once.
- Auxiliary space: \(O(1)\) – excluding the extra storage required as the existing list grows.
Important: extend() modifies the original list.
7. Method 4: Using unpacking operator *
array1 = [10, 20, 30]array2 = [40, 50, 60]merged = [*array1, *array2]print(merged)



Output:
[10, 20, 30, 40, 50, 60]


Syntax:
merged = [*list1, *list2]



How does it work?
- *array1 expands the elements of the first list.
- *array2 expands the elements of the second list.
- Both are stored in a new list.
Dry run:
*array1 → 10, 20, 30
*array2 → 40, 50, 60

merged → [10, 20, 30, 40, 50, 60]


Complexity:
- Time: \(O(n+m)\) – copies all elements.
- Auxiliary space: \(O(n+m)\) – creates a new list.
8. Method 5: Using itertools.chain()
from itertools import chainarray1 = [15, 25, 35]array2 = [45, 55, 65]merged = list(chain(array1, array2))print(merged)



Output:
[15, 25, 35, 45, 55, 65]


Syntax:
from itertools import chainresult = chain(list1, list2)



How does it work?
- chain() provides elements from the first list, followed by the second list.
- It returns an iterator, not a list.
- list() converts the iterator into a list.
Dry run:
chain(array1, array2)
       ↓
15, 25, 35, 45, 55, 65
       ↓
list(...)
       ↓
[15, 25, 35, 45, 55, 65]


Complexity:
- Time: \(O(n+m)\) when all elements are processed.
- Auxiliary space: \(O(1)\) for the iterator itself.
- If converted using list(): \(O(n+m)\) space for the resulting list.
9. Complexity comparison
Here, n = length of the first array and m = length of the second array.
Method	Time	Auxiliary space	Modifies original?
For loop + append	O(m)	O(1)*	Yes
+ operator	O(n+m)	O(n+m)	No
extend()	O(m)	O(1)*	Yes
Unpacking *	O(n+m)	O(n+m)	No
chain() iterator	O(n+m)	O(1)*	No

*O(1) excludes the storage needed to grow an existing list. For chain(), it excludes the output list; converting to a list requires O(n+m) space.

Why are the complexities different?
- A loop and extend() add only the second list's m elements to the existing first list.
- + and unpacking copy both lists into a new list.
- chain() does not immediately create a combined list; it produces elements when requested.
10. Which method should you choose in an interview?
My recommendation is to learn these two methods first:
1. For loop + append() – to demonstrate your basic programming logic.
2. + operator – as your main answer when the interviewer simply asks to merge two lists.
Use extend() if the interviewer asks you to modify the first list.

From a recruiter's perspective, explaining why you selected a method is more important than memorising five methods.
11. Interview questions and answers
Q1. What is merging two arrays?

Combining the elements of two arrays into one array.

Q2. What is the difference between append() and extend()?

append() adds one item. extend() adds all individual elements from another iterable.

Q3. What is the difference between + and extend()?

+ creates a new list. extend() modifies the existing list.

Q4. Does merging remove duplicate elements?

No. Normal merging preserves duplicates.

Example:
[1, 2, 3] + [3, 4, 5]



Output:
[1, 2, 3, 3, 4, 5]


Q5. What does chain() return?

It returns an iterator, which can be converted into a list using list().

Q6. What is the best method for large data?

If I only need to process elements one by one, chain() avoids creating a combined list immediately. If I need an actual merged list, I must store the output.
12. Interviewee explanation
You can say:
I am given two arrays, and I need to combine their elements into a single array. In Python, I can use lists for this task. First, I can use a for loop to iterate through the second list and append each element to the first list. This takes O(m) time because I process the second list once. Alternatively, I can use the plus operator to create a new merged list. That takes O(n + m) time and O(n + m) extra space.

13. Summary
- for loop: Good for understanding the logic.
- +: Simple way to create a new merged list.
- extend(): Adds elements to an existing list.
- *: Unpacks elements into a new list.
- chain(): Useful for processing elements without immediately creating a combined list.
- Normal merging does not remove duplicates or sort elements.


# Merge Two Arrays in Python

## Problem Statement
Given two arrays, combine their elements into one array.

### Example
Input:
```python
array1 = [1, 3, 5]
array2 = [2, 4, 6]
```

Output:
```text
[1, 3, 5, 2, 4, 6]
```

## Method 1: For Loop

```python
array1 = [1, 3, 5]
array2 = [2, 4, 6]

for num in array2:
    array1.append(num)

print(array1)
```

## Method 2: Plus Operator

```python
array1 = [7, 9, 11]
array2 = [8, 10, 12]

merged = array1 + array2
print(merged)
```

## Method 3: extend()

```python
array1 = ['a', 'b', 'c']
array2 = ['d', 'e', 'f']

array1.extend(array2)
print(array1)
```

## Method 4: Unpacking Operator

```python
array1 = [10, 20, 30]
array2 = [40, 50, 60]

merged = [*array1, *array2]
print(merged)
```

## Method 5: itertools.chain()

```python
from itertools import chain

array1 = [15, 25, 35]
array2 = [45, 55, 65]

merged = list(chain(array1, array2))
print(merged)
```

## Complexity Comparison

| Method | Time | Auxiliary Space |
|---|---|---|
| For loop | O(m) | O(1)* |
| + operator | O(n+m) | O(n+m) |
| extend() | O(m) | O(1)* |
| Unpacking | O(n+m) | O(n+m) |
| chain() iterator | O(n+m) | O(1)* |

*Excludes storage needed to grow the existing list or store the final output.*

## Important Concepts

- append(): Adds one item.
- extend(): Adds multiple elements.
- +: Concatenates lists.
- *: Unpacks iterable elements.
- chain(): Combines iterables into an iterator.
- list(): Converts an iterable into a list.

## Interview Recommendation

- Use a for loop to explain the basic logic.
- Use + for simple list merging.
- Use extend() when modifying the first list.
- Use chain() when processing elements lazily.

## Important Note

Merging does not automatically sort or remove duplicate elements.

--------------------------------------
# Merge Two Arrays in Python

## Problem Statement
Given two arrays, combine their elements into one array.

### Example
Input:
```python
array1 = [1, 3, 5]
array2 = [2, 4, 6]
```

Output:
```text
[1, 3, 5, 2, 4, 6]
```

## Method 1: For Loop

```python
array1 = [1, 3, 5]
array2 = [2, 4, 6]

for num in array2:
    array1.append(num)

print(array1)
```

## Method 2: Plus Operator

```python
array1 = [7, 9, 11]
array2 = [8, 10, 12]

merged = array1 + array2
print(merged)
```

## Method 3: extend()

```python
array1 = ['a', 'b', 'c']
array2 = ['d', 'e', 'f']

array1.extend(array2)
print(array1)
```

## Method 4: Unpacking Operator

```python
array1 = [10, 20, 30]
array2 = [40, 50, 60]

merged = [*array1, *array2]
print(merged)
```

## Method 5: itertools.chain()

```python
from itertools import chain

array1 = [15, 25, 35]
array2 = [45, 55, 65]

merged = list(chain(array1, array2))
print(merged)
```

## Complexity Comparison

| Method | Time | Auxiliary Space |
|---|---|---|
| For loop | O(m) | O(1)* |
| + operator | O(n+m) | O(n+m) |
| extend() | O(m) | O(1)* |
| Unpacking | O(n+m) | O(n+m) |
| chain() iterator | O(n+m) | O(1)* |

*Excludes storage needed to grow the existing list or store the final output.*

## Important Concepts

- append(): Adds one item.
- extend(): Adds multiple elements.
- +: Concatenates lists.
- *: Unpacks iterable elements.
- chain(): Combines iterables into an iterator.
- list(): Converts an iterable into a list.

## Interview Recommendation

- Use a for loop to explain the basic logic.
- Use + for simple list merging.
- Use extend() when modifying the first list.
- Use chain() when processing elements lazily.

## Important Note

Merging does not automatically sort or remove duplicate elements.
