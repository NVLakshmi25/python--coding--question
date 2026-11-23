Python Interview Preparation: Find the Second Largest Number
Let's understand this problem from a recruiter's point of view, using simple English, Python syntax, examples, dry runs, and time and space complexity.

My recommendation: Learn the Single for Loop method first. It is a good choice for coding interviews because it demonstrates your logical thinking without using built-in sorting functions.
1. Understand the problem
Problem statement: Given a list of numbers, find the second largest distinct number in that list.

Example:
a = [10, 20, 4, 45, 99]



Output:
45


Why is the answer 45?
- Largest number = 99
- Second largest number = 45
- Remaining numbers = 10, 20, 4
The question is asking us to find the number that comes immediately after the largest number when the unique numbers are arranged in descending order.
Important interview condition
a = [10, 20, 99, 99, 45]



The second largest distinct number is 45, not 99.

We ignore duplicate values.
2. Basic interview questions
Question	Simple answer
What is a list?	A list stores multiple values in a single variable.
What is the largest number?	The highest number in a collection.
What is the second largest number?	The second highest distinct number.
Why do we need this program?	To find the next highest value without manually comparing numbers.
Where is it useful?	Ranking systems, student marks, employee salaries and data analysis.
When do we use it?	Whenever we need the second highest unique value from a collection.

3. Method 1: Using a Single For Loop (Recommended)
Best for coding interviews
Definition: We use two variables to track the largest and second largest numbers while checking each element only once.

Why use this method?
- No need to sort the entire list.
- Uses only one loop.
- Requires very little extra memory.
- Shows your problem-solving ability.
Syntax
if n > max1:    max2 = max1    max1 = nelif n > max2 and n != max1:    max2 = n



Complete program
a = [10, 20, 4, 45, 99]max1 = max2 = float('-inf')for n in a:    if n > max1:        max2 = max1        max1 = n    elif n > max2 and n != max1:        max2 = nprint(max2)



Output:
45


What is float('-inf')?
Definition: It represents negative infinity, a value smaller than any ordinary number.

Why do we use it?

We don't know the values in the list in advance. Initializing both variables with negative infinity ensures that even negative numbers can be handled correctly.
Dry run (step-by-step tracing)
Input:
a = [10, 20, 4, 45, 99]



Initially:
max1 = -infinitymax2 = -infinity



Iteration	Current n	max1	max2
1	10	10	-∞
2	20	20	10
3	4	20	10
4	45	45	20
5	99	99	45

Final answer: 45
How does the logic work?
1. If the current number is greater than max1, move the old max1 into max2.
2. Update max1 with the current number.
3. Otherwise, check whether the current number is greater than max2 but not equal to max1.
4. If true, update max2.
Complexity
- Time Complexity: O(n) — We visit each element only once.
- Space Complexity: O(1) — We use only two variables, regardless of list size.

4. Method 2: Using sorted() and set()
Definition: We remove duplicate numbers using set() and arrange the remaining numbers in descending order using sorted().

Why use this method?

It is easy to understand and write. It is suitable for beginners, but sorting takes more time.
Syntax
sorted(set(a), reverse=True)



Complete program
a = [10, 20, 4, 45, 99]unique_numbers = sorted(set(a), reverse=True)if len(unique_numbers) >= 2:    print(unique_numbers[1])else:    print(-1)



Output:
45


Dry run
Original list:
a = [10, 20, 4, 45, 99]



Step 1: Remove duplicates.
set(a)# {10, 20, 4, 45, 99}



Step 2: Sort in descending order.
[99, 45, 20, 10, 4]



Step 3: Access index 1.
unique_numbers[1]# 45



Remember:
- set() removes duplicate values.
- sorted() arranges values.
- reverse=True gives descending order.
- [1] accesses the second element.
Complexity
- Time: O(n log n) — Sorting takes O(n log n) time.
- Space: O(n) — We create a set and a sorted list containing up to n elements.
5. Method 3: Using heapq.nlargest()
Definition: Python's heapq module provides a function called nlargest() that returns the largest k elements.

Why use it?

It is useful when we need the top few largest elements from a large collection.
Syntax
heapq.nlargest(k, iterable)



- k = Number of largest elements required.
- iterable = List or another collection.
Complete program
import heapqa = [10, 20, 4, 45, 99]unique_numbers = set(a)result = heapq.nlargest(2, unique_numbers)if len(result) >= 2:    print(result[1])else:    print(-1)



Output:
45


Dry run
a = [10, 20, 4, 45, 99]



Step 1:
set(a)



Unique numbers:
{10, 20, 4, 45, 99}


Step 2:
heapq.nlargest(2, unique_numbers)



Result:
[99, 45]


Step 3:
result[1]



Output:
45


Important interview point: heapq.nlargest(2, a) without set() can return duplicate largest values. For example, [99, 99]. Remove duplicates first when the question asks for the second largest distinct number.
Complexity
- Time: O(n log k) — It finds the k largest elements using a heap. Here k = 2.
- Space: O(n) in this implementation because we create a set; the heap itself needs O(k) space.
6. Method 4: Using max() Twice
Definition: Find the largest number first, remove it from the unique values, and then find the next largest number.
Complete program
a = [10, 20, 4, 45, 99]unique_numbers = set(a)if len(unique_numbers) >= 2:    largest = max(unique_numbers)    unique_numbers.remove(largest)    second_largest = max(unique_numbers)    print(second_largest)else:    print(-1)



Output:
45


Dry run
unique_numbers = {10, 20, 4, 45, 99}



Step 1: Find the largest.
largest = max(unique_numbers)# 99



Step 2: Remove the largest.
unique_numbers.remove(99)



Remaining values:
{10, 20, 4, 45}


Step 3: Find the maximum again.
second_largest = max(unique_numbers)# 45



Complexity
- Time: O(n) — We scan the collection twice, which is still linear time.
- Space: O(n) — We create a set of unique values.
7. Comparison of all methods
Method	Time	Extra space	Best use
Single loop	O(n)	O(1)	Interviews
sorted(set())	O(n log n)	O(n)	Beginners
heapq.nlargest()	O(n log 2)	O(n) here	Top K elements
Double max()	O(n)	O(n)	Simple alternative

My recommendation:
Choose Method 1
Learn the single-loop approach first.

Why?
1. It takes only one traversal.
2. It does not sort the list.
3. It uses constant extra space.
4. It demonstrates your understanding of conditional statements and variable updates.
5. Interviewers can ask you to explain each iteration, which helps demonstrate your logic.
8. Interviewer and interviewee explanation
Interviewer: How would you find the second largest number in a list?

Interviewee:

"I would use a single for loop to solve this problem efficiently. First, I initialize two variables, max1 and max2, with negative infinity.

Then I iterate through the list. If the current number is greater than the largest number, I move the previous largest number into the second largest variable and update the largest number.

Otherwise, I check whether the current number is greater than the second largest number and different from the largest number.

Finally, I return the second largest number. This approach takes O(n) time and O(1) extra space."
Possible follow-up questions
Q1. Why do you use two variables?

To track the largest and second largest numbers separately.

Q2. Why do you use float('-inf')?

To handle negative numbers without assuming any minimum input value.

Q3. Why do you use n != max1?

To avoid considering duplicate largest values as the second largest.

Q4. What happens if the list contains only one unique number?

There is no second largest distinct number. We should return -1 or None, depending on the problem requirement.

Q5. Can you solve this without sorting?

Yes. We can use a single for loop and track the two largest values.

9. Important: Second largest number vs second largest digit in a string
These are two different interview questions.

Example 1: List of numbers
a = [10, 20, 45, 99]# Answer: 45



Example 2: Digits inside a string
s = "p84t3ho1n"# Digits: 8, 4, 3, 1# Answer: 4



For the string question, use isdigit() to identify digits and set() to remove duplicates.
s = "p84t3ho1n"digits = sorted({int(ch) for ch in s if ch.isdigit()}, reverse=True)if len(digits) >= 2:    print(digits[1])else:    print(-1)



Output:
4



10. README.md – Interview Notes
Here is a README document you can keep in your Python practice repository.
Find the Second Largest Number in a List – Python
1. Problem Statement
Given a list of numbers, find the second largest distinct number.

Example:
a = [10, 20, 4, 45, 99]
Output:
45
2. Recommended Approach – Single For Loop
We use two variables:
- max1: Stores the largest number.
- max2: Stores the second largest number.
Python Code
def second_largest(a):
    max1 = max2 = float('-inf')

    for n in a:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n

    if max2 == float('-inf'):
        return -1

    return max2


a = [10, 20, 4, 45, 99]
print(second_largest(a))
Output:
45
3. Dry Run
Input:
a = [10, 20, 4, 45, 99]
Current number	Largest	Second largest
10	10	-∞
20	20	10
4	20	10
45	45	20
99	99	45Final answer: 45
4. Other Approaches
Using Sorting
a = [10, 20, 4, 45, 99]

unique = sorted(set(a), reverse=True)

print(unique[1] if len(unique) >= 2 else -1)
Using heapq
import heapq

a = [10, 20, 4, 45, 99]

result = heapq.nlargest(2, set(a))

print(result[1] if len(result) >= 2 else -1)
Using max() Twice
a = [10, 20, 4, 45, 99]

unique = set(a)

if len(unique) >= 2:
    largest = max(unique)
    unique.remove(largest)
    print(max(unique))
else:
    print(-1)
5. Time and Space Complexity
Approach	Time Complexity	Space Complexity
Single loop	O(n)	O(1)
Sorting	O(n log n)	O(n)
heapq	O(n log 2)	O(n)
Double max	O(n)	O(n)Best interview approach: Single for loop.

Reason: It takes one traversal and uses constant extra space.
6. Important Interview Questions
1. Why do we use two variables?
2. What is the purpose of float('-inf')?
3. Why do we check n != max1?
4. What happens if duplicate numbers are present?
5. Can we solve this without sorting?
6. What is the time complexity?
7. What is the space complexity?
8. What happens if the list contains only one unique number?
7. Interview Explanation
"I use a single for loop to find the second largest distinct number. I maintain two variables to track the largest and second largest values. I compare each element and update these variables based on the conditions. This approach takes O(n) time and O(1) extra space."
8. Summary
- max1 stores the largest number.
- max2 stores the second largest number.
- A single loop checks every element.
- Duplicate largest values are ignored.
- We return -1 if there is no second largest distinct number.
Interview tip: Understand the logic and dry run instead of memorizing the code.




Your practice task: Try tracing this input yourself using the single-loop method:
a = [15, 15, 8, 25, 12, 25, 20]



Expected output: 20