Python Program to Find the Sum of Digits of a Number
Best for fresher interviews
Beginner level

1. Problem Statement
Question: Given an integer, calculate the sum of all its digits.

Definition: The sum of digits means adding all individual digits of a number.

Example:
Input: 12345

Calculation:
1 + 2 + 3 + 4 + 5 = 15

Output: 15


Purpose: This problem helps us understand loops, digit extraction, and mathematical operators.
2. Method 1 – Using Modulo (%) and While Loop
Recommended method
Definition: Extract each digit from the number, add it to the total, and remove the extracted digit.

Why use this method?
- Easy to understand and explain.
- No string conversion is required.
- Uses O(1) auxiliary space.
- Demonstrates basic problem-solving skills.
Important syntax:
digit = n % 10total += digitn //= 10



Operator	Purpose	Example
% 10	Extract last digit	12345 → 5
// 10	Remove last digit	12345 → 1234
+=	Add to existing total	total = 5 + 4

Python Code:
n = 12345total = 0while n > 0:    digit = n % 10    total += digit    n //= 10print(total)



Dry Run:

Initial values:
n = 12345
total = 0


Iteration	n	digit = n % 10	total	n // 10
1	12345	5	5	1234
2	1234	4	9	123
3	123	3	12	12
4	12	2	14	1
5	1	1	15	0

When n = 0, the loop stops.

Output:
15


Complexity:
- Time: O(d) – We process each digit once.
- Auxiliary space: O(1) – We use a fixed number of variables.
Here, d means the number of digits.
3. Method 2 – Using Recursion
Definition: Recursion means a function calls itself until a stopping condition is reached.

Why use it? To understand how a problem can be divided into smaller operations.

Syntax:
def function(n):    if n == 0:        return 0    return (n % 10) + function(n // 10)



Code:
def digit_sum(n):    if n == 0:        return 0    return (n % 10) + digit_sum(n // 10)n = 12345print(digit_sum(n))



Dry Run:
digit_sum(12345)
= 5 + digit_sum(1234)
= 5 + 4 + digit_sum(123)
= 5 + 4 + 3 + digit_sum(12)
= 5 + 4 + 3 + 2 + digit_sum(1)
= 5 + 4 + 3 + 2 + 1 + digit_sum(0)
= 15


Output:
15


Complexity:
- Time: O(d) – One recursive call per digit.
- Space: O(d) – Recursive calls occupy stack memory.
4. Method 3 – Using map() and sum()
Definition:
- str() converts a number into a string.
- map() applies a function to each character.
- int() converts each character into an integer.
- sum() adds all the integers.
Why use it? It is a shorter Python solution without an explicit loop.

Syntax:
sum(map(int, str(n)))



Code:
n = 12345total = sum(map(int, str(n)))print(total)



Dry Run:

First:
str(12345) = "12345"


Next, map converts the characters:
1, 2, 3, 4, 5


Finally:
sum = 1 + 2 + 3 + 4 + 5
    = 15


Output:
15


Complexity:
- Time: O(d) – Every digit is processed once.
- Space: O(d) – The string representation requires memory.
5. Method 4 – Using reduce()
Definition: reduce() repeatedly applies an operation to combine multiple elements into one result.

It is available inside the functools module.

Why use it? It is useful for understanding functional programming and cumulative operations.

Syntax:
from functools import reducereduce(function, iterable, initial_value)



Code:
from functools import reducen = 12345total = reduce(    lambda x, y: x + int(y),    str(n),    0)print(total)



Dry Run:
Step	x	y	Result
1	0	'1'	1
2	1	'2'	3
3	3	'3'	6
4	6	'4'	10
5	10	'5'	15

Output:
15


Complexity:
- Time: O(d) – Processes every digit.
- Space: O(d) – Stores the string representation.
6. Comparison and Interview Recommendation
Method	Time	Auxiliary space	Recommendation
While + Modulo	O(d)	O(1)	Best
Recursion	O(d)	O(d)	Learn recursion
map() + sum()	O(d)	O(d)	Pythonic approach
reduce()	O(d)	O(d)	Advanced alternative

Which method should you choose in an interview?

I recommend While Loop + Modulo (%).

Why?
1. Easy to explain in simple English.
2. Shows knowledge of loops and operators.
3. Does not require string conversion.
4. Uses constant auxiliary space.
5. Easy to perform a dry run on a whiteboard.
7. Interview Questions and Answers
Q1. What is the sum of digits?

It means adding all the individual digits of a number.

Q2. Why do we use % 10?

To extract the last digit of a number.

Q3. Why do we use // 10?

To remove the last digit of a number.

Q4. Why do we initialize total = 0?

To store the sum of the extracted digits.

Q5. Why do we use a while loop?

To repeat the process until all digits are extracted.

Q6. Can we solve this without a while loop?

Yes, we can use recursion, map(), or reduce().

Q7. What is the difference between map() and reduce()?

map() processes each element separately, whereas reduce() combines elements into one result.

Q8. What is the time complexity?

O(d), because we process every digit once.

Q9. What is the auxiliary space complexity?

O(1) for the while-loop method because we use a fixed number of variables.

Q10. What happens if the input is zero?

The output is zero.
8. Interviewee Explanation
Practise saying this answer naturally:
"First, I initialize a variable called total to zero. Then I use a while loop to extract each digit using the modulo operator. I add each extracted digit to the total. After that, I remove the last digit using floor division by 10. I repeat this process until the number becomes zero. Finally, I print the total sum.

The time complexity is O(d), and the auxiliary space complexity is O(1), where d is the number of digits."
 Copy answer

9. README.md – Revision Notes
Save the following content as Sum_of_Digits_README.md.
Python – Sum of Digits
1. Problem Statement
Given an integer, calculate the sum of all its digits.

Example:
Input: 12345

Calculation:
1 + 2 + 3 + 4 + 5 = 15

Output: 15
2. Recommended Method
While Loop + Modulo (%)
3. Important Operators
Operator	Purpose
% 10	Extract last digit
// 10	Remove last digit
+=	Add value to total4. Python Code
n = 12345
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)
5. Output
15
6. Dry Run
n	Extracted digit	Total
12345	5	5
1234	4	9
123	3	12
12	2	14
1	1	157. Complexity
- Time Complexity: O(d)
- Auxiliary Space: O(1)
d = Number of digits.
8. Other Methods
1. Recursion
2. map() + sum()
3. reduce()
9. Interview Questions
1. Why do we use % 10?
2. Why do we use // 10?
3. Why initialize total = 0?
4. Why do we use a while loop?
5. Difference between map() and reduce()?
6. What is time complexity?
7. What is auxiliary space complexity?
10. Remember
- % 10 = Extract last digit.
- // 10 = Remove last digit.
- total += digit = Add digit to sum.




10. Practice Test
Mini Coding Interview Test
0/5 answered

1. What is the sum of digits of 456?

12

15

18




2. What is 12345 % 10?

1234

5

12345




3. What is 12345 // 10?

1234

5

12345




4. Which method uses O(1) auxiliary space?

Recursion

While + Modulo

reduce()




5. What is the time complexity?

O(1)

O(d)

O(d²)


Submit answers
One important interview tip: Don't memorize four methods immediately. First become confident with the while-loop approach and understand how % 10, // 10, and total += digit work. These same concepts will help you solve:
- Reverse a Number
- Palindrome Number
- Armstrong Number
- Count Digits in a Number
You can reuse this logic in many beginner-level Python coding interview questions.