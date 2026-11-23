Python Program to Find the Average of a List
1. Problem statement
Given a list of numbers, calculate the average of all elements.

Example:
numbers = [10, 20, 30, 40]



Output:
Sum: 100
Average: 25.0


Formula:
\[
\text{Average} = \frac{\text{Sum of all elements}}{\text{Number of elements}}
\]

2. Definition, purpose and uses
- Definition: Average is the sum of all numbers divided by the total number of elements.
- Purpose: To find the central value of a group of numbers.
- Why: It helps us understand the overall value of a collection.
- Where: Student marks, employee salaries, sales reports and data analysis.
3. Important Python syntax
Syntax	Purpose
sum(numbers)	Calculates the total
len(numbers)	Counts the elements
total / count	Calculates the average
for num in numbers	Iterates through elements
statistics.mean()	Calculates the arithmetic mean

4. Method 1: Using sum() and len()
Recommended for everyday Python
numbers = [10, 20, 30, 40]total = sum(numbers)count = len(numbers)average = total / countprint("Sum:", total)print("Average:", average)



Output:
Sum: 100
Average: 25.0


How it works:
1. sum() adds all numbers.
2. len() counts the elements.
3. Divide the total by the count.
Dry run:
Operation	Calculation	Result
Sum	10 + 20 + 30 + 40	100
Count	Number of elements	4
Average	100 / 4	25.0

Complexity:
- Time: O(n) — sum() visits all n elements; len() takes O(1).
- Auxiliary space: O(1) — no additional collection is created.
5. Method 2: Using a for loop
Recommended for coding interviews
This method calculates the sum manually without using sum().
numbers = [10, 20, 30, 40]total = 0for num in numbers:    total += numaverage = total / len(numbers)print("Sum:", total)print("Average:", average)



Output:
Sum: 100
Average: 25.0


How it works:
- Initialize total = 0.
- Visit each number using the loop.
- Add each number to total.
- Divide the total by the number of elements.
Dry run:
Iteration	num	total
Initial	—	0
1	10	10
2	20	30
3	30	60
4	40	100

Finally:

average = 100 / 4 = 25.0

Complexity:
- Time: O(n) — the loop visits every element once.
- Auxiliary space: O(1) — only the total, num and average variables are used.
6. Method 3: Using the statistics module
Python provides a built-in module called statistics to calculate the average.
import statisticsnumbers = [10, 20, 30, 40]average = statistics.mean(numbers)print("Average:", average)



Output:
Average: 25


How it works:
- import statistics imports Python's statistics module.
- statistics.mean() calculates the arithmetic mean.
- It adds the numbers and divides by their count.
Syntax:
statistics.mean(iterable)



Complexity:
- Time: O(n) — it processes all elements.
- Auxiliary space: O(1) for a list input in the standard implementation.
When to use: When your program performs statistical calculations and you want a clear, meaningful function name.
7. Method 4: Using NumPy
NumPy is a third-party Python library commonly used for numerical and scientific computing.
import numpy as npnumbers = np.array([10, 20, 30, 40])average = np.mean(numbers)print("Average:", average)



Output:
Average: 25.0


How it works:
- np.array() creates a NumPy array.
- np.mean() calculates its average.
Complexity:
- Time: O(n) — every element contributes to the average.
- Auxiliary space: O(1) for the mean calculation on an existing array, excluding implementation overhead.
When to use: Large numerical datasets, scientific calculations and multi-dimensional arrays. NumPy must be installed separately.
8. Handling an empty list
An empty list has no numbers, so its average cannot be calculated.
numbers = []if numbers:    average = sum(numbers) / len(numbers)    print("Average:", average)else:    print("List is empty")



Output:
List is empty


Why is this check important?

If we calculate sum(numbers) / len(numbers) directly, Python attempts to divide by zero and raises ZeroDivisionError.
9. Method comparison
Method	Time	Best use
sum() / len()	O(n)	Everyday Python
for loop	O(n)	Coding interviews
statistics.mean()	O(n)	Statistical calculations
numpy.mean()	O(n)	Numerical datasets

10. Which method should you follow for interviews?
My recommendation:
1. First priority: for loop – It demonstrates your problem-solving skills and understanding of loops, variables and arithmetic.
2. Second priority: sum() and len() – It demonstrates your knowledge of Python built-in functions.
A recruiter or interviewer may ask you to solve the problem without built-in functions. So practise the loop method first.
11. Interview questions and answers
Q1. What is the formula for average?

Average = Sum of all elements / Number of elements.

Q2. Why do we initialize total = 0?

Because zero is the starting value when adding numbers.

Q3. What is the difference between sum() and len()?
- sum() calculates the total.
- len() counts the elements.
Q4. Why do we check for an empty list?

To avoid ZeroDivisionError when dividing by zero.

Q5. What is the time complexity?

O(n), because we visit all elements to calculate their sum.

Q6. What is the auxiliary space complexity?

O(1), because we use only a fixed number of extra variables.
12. Interviewee explanation
You can explain the loop method like this:
First, I initialize a variable called total to zero. Then I use a for loop to iterate through the list and add each number to the total. After calculating the sum, I divide it by the number of elements using the len() function. Finally, I print the average. The time complexity is O(n), and the auxiliary space complexity is O(1).

13. What, why, how, where and when – revision
Question	Answer
What?	Find the average of a list of numbers.
Why?	To calculate the central value of the numbers.
How?	Add all numbers and divide by their count.
Where?	Marks, salaries, sales and data analysis.
When?	Whenever we need the average of numerical values.
----------------------------------------------------

# Find Average of a List – Python

## Problem Statement

Given a list of numbers, calculate the sum and average of its elements.

### Example

Input:
```python
numbers = [10, 20, 30, 40]
```

Output:
```text
Sum: 100
Average: 25.0
```

## Formula

Average = Sum of elements / Number of elements

## Method 1: Using sum() and len()

```python
numbers = [10, 20, 30, 40]

total = sum(numbers)
count = len(numbers)
average = total / count

print("Sum:", total)
print("Average:", average)
```

Time Complexity: O(n)

Auxiliary Space: O(1)

## Method 2: Using For Loop

```python
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
```

Time Complexity: O(n)

Auxiliary Space: O(1)

## Method 3: Using statistics.mean()

```python
import statistics

numbers = [10, 20, 30, 40]

average = statistics.mean(numbers)

print("Average:", average)
```

Time Complexity: O(n)

Auxiliary Space: O(1)

## Method 4: Using NumPy

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

average = np.mean(numbers)

print("Average:", average)
```

Time Complexity: O(n)

Auxiliary Space: O(1), excluding implementation overhead.

## Handling Empty Lists

```python
numbers = []

if numbers:
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print("List is empty")
```

## Interview Recommendation

The for loop method is recommended for coding interviews because it demonstrates basic programming logic.

The sum() and len() method is recommended for everyday Python programming.

## Important Concepts

- sum()
- len()
- for loop
- statistics.mean()
- numpy.mean()
- Time Complexity
- Auxiliary Space Complexity
- ZeroDivisionError

Final takeaway: Remember this simple logic: Average = Total / Count. Practise the for loop method first, then the built-in sum() and len() method.

<!-- --------------------------------------------------------------- -->
# Python Program to Add Two Lists Element by Element

## 1. Problem Statement

Given two lists, add the elements at the same index and store the results in a new list.

**Example:**

```python
a = [1, 2, 3]
b = [4, 5, 6]
```

**Expected Output:**

```python
[5, 7, 9]
```

**Explanation:**
- 1 + 4 = 5
- 2 + 5 = 7
- 3 + 6 = 9

The goal is to add corresponding elements, not calculate the total sum of both lists.

---

## 2. Definition, Purpose and Uses

**Definition:** Element-by-element addition means adding elements from two lists that have the same index.

**Why:** To combine corresponding values from two lists.

**Purpose:** To create a new list containing the addition results.

**Where:** Marks calculation, monthly sales, prices and numerical data processing.

**When:** When two lists contain related values that need to be added position by position.

---

## 3. Important Python Syntax

| Syntax | Purpose |
|---|---|
| `range()` | Generates indexes |
| `len()` | Returns the number of elements |
| `append()` | Adds an element to a list |
| `zip()` | Combines corresponding elements |
| `map()` | Applies a function to elements |
| `operator.add` | Performs addition |
| `zip_longest()` | Combines elements even when lengths differ |

---

## 4. Method 1: Using a For Loop (Recommended for Interviews)

### Code

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)
```

**Output:**

```python
[5, 7, 9]
```

### How does it work?

1. Create an empty list called `result`.
2. `len(a)` returns 3.
3. `range(len(a))` generates indexes 0, 1, 2.
4. `a[i] + b[i]` adds the elements at the same index.
5. `append()` stores each answer in the result list.
6. Finally, print the result.

### Dry Run (Tracing)

| Iteration | i | a[i] | b[i] | Addition | Result |
|---|---:|---:|---:|---|---|
| 1 | 0 | 1 | 4 | 1 + 4 = 5 | [5] |
| 2 | 1 | 2 | 5 | 2 + 5 = 7 | [5, 7] |
| 3 | 2 | 3 | 6 | 3 + 6 = 9 | [5, 7, 9] |

**Final Output:** `[5, 7, 9]`

### Important Syntax

```python
for i in range(len(a)):
    result.append(a[i] + b[i])
```

- `len(a)` – Gets the list length.
- `range()` – Generates indexes.
- `a[i]` – Accesses an element from the first list.
- `b[i]` – Accesses an element from the second list.
- `append()` – Stores the calculated value.

### Time and Space Complexity

- **Time Complexity: O(n)** – The loop runs n times, and each iteration performs one addition.
- **Auxiliary Space Complexity: O(n)** – A new result list stores n elements.

---

## 5. Method 2: Using zip() and List Comprehension

### Code

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = [x + y for x, y in zip(a, b)]

print(result)
```

**Output:**

```python
[5, 7, 9]
```

### Definition

`zip()` combines corresponding elements from two or more iterables.

### How does it work?

1. `zip(a, b)` combines matching elements.
2. `x` receives an element from the first list.
3. `y` receives an element from the second list.
4. `x + y` performs addition.
5. List comprehension stores the results in a new list.

### Dry Run

| Iteration | x | y | x + y |
|---|---:|---:|---:|
| 1 | 1 | 4 | 5 |
| 2 | 2 | 5 | 7 |
| 3 | 3 | 6 | 9 |

**Final Output:** `[5, 7, 9]`

### Syntax

```python
[expression for variable in iterable]
```

### Complexity

- **Time: O(n)** – Each pair is processed once.
- **Auxiliary Space: O(n)** – The new result list stores n elements.

**When to use:** When you want clean, short and Pythonic code.

---

## 6. Method 3: Using map() and operator.add

### Code

```python
import operator

a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(operator.add, a, b))

print(result)
```

**Output:**

```python
[5, 7, 9]
```

### How does it work?

- `operator.add` performs addition.
- `map()` applies addition to corresponding elements.
- `list()` converts the map object into a list.

### Dry Run

| a | b | operator.add(a, b) |
|---:|---:|---:|
| 1 | 4 | 5 |
| 2 | 5 | 7 |
| 3 | 6 | 9 |

**Final Output:** `[5, 7, 9]`

### Syntax

```python
map(function, iterable1, iterable2)
```

### Complexity

- **Time: O(n)** – One addition is performed for each pair.
- **Auxiliary Space: O(n)** – The resulting list stores n elements.

**When to use:** When you are comfortable with Python's functional programming features.

---

## 7. Method 4: Using NumPy

### Code

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a + b

print(result)
```

**Output:**

```python
[5 7 9]
```

### How does it work?

1. `np.array()` converts Python lists into NumPy arrays.
2. The `+` operator adds corresponding elements.
3. The result is a new NumPy array.

### Dry Run

| First Array | Second Array | Result |
|---:|---:|---:|
| 1 | 4 | 5 |
| 2 | 5 | 7 |
| 3 | 6 | 9 |

### Complexity

- **Time: O(n)** – Each element is processed once.
- **Auxiliary Space: O(n)** – A new result array is created.

**When to use:** For numerical calculations, data science and large datasets.

Note: NumPy must be installed separately.

---

## 8. Important Interview Question: What If Lists Have Different Lengths?

Example:

```python
a = [1, 2, 3]
b = [4, 5]

result = [x + y for x, y in zip(a, b)]

print(result)
```

**Output:**

```python
[5, 7]
```

**Why?**

By default, `zip()` stops when the shortest list ends. Therefore, the extra element `3` is ignored.

### Alternative: Using zip_longest()

If missing elements should be treated as zero:

```python
from itertools import zip_longest

a = [1, 2, 3]
b = [4, 5]

result = [
    x + y
    for x, y in zip_longest(a, b, fillvalue=0)
]

print(result)
```

**Output:**

```python
[5, 7, 3]
```

**Why?** `fillvalue=0` replaces missing elements with zero.

---

## 9. Method Comparison

| Method | Time | Best Use |
|---|---|---|
| For loop | O(n) | Coding interviews |
| zip() + comprehension | O(n) | Clean Python code |
| map() + operator.add | O(n) | Functional programming |
| NumPy | O(n) | Numerical calculations |

Here, n represents the number of elements processed. For normal `zip()`, it is the length of the shorter list.

---

## 10. Which Method Should You Follow in Interviews?

**My recommendation:**

1. First priority: `for` loop – Demonstrates your basic programming logic.
2. Second priority: `zip()` – Demonstrates Python knowledge and clean coding.
3. Third priority: `map()` – Useful additional knowledge.
4. Fourth priority: NumPy – Useful for numerical applications.

**Recruiter's point of view:**

When you solve a problem using a for loop, the interviewer can easily understand your knowledge of:
- Loops and indexes.
- List operations.
- Addition and variables.
- Problem-solving logic.
- Time and space complexity.

You should be able to explain the logic, not just write the code.

---

## 11. Interview Questions and Answers

**Q1. What is the purpose of this program?**

To add corresponding elements from two lists and store the results in a new list.

**Q2. Why do we use `range(len(a))`?**

To generate indexes and access elements from both lists.

**Q3. Why do we use `append()`?**

To add each calculated result to the new list.

**Q4. What is `zip()` in Python?**

It combines corresponding elements from multiple iterables.

**Q5. What happens if two lists have different lengths?**

Normal `zip()` stops at the shortest list.

**Q6. What is the difference between `append()` and `extend()`?**

`append()` adds one item, whereas `extend()` adds multiple items from an iterable.

**Q7. What is the time complexity?**

O(n), because we process each corresponding pair once.

**Q8. What is the auxiliary space complexity?**

O(n), because we create a new result list containing n elements.

---

## 12. Interviewee Explanation (Natural English)

"I first create an empty list called result. Then I use a for loop with the range function to access the indexes of both lists. At each index, I add the corresponding elements and store the result using append(). Finally, I print the new list.

The time complexity is O(n) because the loop runs n times. The auxiliary space complexity is O(n) because we create a new list to store the results."

---

## 13. What, Why, How, Where and When – Quick Revision

| Question | Simple Answer |
|---|---|
| What? | Adding corresponding elements from two lists. |
| Why? | To combine values at matching positions. |
| Purpose? | To create a new list of addition results. |
| How? | Using indexes, loops or zip(). |
| Where? | Marks, prices and sales calculations. |
| When? | When two lists contain related numerical values. |

---

## 14. Final Summary

- **Problem:** Add elements at the same index in two lists.
- **Recommended interview method:** For loop.
- **Pythonic method:** zip() + list comprehension.
- **Output:** `[5, 7, 9]`
- **Time Complexity:** O(n).
- **Auxiliary Space Complexity:** O(n).

**Remember:** Understand the for loop first, practise the dry run, and then learn the shorter Pythonic solution. This will help you explain your logic confidently in a fresher coding interview.