Python Program to Find the GCD of Two Numbers
1. Problem statement
Given two integers, find the GCD (Greatest Common Divisor), also called HCF (Highest Common Factor).

The GCD is the largest positive number that divides both numbers without leaving a remainder.

Example:
a = 60b = 48


Factors of 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60

Factors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48

Common factors: 1, 2, 3, 4, 6, 12
Output: 12
2. Definition, purpose, and usage
- What: Find the largest number that divides two numbers exactly.
- Why: To find common divisors and simplify fractions.
- Purpose: To calculate the highest common factor efficiently.
- How: Check common divisors or use the Euclidean algorithm.
- Where: Mathematics, fraction simplification, and number-related programming problems.
- When: Whenever we need the greatest common factor of two integers.
3. Different methods
Method 1: Euclidean Algorithm using while loop
Best for coding interviews
Logic: Repeatedly calculate the remainder. Replace the first number with the second number and the second number with the remainder. Stop when the second number becomes zero.

Syntax:
while b != 0:    a, b = b, a % breturn a



Complete code:
def find_gcd(a, b):    while b != 0:        a, b = b, a % b    return aprint(find_gcd(60, 48))



Output:
12


Dry run:
Iteration	a	b	a % b
Initial	60	48	12
1	48	12	0
2	12	0	Stop

When b == 0, the loop stops and returns a, which is 12.

Why does it work?

The GCD of two numbers does not change when we replace the larger number with the remainder.

For example:
\[
GCD(60,48)=GCD(48,12)=12
\]

Complexity:
- Time: \(O(\log(\min(a,b)))\) — the remainder operations reduce the numbers quickly.
- Space: \(O(1)\) — only two variables are used.
Method 2: Built-in math.gcd()
Python provides a built-in function to calculate GCD.
import matha = 60b = 48print(math.gcd(a, b))



Output:
12


- Time: \(O(\log(\min(a,b)))\) for the Euclidean algorithm.
- Space: \(O(1)\) auxiliary space for this calculation.
- Best for: Real-world Python applications and quick solutions.
Method 3: Using a for loop
Logic: Check every number from 1 to the smaller input. Store the largest number that divides both numbers exactly.
def find_gcd(a, b):    smaller = min(a, b)    gcd = 1    for i in range(1, smaller + 1):        if a % i == 0 and b % i == 0:            gcd = i    return gcdprint(find_gcd(60, 48))



Output:
12


Dry run: The loop checks numbers from 1 to 48. When i = 12, both 60 % 12 and 48 % 12 are zero. No larger number divides both, so the answer is 12.
- Time: \(O(\min(a,b))\) — checks every number up to the smaller input.
- Space: \(O(1)\) — uses only a few variables.
Method 4: Using recursion
The function calls itself until the second number becomes zero.
def find_gcd(a, b):    if b == 0:        return a    return find_gcd(b, a % b)print(find_gcd(60, 48))



Output:
12


Dry run:
find_gcd(60, 48)
find_gcd(48, 12)
find_gcd(12, 0)
Returns 12


- Time: \(O(\log(\min(a,b)))\) — same remainder reduction as the iterative method.
- Space: \(O(\log(\min(a,b)))\) — recursive calls use the call stack.
Method 5: Repeated subtraction
Logic: Subtract the smaller number from the larger number until both numbers become equal.
def find_gcd(a, b):    while a != b:        if a > b:            a -= b        else:            b -= a    return aprint(find_gcd(60, 48))



Output:
12


- Time: Can take \(O(\max(a,b))\) iterations in the worst case.
- Space: \(O(1)\) — uses only two variables.
- Limitation: Can be slow for large numbers.
Note: These examples assume positive integers. For general Python inputs, math.gcd() also handles zero and negative integers. The manual methods above should be adapted using abs() and a zero-input check if those cases are required.
4. Which method should you follow for interviews?
Method	Time	Space	Recommendation
Euclidean while loop	\(O(\log n)\)	\(O(1)\)	Best choice
math.gcd()	\(O(\log n)\)	\(O(1)\) auxiliary	Best for real projects
for loop	\(O(n)\)	\(O(1)\)	Beginner-friendly
Recursion	\(O(\log n)\)	\(O(\log n)\)	Good to understand recursion
Subtraction	\(O(n)\) worst case	\(O(1)\)	Less efficient

My recommendation: Learn and explain the Euclidean algorithm using a while loop.

Why recruiters may prefer this approach:
- Shows your problem-solving skills.
- Demonstrates your understanding of loops and modulo %.
- Does not depend on a built-in GCD function.
- Efficient for large numbers.
- Uses constant extra space.
5. Interview questions and answers
Q1. What is GCD?

GCD is the largest positive integer that divides two numbers without leaving a remainder.

Q2. What is the difference between GCD and HCF?

There is no difference. Both mean the same thing.

Q3. What is the Euclidean algorithm?

It is an efficient method that repeatedly calculates remainders until the remainder becomes zero.

Q4. Why do we use the modulo % operator?

It returns the remainder after division. We use that remainder to reduce the numbers in each iteration.

Q5. Why is the time complexity \(O(\log n)\)?

Because the numbers become smaller quickly after each remainder operation. The number of iterations grows logarithmically with the input size.

Q6. What happens when one number is zero?

The GCD of a and 0 is abs(a). Python's math.gcd(60, 0) returns 60.

Q7. Which method is better: recursion or iteration?

Both use the Euclidean algorithm. Iteration is generally preferable because it avoids recursive call-stack memory.
6. Interviewee explanation
You can explain it like this:
To find the GCD of two numbers, I use the Euclidean algorithm.

First, I take two numbers, 60 and 48. Then I calculate the remainder using the modulo operator.

I update the first number with the second number and the second number with the remainder.

I repeat this process until the second number becomes zero.

Finally, the first number is the GCD, which is 12.

The time complexity is O(log n), and the space complexity is O(1).

7. README.md revision notes
Python Program to Find GCD of Two Numbers
1. Definition
GCD (Greatest Common Divisor), also called HCF, is the largest positive integer that divides two numbers without leaving a remainder.

Example: GCD of 60 and 48 = 12.
2. Recommended Method: Euclidean Algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(find_gcd(60, 48))
Output:
12
3. Dry Run
a	b	Remainder
60	48	12
48	12	0
12	0	StopWhen b == 0, return a.
4. Other Methods
1. math.gcd(a, b) – built-in method.
2. Euclidean algorithm using recursion.
3. Checking divisors using a for loop.
4. Repeated subtraction using a while loop.
5. Complexity
Method	Time	Space
Euclidean while	O(log n)	O(1)
math.gcd()	O(log n)	O(1) auxiliary
For loop	O(n)	O(1)
Recursion	O(log n)	O(log n)
Subtraction	O(n) worst case	O(1)Here, n represents the smaller input for the GCD methods.
6. Important Concepts
- % – returns the remainder.
- while – repeats until the condition becomes false.
- a, b = b, a % b – updates both variables.
- return – sends the final GCD back.
7. Interview Tip
Prefer the Euclidean algorithm using a while loop. It is efficient and demonstrates problem-solving skills.
8. Practice
1. Find GCD of 54 and 24.
2. Find GCD of 100 and 75.
3. Find GCD of 17 and 19.
4. Find GCD of 0 and 25.
5. Write the same logic using recursion.


Remember: For interviews, understand the Euclidean algorithm rather than memorizing the code. Be ready to explain why a, b = b, a % b works.