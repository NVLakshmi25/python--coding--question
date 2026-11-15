Python Program to Find the Largest Number in a List
1. Problem definition
Problem: Given a list of numbers, find and return the largest number.

Example:
a = [10, 24, 76, 23, 12]



Output:
76


Meaning: We compare the numbers and identify the number that has the highest value.
2. Why and where do we use this?
- Why: To identify the highest value in a collection of numbers.
- Purpose: Find the maximum value without manually checking every number.
- Where: Student marks, employee salaries, product prices, sales reports.
- When: Whenever we need the highest value from a list or collection.
3. Different methods
Method 1: Using max() — Recommended
Python provides a built-in function called max() to find the largest element.
a = [10, 24, 76, 23, 12]res = max(a)print(res)



Output:
76


Syntax:
max(iterable)



Dry run:

Internally, Python compares the elements:
Comparison	Larger value
10 and 24	24
24 and 76	76
76 and 23	76
76 and 12	76

Final result: 76

Interview explanation:

"I used Python's built-in max() function. It compares the elements in the list and returns the largest value. It is simple, readable, and efficient."

Complexity:
- Time: O(n) — It needs to examine all n elements.
- Auxiliary space: O(1) — It does not need another list to store the result.
Method 2: Using a for loop — Best for learning logic
a = [10, 24, 76, 23, 12]res = a[0]for n in a:    if n > res:        res = nprint(res)



Output:
76


Syntax to understand:
- a[0] — Gets the first element.
- for n in a — Visits each element.
- if n > res — Checks whether the current number is larger.
- res = n — Updates the largest value.
Dry run:
Current n	res before comparison	Condition	res after
10	10	10 > 10 (False)	10
24	10	24 > 10 (True)	24
76	24	76 > 24 (True)	76
23	76	23 > 76 (False)	76
12	76	12 > 76 (False)	76

Final result: 76

Why do we write res = a[0]?

We assume the first element is the largest initially. Then we compare the remaining elements with it.

Interview explanation:

"I initialize a variable with the first element. Then I iterate through the list and compare each element with the current largest value. If I find a bigger number, I update the variable. Finally, I print the largest number."

Complexity:
- Time: O(n) — We visit every element once.
- Auxiliary space: O(1) — We use only one extra variable, res.
Method 3: Using reduce() from functools
reduce() applies a function repeatedly to combine list elements into one result.
from functools import reducea = [10, 24, 76, 23, 12]res = reduce(lambda x, y: x if x > y else y, a)print(res)



Output:
76


Syntax:
reduce(function, iterable)



How does the lambda work?
lambda x, y: x if x > y else y



- If x > y, return x.
- Otherwise, return y.
Dry run:
Comparison	Result
10 and 24	24
24 and 76	76
76 and 23	76
76 and 12	76

Final result: 76

Interview explanation:

"I use reduce() to compare two elements at a time. It keeps the larger value and continues until all elements are processed. Finally, it returns the largest number."

Complexity:
- Time: O(n) — It processes the list elements once.
- Auxiliary space: O(1) — The reduction itself uses a constant amount of extra working space.
Method 4: Using sort()
The sort() method arranges the list in ascending order. The last element will be the largest.
a = [10, 24, 76, 23, 12]a.sort()res = a[-1]print(res)



Output:
76


Syntax:
list.sort()



Dry run:

Original list:
[10, 24, 76, 23, 12]


After sorting:
[10, 12, 23, 24, 76]


Access the last element:
a[-1]  # 76



Interview explanation:

"I use the sort() method to arrange the numbers in ascending order. Then I access the last element using a[-1], which gives the largest number."

Complexity:
- Time: O(n log n) — Sorting requires more work than a single traversal.
- Auxiliary space: O(n) worst case — Python's sorting algorithm may use temporary memory.
- Note: sort() changes the original list.
4. Comparison of all methods
Method	Time complexity	Auxiliary space
max()	O(n)	O(1)
for loop	O(n)	O(1)
reduce()	O(n)	O(1)
sort()	O(n log n)	O(n) worst case

5. Which method should you follow for interviews?
My recommendation
 Practise the for loop first, and know max() as the simplest Python solution.
1. For coding interviews: Use the for loop. It demonstrates your problem-solving logic.
2. For real-world Python programs: Use max() when you simply need the largest value.
3. For understanding functional programming: Learn reduce().
4. For sorting-related problems: Use sort(), but don't sort just to find the maximum.
Important: These examples assume the list is not empty. For an empty list, handle that case before accessing a[0] or a[-1], or calling max().
6. Interview questions and answers
Q1. What is the largest number in a list?

The largest number is the element with the highest value in the list.

Q2. Which Python function finds the largest number?

The max() function.

Q3. Why do we initialize res = a[0]?

To use the first element as the initial largest value for comparison.

Q4. Why do we use if n > res?

To check whether the current element is greater than the largest value found so far.

Q5. What is the time complexity of the loop method?

O(n), because we visit each element once.

Q6. Why is sort() not the best choice for this problem?

Because sorting takes O(n log n) time, while max() and a loop take O(n) time.

Q7. What happens if the list is empty?

There is no largest element. We should check whether the list is empty before finding the maximum.

Q8. What is the difference between sort() and max()?

sort() arranges all elements, whereas max() returns only the largest element.
7. README.md – Revision notes
Find the Largest Number in a List – Python
Problem
Given a list of numbers, find the largest number.

Example:
a = [10, 24, 76, 23, 12]
Output: 76
Method 1: Using max()
a = [10, 24, 76, 23, 12]
res = max(a)
print(res)
- Time: O(n)
- Auxiliary Space: O(1)
- Best for simple Python programs.
Method 2: Using a for loop
a = [10, 24, 76, 23, 12]

res = a[0]

for n in a:
    if n > res:
        res = n

print(res)
- Time: O(n)
- Auxiliary Space: O(1)
- Recommended for coding interviews because it demonstrates logic.
Method 3: Using reduce()
from functools import reduce

a = [10, 24, 76, 23, 12]
res = reduce(lambda x, y: x if x > y else y, a)
print(res)
- Time: O(n)
- Auxiliary Space: O(1)
Method 4: Using sort()
a = [10, 24, 76, 23, 12]
a.sort()
res = a[-1]
print(res)
- Time: O(n log n)
- Auxiliary Space: O(n) worst case
- Changes the original list.
Important concepts
- max(a) returns the largest element.
- a[0] accesses the first element.
- a[-1] accesses the last element.
- for n in a visits each element.
- res = n updates the largest value.
- sort() arranges elements in ascending order.
Interview recommendation
Practise the for-loop method first. Understand max() as the simplest built-in solution.
Practice questions
1. Find the smallest number in a list.
2. Find the second-largest number.
3. Find both the largest and smallest numbers.
4. Find the largest number without using max() or sort().
5. Find the largest number in a list containing duplicate values.
Note: Handle an empty list before finding the largest element.