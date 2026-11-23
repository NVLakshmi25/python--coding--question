Python Program to Check Whether a Number is Odd or Even
1. Problem Statement
Question: Given an integer, check whether it is an even number or an odd number.

Definition:
- Even number: A number that is exactly divisible by 2. The remainder is 0.
- Odd number: A number that is not exactly divisible by 2. The remainder is 1 (for positive integers).
Example:
- Input: 24 → Output: Even
- Input: 7 → Output: Odd
2. Recommended Method – Modulo Operator (%)
Recommended for interviews
 Beginner friendly


Definition: The modulo operator (%) returns the remainder after division.

Syntax:
if number % 2 == 0:    print("Even")else:    print("Odd")



Why do we use it?

We use the modulo operator because checking divisibility is simple and easy to understand.

Code:
x = 24if x % 2 == 0:    print("Even")else:    print("Odd")



Dry Run (Tracing):
Step	Operation	Result
1	x = 24	24
2	24 % 2	0
3	0 == 0	True
4	Execute if block	Even

Output:
Even


For x = 7:
Step	Operation	Result
1	x = 7	7
2	7 % 2	1
3	1 == 0	False
4	Execute else block	Odd

Output:
Odd


Time Complexity: O(1) – Only one modulo operation and one condition check.

Space Complexity: O(1) – We use only a fixed amount of extra memory.
3. Method 2 – Using Bitwise AND (&)
Definition: The bitwise AND (&) operator compares the binary bits of two numbers.

Why do we use it?

The last bit of an even number is always 0, and the last bit of an odd number is always 1.

Syntax:
if number & 1 == 0:    print("Even")else:    print("Odd")



Code:
x = 7if x & 1 == 0:    print("Even")else:    print("Odd")



Dry Run:

First, convert 7 into binary.
7 = 111
1 = 001
-------
    001


Bitwise AND operation:
111 & 001 = 001


001 represents 1.

Therefore, the condition is false, and the else block executes.

Output:
Odd


For an even number:
24 = 11000
 1 = 00001
-----------
     00000


Result is 0, so the number is even.

Time Complexity: O(1) – One bitwise operation and one condition check.

Space Complexity: O(1) – No additional data structures are required.
4. Method 3 – Using Lambda with Map()
Definition:
- Lambda: Creates a small anonymous function without using def.
- Map(): Applies a function to every element in an iterable and returns an iterator.
Why do we use it?

When we want to check multiple numbers in a list, we can use map() with lambda.

Syntax:
map(lambda number: expression, iterable)



Code:
a = [1, 2, 3, 4, 5]res = map(    lambda num: str(num) + " Even"    if num % 2 == 0    else str(num) + " Odd",    a)print("\n".join(res))



Dry Run:
Number	Remainder	Result
1	1	1 Odd
2	0	2 Even
3	1	3 Odd
4	0	4 Even
5	1	5 Odd

Output:
1 Odd
2 Even
3 Odd
4 Even
5 Odd


Time Complexity: O(n) – We process every element in the list once.

Space Complexity: O(1) auxiliary space – map() produces results lazily instead of creating another complete list. The output strings still require memory as they are generated.
5. Comparison of All Methods
Method	Time Complexity	Space Complexity	Best use
Modulo (%)	O(1)	O(1)	Single number
Bitwise (&)	O(1)	O(1)	Binary-level operation
Lambda + Map	O(n)	O(1)*	Multiple numbers

For the map iterator, excluding generated output and input storage.

My recommendation: Use the modulo (%) method in fresher interviews. It is simple, readable, and clearly explains your logic. You can learn bitwise AND as an alternative method. Use map() when you need to process a collection of numbers.

6. Interview Questions and Answers
Q1. What is an even number?

An even number is a number that is exactly divisible by 2, and its remainder is zero.

Q2. What is an odd number?

An odd number is a number that is not exactly divisible by 2, and its remainder is one for positive integers.

Q3. Why do we use the modulo operator?

We use the modulo operator to find the remainder after division.

Q4. What does 24 % 2 return?

It returns 0 because 24 is exactly divisible by 2.

Q5. What does 7 % 2 return?

It returns 1 because 7 is not exactly divisible by 2.

Q6. Can we check odd or even without using modulo?

Yes. We can use the bitwise AND (&) operator.

Q7. Which method is best for interviews?

I prefer the modulo operator because it is simple, readable, and easy to understand.

Q8. What is the time complexity?

For checking one number, the time complexity is O(1), because we perform a constant number of operations.

Q9. What is the difference between / and %?
- / returns the division result.
- % returns the remainder.
Example:
print(10 / 2)  # 5.0print(10 % 2)  # 0



7. Interviewee Explanation (Speak Naturally)
If the interviewer asks you to explain your code, you can say:
"First, I take an integer as input. Then I use the modulo operator to divide the number by 2. If the remainder is zero, I print Even. Otherwise, I print Odd. This solution takes constant time, O(1), and constant extra space, O(1)." Copy answer

8. Quick Summary – README Notes
Problem: Check whether a number is odd or even.

Recommended approach: Modulo operator (%).

Logic:
- number % 2 == 0 → Even
- number % 2 != 0 → Odd
Complexity:
- Time: O(1)
- Space: O(1)
Remember:
- % → Finds remainder.
- & → Performs bitwise AND.
- lambda → Creates an anonymous function.
- map() → Processes every element in an iterable.

9. Practice Questions
Try these yourself without looking at the solution.
Mini Interview Test
0/4 answered

1. What is the output of 15 % 2?

0

1

2




2. Which operator is used to find the remainder?

/

//

%




3. What is the time complexity for checking one number?

O(n)

O(1)

O(n²)




4. Which method is easiest for a fresher interview?

Modulo (%)

Lambda + map()

Bitwise AND



Check my answers
Final interview tip: Understand the modulo method first. Don't just memorize the code. Be able to explain why remainder 0 means even and remainder 1 means odd.