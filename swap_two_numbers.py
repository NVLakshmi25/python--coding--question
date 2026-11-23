Python Program to Swap Two Numbers
Recommended for fresher interviews
 Beginner level

1. Problem statement
Question: Given two numbers a and b, swap their values.

Definition: Swapping means exchanging the values of two variables.

Example 1:
a = 10b = 20



Output:
a = 20
b = 10


Example 2:
a = 2b = 3



Output:
3 2


2. Why, purpose, how, where and when?
- Why? To understand variable assignment and value exchange.
- Purpose: Exchange the values stored in two variables.
- How? Store or exchange the original values without losing either one.
- Where? Sorting algorithms, rearranging data, and coding interviews.
- When? When a problem asks you to exchange two variables or swap array elements.
3. Method 1: Using a third variable
Best for beginners
Definition: A temporary variable stores one value while we exchange the other values.

Syntax:
temp = aa = bb = temp



Code:
a = 10b = 20temp = aa = bb = tempprint("a =", a)print("b =", b)



Output:
a = 20
b = 10


Dry run:
Step	a	b	temp
Initial	10	20	—
temp = a	10	20	10
a = b	20	20	10
b = temp	20	10	10

Explanation: First, save a in temp. Then assign b to a. Finally, assign the saved value to b.
4. Method 2: Without a third variable – Addition and subtraction
Definition: Use arithmetic operations to exchange values without creating a temporary variable.

Syntax:
a = a + bb = a - ba = a - b



Code:
a = 10b = 20a = a + bb = a - ba = a - bprint("a =", a)print("b =", b)



Output:
a = 20
b = 10


Dry run:
Step	a	b
Initial	10	20
a = a + b	30	20
b = a - b	30	10
a = a - b	20	10

Explanation: First, store the sum in a. Then use subtraction to recover the original values in the opposite variables.

Limitation: In fixed-size integer languages, addition can cause integer overflow. Python integers do not have this fixed-width overflow issue, but this approach is still less readable.
5. Method 3: Without a third variable – Bitwise XOR
Definition: XOR (^) is a bitwise operator. It can swap two integer values without using a temporary variable.

Syntax:
a = a ^ bb = a ^ ba = a ^ b



Code:
a = 10b = 20a = a ^ bb = a ^ ba = a ^ bprint("a =", a)print("b =", b)



Output:
a = 20
b = 10


Dry run:
Step	a	b
Initial	10	20
a = a ^ b	30	20
b = a ^ b	30	10
a = a ^ b	20	10

Here, the XOR calculations are:
- 10 ^ 20 = 30
- 30 ^ 20 = 10
- 30 ^ 10 = 20
Note: XOR works with integers, but it is less readable than Python's normal swapping syntax.
6. Method 4: Using Python tuple unpacking
Best for real-world Python code
Definition: Tuple unpacking allows us to exchange two variable values in one statement.

Syntax:
a, b = b, a



Code:
a = 10b = 20a, b = b, aprint("a =", a)print("b =", b)



Output:
a = 20
b = 10


Dry run:
Step	a	b
Initial	10	20
Right side values	20	10
Assignment completed	20	10

How does it work?

Python evaluates the right-hand side first, then assigns the values to the left-hand variables. So neither original value is lost.
7. Method 5: Multiplication and division
This is another mathematical approach, but it is not recommended.
a = 10b = 20a = a * bb = a // ba = a // bprint(a, b)



Output:
20 10


Limitation: It fails if either number is zero because division by zero is not allowed. It can also cause overflow in fixed-size integer languages.
8. Time and space complexity
Let the input contain two numbers.
Method	Time complexity	Auxiliary space
Third variable	O(1)	O(1)
Addition/subtraction	O(1)	O(1)
XOR	O(1)	O(1)
Tuple unpacking	O(1)	O(1)
Multiplication/division	O(1)	O(1)

Why?
- Time O(1): Every method performs a fixed number of operations, regardless of the input values.
- Space O(1): Only a fixed number of variables or temporary values are used.
9. Which method should you follow?
My recommendation:
1. For fresher interviews: Learn the third-variable method first because it clearly demonstrates variable assignment.
2. For Python coding interviews: Also learn tuple unpacking because it is the cleanest Python solution.
3. For problem-solving knowledge: Understand addition/subtraction and XOR as alternative techniques.
If the interviewer specifically says "without using a third variable", use tuple unpacking in Python unless they specifically require an arithmetic or XOR solution.
10. Interview questions and answers
Q1. What is swapping?

Swapping means exchanging the values of two variables.

Q2. Can we swap two numbers without a third variable?

Yes. We can use arithmetic operations, XOR, or Python tuple unpacking.

Q3. What is tuple unpacking?

It assigns multiple values to multiple variables in a single statement.

Q4. Why do we use a temporary variable?

To store the original value temporarily so that it is not lost during swapping.

Q5. Which method is best in Python?

Tuple unpacking: a, b = b, a.

Q6. What is the time complexity?

O(1), because swapping takes a fixed number of operations.
11. Interviewee explanation
If the interviewer asks you to explain your solution using a temporary variable:

"I initialize two variables, a and b, with values 10 and 20. First, I store the value of a in a temporary variable. Then I assign the value of b to a. Finally, I assign the temporary value to b. This exchanges the values of both variables. The time complexity is O(1), and the auxiliary space complexity is O(1)."

If asked to solve it using Python:

"I can also use tuple unpacking. By writing a, b = b, a, Python evaluates the right-hand values first and assigns them in the opposite order."
12. README.md – Interview revision notes
Swap Two Numbers in Python
Problem Statement
Given two numbers, exchange their values.

Input:
a = 10
b = 20
Output:
a = 20
b = 10
Method 1: Using a Third Variable
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)
Explanation: Store the first value in a temporary variable, assign the second value to the first, and then restore the saved value to the second.
Method 2: Addition and Subtraction
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)
Method 3: Bitwise XOR
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
Method 4: Python Tuple Unpacking
a = 10
b = 20

a, b = b, a

print(a, b)
Method 5: Multiplication and Division
a = 10
b = 20

a = a * b
b = a // b
a = a // b

print(a, b)
Note: This method fails if either number is zero.
Important Concepts
- Temporary variable: Stores a value temporarily.
- Arithmetic operators: +, -, *, //.
- Bitwise XOR: ^.
- Tuple unpacking: a, b = b, a.
Complexity
All five methods have:
- Time complexity: O(1)
- Auxiliary space complexity: O(1)
A fixed number of operations is performed regardless of the input values.
Interview Questions
1. What is swapping?
2. Why do we use a temporary variable?
3. How can we swap without a third variable?
4. What is tuple unpacking?
5. What is the difference between XOR and arithmetic swapping?
6. What is the time complexity?
Interview Recommendation
- Learn the temporary-variable method to understand the basic logic.
- Learn tuple unpacking for Python programming.
- Practice XOR and arithmetic swapping as alternative interview methods.




Practice question: Write a Python program to swap three variables: a = 10, b = 20, and c = 30, so the final values become a = 30, b = 10, and c = 20.