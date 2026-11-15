Prime Number in Python – Different Methods
Let's understand this problem in simple English, with dry runs, outputs, interview answers, and time and space complexity.
1. Definition: What is a prime number?
A prime number is a number greater than 1 that has exactly two factors:
- 1
- The number itself
Examples: 2, 3, 5, 7, 11, 13

A composite number has more than two factors.

Examples: 4, 6, 8, 9, 10

Important: 0 and 1 are neither prime nor composite.
Number	Factors	Result
2	1, 2	Prime
3	1, 3	Prime
4	1, 2, 4	Composite
5	1, 5	Prime
9	1, 3, 9	Composite

2. Why do we need different methods?
Suppose the interviewer asks:

"How do you check whether a number is prime?"

We can solve it using different approaches.
- Method 1: Check every number from 2 to n-1.
- Method 2: Check only up to the square root of n.
- Method 3: Check only odd divisors after handling 2.
- Method 4: Use the Sieve of Eratosthenes to generate many prime numbers.
The main purpose of optimization is to reduce unnecessary checks and save execution time.

Method 1: Check all numbers from 2 to n-1
Idea: Check whether any number between 2 and n-1 divides the given number.
def is_prime(n):    if n <= 1:        return False    for i in range(2, n):        if n % i == 0:            return False    return Trueprint(is_prime(7))print(is_prime(8))



Output:
True
False


Dry run: n = 7
i	7 % i	Result
2	1	Continue
3	1	Continue
4	3	Continue
5	2	Continue
6	1	Continue

No number divides 7 exactly, so it returns True.

For n = 8, when i = 2, 8 % 2 == 0. So it returns False immediately.

Interview explanation:

"I check every number from 2 to n-1. If any number divides the given number exactly, it is not prime. Otherwise, it is prime."

Complexity:
- Time: O(n) — in the worst case, we check almost n numbers.
- Space: O(1) — we use only a few variables.

Method 2: Check up to the square root
Idea: We don't need to check all numbers. We only need to check divisors up to the square root of n.

Why?

Consider 36:
36 = 1 × 36
36 = 2 × 18
36 = 3 × 12
36 = 4 × 9
36 = 6 × 6
36 = 9 × 4
36 = 12 × 3
36 = 18 × 2
36 = 36 × 1


Notice that after 6 × 6, the factor pairs repeat in reverse order.

Therefore, if a number has a divisor greater than its square root, it must also have a corresponding divisor smaller than its square root.

So, checking up to √n is sufficient.
import mathdef is_prime(n):    if n <= 1:        return False    max_div = math.isqrt(n)    for i in range(2, max_div + 1):        if n % i == 0:            return False    return Trueprint(is_prime(29))print(is_prime(36))



Output:
True
False


math.isqrt(n) returns the integer square root. For example, math.isqrt(36) is 6.

Dry run: n = 36
- Square root of 36 = 6.
- Check divisors from 2 to 6.
i	36 % i	Result
2	0	Divisible

The function immediately returns False.

For n = 29, we check 2, 3, 4, 5. None divides 29 exactly, so the result is True.

Interview explanation:

"Instead of checking all numbers up to n-1, I check only up to the square root of n. This works because factors occur in pairs. It reduces the number of checks."

Complexity:
- Time: O(√n) — we check at most approximately √n divisors.
- Space: O(1) — no additional collection is created.

Method 3: Check only odd divisors
Idea: Every even number except 2 is not prime.

For example:
- 4 is divisible by 2.
- 6 is divisible by 2.
- 8 is divisible by 2.
- 10 is divisible by 2.
So, first handle 2 and remove all other even numbers. Then check only odd divisors.
import mathdef is_prime(n):    if n <= 1:        return False    if n % 2 == 0:        return n == 2    for i in range(3, math.isqrt(n) + 1, 2):        if n % i == 0:            return False    return Trueprint(is_prime(2))print(is_prime(17))print(is_prime(21))



Output:
True
True
False


Dry run: n = 21
1. 21 <= 1? No.
2. 21 % 2 == 0? No.
3. Square root of 21 is approximately 4.58.
4. Check odd divisors: 3.
i	21 % i	Result
3	0	Divisible

So, the function returns False.

What does range(3, math.isqrt(n) + 1, 2) mean?
- 3: Start from 3.
- math.isqrt(n) + 1: Stop after the square-root limit.
- 2: Increase by 2, so we check only odd numbers: 3, 5, 7, 9...
Interview explanation:

"First, I handle numbers less than or equal to 1. Then I check whether the number is even. If it is even, only 2 is prime. For odd numbers, I check only odd divisors up to the square root."

Complexity:
- Time: O(√n) — we check fewer divisors than Method 2, approximately half.
- Space: O(1) — we use only a few variables.

Method 4: Sieve of Eratosthenes
Idea: The previous methods check one number at a time. The Sieve method generates all prime numbers up to a given limit.

For example, if n = 20, the answer is:

2, 3, 5, 7, 11, 13, 17, 19

How does it work?
1. Initially, assume every number is prime.
2. Start from 2.
3. Mark all multiples of 2 as not prime.
4. Move to the next unmarked number, 3.
5. Mark all multiples of 3 as not prime.
6. Continue until the square root of n.
7. The remaining unmarked numbers are prime.
def sieve(n):    prime = [True] * (n + 1)    prime[0] = False    prime[1] = False    p = 2    while p * p <= n:        if prime[p]:            for i in range(p * p, n + 1, p):                prime[i] = False        p += 1    result = []    for i in range(2, n + 1):        if prime[i]:            result.append(i)    return resultprint(sieve(20))



Output:
[2, 3, 5, 7, 11, 13, 17, 19]


Dry run: n = 10

Initially:
Numbers:  0  1  2  3  4  5  6  7  8  9  10
Prime?:   F  F  T  T  T  T  T  T  T  T  T


- Start with 2. Mark its multiples: 4, 6, 8, 10.
- Move to 3. Mark its multiples: 6, 9.
- Stop when p * p > n.
Remaining prime numbers:
2, 3, 5, 7


Important syntax:
- [True] * (n + 1) creates a list of n + 1 True values.
- prime[i] = False marks a number as not prime.
- range(p * p, n + 1, p) visits multiples of p, starting at p squared.
- while p * p <= n ensures we only process possible prime divisors up to √n.
Why start marking from p * p?

For example, when p = 5, we don't need to mark 10, 15, or 20 again. They have already been marked as multiples of 2 or 3. So we start at 5 * 5 = 25.

Interview explanation:

"The Sieve of Eratosthenes is used to generate all prime numbers up to a given limit. Initially, we mark all numbers as prime. Then we repeatedly mark the multiples of each prime number as not prime. The remaining numbers are prime."

Complexity:
- Time: O(n log log n) — marking multiples across all prime numbers takes approximately this much work.
- Space: O(n) — we store a Boolean list of size n + 1.

5. Comparison of all methods
Method	Time complexity	Space complexity	Best use
Method 1	O(n)	O(1)	Basic learning
Method 2	O(√n)	O(1)	Check one number
Method 3	O(√n)	O(1)	Optimized single-number check
Sieve	O(n log log n)	O(n)	Generate many primes

Which method should I use?
- Checking one number? Use Method 3.
- Generating all primes up to a limit? Use Sieve.
- Learning the basic logic? Start with Method 1.
One important point about the article: Its Sieve example uses range(2, n), which excludes n itself. If the requirement is to include all primes less than or equal to n, use range(2, n + 1), as in the corrected code above. Also, the article's timings are just example measurements; actual execution time depends on the computer and Python environment.
6. Common interview questions and answers
Q1. What is a prime number?

A prime number is a number greater than 1 that is divisible only by 1 and itself.

Q2. Why is 1 not a prime number?

Because 1 has only one factor, but a prime number must have exactly two factors.

Q3. Why do we check up to the square root?

Because factors occur in pairs. If a divisor exists above the square root, its matching divisor exists below it.

Q4. Why do we skip even numbers in Method 3?

Because every even number except 2 is divisible by 2, so it cannot be prime.

Q5. What is the difference between Method 3 and Sieve?

Method 3 checks whether one particular number is prime. Sieve generates all prime numbers up to a given limit.

Q6. What does % mean in Python?

It is the modulus operator. It returns the remainder.

Example: 10 % 2 = 0, meaning 10 is exactly divisible by 2.

Q7. What does return False do?

It immediately stops the function and returns False.
7. README.md – Prime Number in Python
Prime Number in Python
Definition
A prime number is a number greater than 1 that has exactly two factors: 1 and itself.

Examples: 2, 3, 5, 7, 11.

1 is neither prime nor composite.
Different Methods
Method 1: Basic Approach
- Check all divisors from 2 to n-1.
- Easy to understand.
- Time: O(n)
- Space: O(1)
Method 2: Square Root Approach
- Check divisors only up to √n.
- Reduces unnecessary checks.
- Time: O(√n)
- Space: O(1)
Method 3: Optimized Approach
- Handle even numbers separately.
- Check only odd divisors up to √n.
- Time: O(√n)
- Space: O(1)
Method 4: Sieve of Eratosthenes
- Generates all prime numbers up to n.
- Marks multiples of prime numbers as not prime.
- Time: O(n log log n)
- Space: O(n)
Important Python Concepts
- % : Returns the remainder.
- range(start, stop, step) : Generates numbers in a sequence.
- math.isqrt(n) : Returns the integer square root.
- return False : Stops the function and returns False.
- prime[i] = False : Marks a number as not prime.
Interview Summary
For checking a single number, the optimized square-root approach is useful. For generating all prime numbers within a range, the Sieve of Eratosthenes is more efficient.
Practice Questions
1. Check whether 13 is prime.
2. Check whether 25 is prime.
3. Print all prime numbers from 1 to 50.
4. Count the prime numbers from 1 to 100.
5. Explain why 1 is not prime.




8. Practice – Test your understanding
1. Which number is neither prime nor composite?

0

1

2

3




2. What is the time complexity of checking divisors up to the square root?

O(n)

O(√n)

O(n²)

O(1)




3. Which method is best for generating all primes up to 1000?

Basic approach

String method

Sieve of Eratosthenes