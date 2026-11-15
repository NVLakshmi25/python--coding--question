Prime Number – Interview Preparation Notes
1. Understand the problem
Question: What is a prime number?

A prime number is a number greater than 1 that has exactly two factors: 1 and itself.

Examples: 2, 3, 5, 7, 11

Question: What is the purpose of this program?

To check whether a given number is prime or not, or to generate all prime numbers within a range.

Question: Why do we use different methods?

To improve performance by reducing unnecessary divisor checks.
2. Method 1 – Basic approach
Logic: Check every number from 2 to n-1.
def is_prime(n):    if n <= 1:        return False    for i in range(2, n):        if n % i == 0:            return False    return True print(is_prime(7))



Output:
True


Dry run: n = 7
i	7 % i	Action
2	1	Continue
3	1	Continue
4	3	Continue
5	2	Continue
6	1	Continue

No divisor gives remainder zero. Therefore, True.

Syntax you should know:
- range(2, n) – generates numbers from 2 to n-1.
- n % i – calculates the remainder.
- return False – stops the function if a divisor is found.
- return True – confirms that no divisor was found.
Interview answer:

"I use a for loop to check all numbers from 2 to n-1. If any number divides n exactly, I return False. Otherwise, I return True."

Complexity:
- Time: O(n), because in the worst case we check nearly n divisors.
- Space: O(1), because we use only a few variables.
3. Method 2 – Square root approach
Question: Why do we use square root?

Because factors come in pairs. We only need to check up to the square root of the number.

Example:
36 = 2 × 18
36 = 3 × 12
36 = 4 × 9
36 = 6 × 6


After 6, the factor pairs repeat in reverse.
import mathdef is_prime(n):    if n <= 1:        return False    for i in range(2, math.isqrt(n) + 1):        if n % i == 0:            return False    return Trueprint(is_prime(29))



Output:
True


Dry run: n = 29
- math.isqrt(29) = 5.
- Loop checks 2, 3, 4, 5.
i	29 % i	Action
2	1	Continue
3	2	Continue
4	1	Continue
5	4	Continue

No divisor found. Result: True.

Syntax:

math.isqrt(n) returns the integer square root.

Example:
math.isqrt(36)  # 6math.isqrt(29)  # 5



Interview answer:

"Instead of checking every number, I check only up to the square root. This reduces unnecessary iterations because factors occur in pairs."

Complexity:
- Time: O(√n), because the loop checks only up to the square root.
- Space: O(1), because no extra list or collection is created.
4. Method 3 – Optimized odd-number approach
Question: Why do we skip even numbers?

Every even number except 2 is divisible by 2. Therefore, it cannot be prime.
import mathdef is_prime(n):    if n <= 1:        return False    if n % 2 == 0:        return n == 2    for i in range(3, math.isqrt(n) + 1, 2):        if n % i == 0:            return False    return Trueprint(is_prime(17))print(is_prime(21))



Output:
True
False


Dry run: n = 21
1. 21 <= 1 → False.
2. 21 % 2 == 0 → False.
3. Square root of 21 is approximately 4.58.
4. Check only odd divisors: 3.
i	21 % i	Action
3	0	Return False

Result: False.

Important syntax:
range(3, math.isqrt(n) + 1, 2)



- Start = 3.
- Stop = integer square root + 1.
- Step = 2.
It generates odd numbers: 3, 5, 7, 9...

Interview answer:

"First, I handle numbers less than or equal to 1. Then I handle even numbers separately. For odd numbers, I check only odd divisors up to the square root."

Complexity:
- Time: O(√n), because it checks approximately half the divisors of Method 2.
- Space: O(1), because it uses constant extra memory.
5. Method 4 – Sieve of Eratosthenes
Question: What is the purpose of Sieve?

To generate all prime numbers up to a given limit.

For example, n = 20:

Output:
[2, 3, 5, 7, 11, 13, 17, 19]


def sieve(n):    prime = [True] * (n + 1)    prime[0] = False    prime[1] = False    p = 2    while p * p <= n:        if prime[p]:            for i in range(p * p, n + 1, p):                prime[i] = False        p += 1    result = []    for i in range(2, n + 1):        if prime[i]:            result.append(i)    return resultprint(sieve(10))



Output:
[2, 3, 5, 7]


Dry run: n = 10

Initially all numbers are marked True, except 0 and 1.
Number	0	1	2	3	4	5	6	7	8	9	10
Initially	F	F	T	T	T	T	T	T	T	T	T
After 2	F	F	T	T	F	T	F	T	F	T	F
After 3	F	F	T	T	F	T	F	T	F	F	F

Remaining prime numbers: 2, 3, 5, 7.

Important syntax:
Syntax	Meaning
[True] * (n+1)	Creates a list filled with True
prime[0] = False	0 is not prime
prime[1] = False	1 is not prime
prime[i] = False	Marks a number as not prime
result.append(i)	Adds a prime number to the result

Why start from p * p?

Smaller multiples of p have already been marked by earlier numbers.

Interview answer:

"Sieve of Eratosthenes generates all prime numbers up to a given limit. I initially mark all numbers as prime and then mark the multiples of each prime number as not prime. The remaining numbers are prime."

Complexity:
- Time: O(n log log n), because we repeatedly mark multiples of prime numbers.
- Space: O(n), because we maintain a Boolean list of size n+1.

6. Final comparison
Method	Time	Space	Purpose
Basic	O(n)	O(1)	Learn the logic
Square root	O(√n)	O(1)	Check one number
Odd divisors	O(√n)	O(1)	Optimized single check
Sieve	O(n log log n)	O(n)	Generate many primes

7. Quick interview questions
Q1. Is 1 a prime number?

No. It has only one factor.

Q2. Is 2 a prime number?

Yes. It has exactly two factors: 1 and 2.

Q3. What is the difference between prime and composite?

A prime number has exactly two factors. A composite number has more than two factors.

Q4. What does % do?

It returns the remainder.

Q5. Why use return False inside the loop?

Because once a divisor is found, we know the number is not prime. There is no need to continue checking.

Q6. Which method is best?

For checking one number, Method 3 is a good choice. For generating many prime numbers, Sieve is better.

8. README.md – Revision notes
Prime Number in Python
Definition
A prime number is greater than 1 and has exactly two factors: 1 and itself.

Examples: 2, 3, 5, 7, 11.
Methods
1. Basic Method
- Checks divisors from 2 to n-1.
- Time: O(n)
- Space: O(1)
2. Square Root Method
- Checks divisors only up to √n.
- Time: O(√n)
- Space: O(1)
3. Optimized Method
- Handles even numbers separately.
- Checks only odd divisors.
- Time: O(√n)
- Space: O(1)
4. Sieve of Eratosthenes
- Generates all prime numbers up to n.
- Marks multiples as not prime.
- Time: O(n log log n)
- Space: O(n)
Important Python Syntax
- % : Modulus operator.
- range() : Generates a sequence of numbers.
- math.isqrt() : Returns integer square root.
- return False : Stops the function and returns False.
- append() : Adds an element to a list.
Interview Summary
For checking a single number, I prefer the optimized square-root approach. For generating all prime numbers up to a limit, I use the Sieve of Eratosthenes.
Practice
1. Check whether 13 is prime.
2. Check whether 25 is prime.
3. Print prime numbers from 1 to 50.
4. Count prime numbers from 1 to 100.
5. Explain why we check only up to the square root.