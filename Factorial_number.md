Factorial of a Number in Python – Different Methods
Let's understand factorial using simple English, Python code, dry runs, outputs, interview answers, and time and space complexity.
1. Definition: What is factorial?
The factorial of a number is the product (multiplication) of all positive integers from 1 up to that number.

It is represented by the symbol !.

Example:
\[
6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720
\]

Some important factorials:
Number	Calculation	Answer
0!	1	1
1!	1	1
2!	2 × 1	2
3!	3 × 2 × 1	6
4!	4 × 3 × 2 × 1	24
5!	5 × 4 × 3 × 2 × 1	120
6!	6 × 5 × 4 × 3 × 2 × 1	720

Important: Factorial is defined for non-negative integers. Negative numbers do not have a factorial in this context.
2. Why do we calculate factorial?
Question: What is the purpose of factorial?

Factorial is used in:
- Mathematics
- Permutations and combinations
- Probability
- Counting different arrangements
Example: If you have 3 different books, the number of ways to arrange them is:
\[
3! = 3 \times 2 \times 1 = 6
\]


Method 1: Using Python's built-in math.factorial()
Idea: Python already provides a function to calculate factorial. We don't need to write a loop or recursion ourselves.
import mathn = 6print(math.factorial(n))



Output:
720


Dry run:
math.factorial(6)



Python internally calculates:
6 × 5 × 4 × 3 × 2 × 1
= 720


Important syntax:
- import math – imports Python's math module.
- math.factorial(n) – calculates the factorial of n.
Interview explanation:

"I use Python's built-in math.factorial() function. It directly calculates the factorial of a non-negative integer without writing a loop or recursive function."

Complexity:
- Time: Roughly O(n) multiplication steps at a high level. The actual implementation is optimized.
- Space: Depends on the internal implementation and the size of the result.
When should we use it?

When we need a quick, reliable factorial calculation without implementing the logic ourselves.

Method 2: Using NumPy's np.prod()
Idea: NumPy provides prod(), which multiplies all the elements in a sequence.
import numpy as npn = 6if n >= 0:    print(np.prod(range(1, n + 1)))else:    print("Factorial is not defined for negative numbers")



Output:
720


Dry run:
range(1, 6 + 1)



This generates:
1, 2, 3, 4, 5, 6


Then:
np.prod([1, 2, 3, 4, 5, 6])



Calculation:
1 × 2 × 3 × 4 × 5 × 6 = 720


Important syntax:
- import numpy as np – imports NumPy using the alias np.
- np.prod() – multiplies all elements.
- range(1, n + 1) – generates numbers from 1 to n.
Interview explanation:

"NumPy's prod() function multiplies all the values in a sequence. I generate numbers from 1 to n and pass them to prod() to calculate factorial."

Complexity:
- Time: O(n) – it processes n values.
- Space: O(n) – NumPy generally needs an array containing the values.
When should we use it?

When we are already working with NumPy arrays or numerical data.

Note: NumPy's default integer type can overflow for large factorials. Python's math.factorial() and normal Python integer multiplication support arbitrarily large integers.

Method 3: Using a for loop
Idea: Start with f = 1 and multiply it by every number from 1 to n.
n = 6if n < 0:    print("Factorial is not defined for negative numbers")else:    f = 1    for i in range(1, n + 1):        f *= i    print(f)



Output:
720


Dry run: n = 6

Initially:
f = 1



Now the loop executes:
Iteration	i	Calculation	f
1	1	1 × 1	1
2	2	1 × 2	2
3	3	2 × 3	6
4	4	6 × 4	24
5	5	24 × 5	120
6	6	120 × 6	720

Final answer: 720.

Important syntax:
- f = 1 – initializes the result.
- range(1, n + 1) – generates numbers from 1 to n.
- f *= i – shorthand for f = f * i.
- print(f) – displays the result.
Question: Why do we initialize f with 1 instead of 0?

Because 1 is the multiplication identity.

If we initialize with 0, every multiplication gives 0.

For example:
0 × 1 × 2 × 3 = 0


That is why we start with 1.

Interview explanation:

"I initialize a variable f with 1. Then I use a for loop from 1 to n and multiply each number with f. After the loop finishes, I print the final factorial."

Complexity:
- Time: O(n) – the loop executes n times.
- Space: O(1) auxiliary space – we use only a fixed number of variables. The result itself grows as the factorial gets larger.
When should we use it?

When an interviewer asks you to calculate factorial using iteration or loops.

Method 4: Using recursion
Idea: A function calls itself with a smaller number until it reaches a stopping condition.

Mathematical formula:
\[
n! = n \times (n-1)!
\]

Base case:
\[
0! = 1,\quad 1! = 1
\]

def fact(n):    if n < 0:        return "Factorial is not defined for negative numbers"    if n <= 1:        return 1    return n * fact(n - 1)print(fact(6))print(fact(-3))



Output:
720
Factorial is not defined for negative numbers


Dry run: n = 6

The function calls itself:
fact(6)
= 6 × fact(5)
= 6 × 5 × fact(4)
= 6 × 5 × 4 × fact(3)
= 6 × 5 × 4 × 3 × fact(2)
= 6 × 5 × 4 × 3 × 2 × fact(1)


Now the base case is reached:
fact(1) = 1



The function returns back:
6 × 5 × 4 × 3 × 2 × 1
= 720


Visualize the recursion
fact(6)


6 × fact(5)


5 × fact(4)


...


fact(1) = 1 — Base case

Then the results return back up the calls.
Important syntax:
- def fact(n) – defines a function.
- fact(n - 1) – calls the same function with a smaller value.
- if n <= 1 – base case that stops recursion.
- return n * fact(n - 1) – multiplies n by the result of the next function call.
Question: Why do we need a base case?

Without a base case, the function keeps calling itself and eventually causes a recursion error.

Interview explanation:

"I use recursion by multiplying n with the factorial of n-1. The function keeps calling itself until n becomes 1 or 0. This is called the base case. Then the results return back and produce the factorial."

Complexity:
- Time: O(n) – the function makes n recursive calls.
- Space: O(n) – each call occupies space on the recursion call stack.
When should we use it?

When the interviewer asks you to solve the problem using recursion or wants to test your understanding of base cases and recursive calls.

5. Comparison of all methods
Method	Time	Space	Best use
math.factorial()	Optimized internally	Implementation-dependent	Direct calculation
NumPy prod()	O(n)	O(n)	NumPy numerical work
For loop	O(n)	O(1) auxiliary	Interview iteration
Recursion	O(n)	O(n) call stack	Learning recursion

6. Common interview questions
Q1. What is factorial?

Factorial is the product of all positive integers from 1 to a given non-negative integer.

Q2. What is 0 factorial?

0! = 1. It is defined as 1 mathematically.

Q3. Why do we initialize f with 1?

Because 1 is the multiplication identity. Multiplying by 1 does not change the result.

Q4. What is recursion?

Recursion is a technique where a function calls itself to solve a smaller problem.

Q5. What is a base case?

A base case is the stopping condition that prevents infinite recursive calls.

Q6. What is the difference between a loop and recursion?

A loop repeats statements using iteration. Recursion repeats the process through function calls.

Q7. Which method is better for interviews?

The for-loop approach is a good starting point because it is simple and demonstrates your logic. You should also understand recursion.

Q8. What happens if n is negative?

Factorial is not defined for negative integers, so we should handle that case.

7. README.md – Factorial in Python
Factorial of a Number in Python
1. Definition
Factorial is the product of all positive integers from 1 to n.

Example:

6! = 6 × 5 × 4 × 3 × 2 × 1 = 720

Important:
- 0! = 1
- 1! = 1
- Negative factorials are not defined for integers.
2. Different Methods
Method 1: math.factorial()
- Uses Python's built-in function.
- Time: Optimized internally.
- Best for direct factorial calculation.
Method 2: NumPy prod()
- Multiplies all values in a sequence.
- Time: O(n)
- Space: O(n)
- Useful when working with NumPy numerical data.
- Note: Default NumPy integer types can overflow for large factorials.
Method 3: For Loop
- Initializes the result with 1.
- Multiplies every number from 1 to n.
- Time: O(n)
- Auxiliary space: O(1)
- Useful for interview coding.
Method 4: Recursion
- A function calls itself with n-1.
- Stops at the base case.
- Time: O(n)
- Space: O(n) because of recursive calls.
- Useful for understanding recursion.
3. Important Python Syntax
- import math: Imports the math module.
- math.factorial(n): Calculates factorial.
- import numpy as np: Imports NumPy.
- np.prod(): Multiplies sequence values.
- range(1, n+1): Generates numbers from 1 to n.
- f *= i: Multiplies f by i.
- return: Sends a result back from a function.
- fact(n-1): Calls the same function with a smaller number.
4. Interview Summary
Factorial is calculated by multiplying all integers from 1 to n.

We can calculate factorial using a built-in function, NumPy, a for loop, or recursion.

The for-loop approach is simple and uses constant auxiliary space. Recursion uses additional call-stack space.
5. Practice Questions
1. Find the factorial of 4.
2. Find the factorial of 0.
3. Find the factorial of 7.
4. Write factorial using a for loop.
5. Write factorial using recursion.
6. Explain why we initialize the result with 1.
7. Explain the base case in recursion.




8. Test your understanding
1. What is the factorial of 5?

25

60

120

720




2. Why do we initialize f = 1?

Because 1 is the multiplication identity

Because 1 is the largest number

Because loops start at 1




3. What is the base case in factorial recursion?

n == 10

n <= 1

n > 1




4. What is the auxiliary space complexity of recursive factorial?

O(1)

O(n)

O(n²)