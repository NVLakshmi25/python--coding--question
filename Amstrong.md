Python Program to Check Armstrong Number
Recommended for fresher interviews
 Beginner level

1. Problem Statement
Question: Given a number n, check whether it is an Armstrong number or not.

Definition:

An Armstrong number is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.

Example:

Input: 153

153 contains 3 digits.
\[
1^3 + 5^3 + 3^3
\]

\[
1 + 125 + 27 = 153
\]

Therefore, 153 is an Armstrong number.

Other examples:
Number	Calculation	Result
153	1³ + 5³ + 3³ = 153	Armstrong
370	3³ + 7³ + 0³ = 370	Armstrong
371	3³ + 7³ + 1³ = 371	Armstrong
123	1³ + 2³ + 3³ = 36	Not Armstrong
9474	9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474	Armstrong

Important: The power depends on the total number of digits, not always 3.
2. Method 1 – Mathematical Approach (Using while Loop)
Best method to follow in interviews
Definition: We extract each digit using the modulo operator, calculate its power, add the results, and compare the final sum with the original number.

Why do we use this method?
- It helps us understand mathematical operations.
- It does not require converting every digit into a string.
- It demonstrates problem-solving skills using loops.
Syntax:
digit = number % 10number = number // 10



- % 10 → Extracts the last digit.
- // 10 → Removes the last digit.
- ** power → Calculates the power.
Code:
n = 153t = np = len(str(n))s = 0while t > 0:    d = t % 10    s += d ** p    t //= 10if s == n:    print("Armstrong Number")else:    print("Not an Armstrong Number")



Dry Run (Tracing) – n = 153

Initial values:
n = 153t = 153p = 3s = 0



Because 153 has 3 digits, p = 3.

Now execute the while loop.
Iteration	t	d = t % 10	d ** p	s	t // 10
1	153	3	27	27	15
2	15	5	125	152	1
3	1	1	1	153	0

When t = 0, the while loop stops.

Now compare:
if s == n:    # 153 == 153 → True



Output:
Armstrong Number


Time Complexity: O(d), because we process each digit exactly once. Here, d represents the number of digits.

Space Complexity: O(d) for this exact implementation because str(n) creates a string containing all digits. The while-loop logic itself uses O(1) extra space.
3. Method 2 – Using String Conversion and sum()
Definition: Convert the number into a string, access each digit, calculate its power, and add all the results using sum().

Why do we use it?

It is shorter and easier to read because Python provides built-in functions.

Syntax:
sum(int(digit) ** power for digit in str(number))



Code:
n = 153p = len(str(n))s = sum(int(d) ** p for d in str(n))if s == n:    print("Armstrong Number")else:    print("Not an Armstrong Number")



Dry Run:
n = 153
p = 3

Digits: 1, 5, 3

1 ** 3 = 1
5 ** 3 = 125
3 ** 3 = 27

sum = 1 + 125 + 27
    = 153


Compare 153 == 153.

Output:
Armstrong Number


Time Complexity: O(d), because we visit every digit once.

Space Complexity: O(d), because the string representation stores all digits.
4. Method 3 – Using map() and lambda
Definition:
- map() applies a function to every digit.
- lambda creates a small anonymous function.
- sum() adds all the calculated values.
Why do we use it?

It provides a compact way to process every digit without writing an explicit loop.

Syntax:
sum(map(lambda d: int(d) ** p, str(n)))



Code:
n = 153p = len(str(n))s = sum(map(lambda d: int(d) ** p, str(n)))if s == n:    print("Armstrong Number")else:    print("Not an Armstrong Number")



Dry Run:
Digit	Lambda calculation	Result
1	1 ** 3	1
5	5 ** 3	125
3	3 ** 3	27

sum = 1 + 125 + 27
    = 153


Output:
Armstrong Number


Time Complexity: O(d), because map processes each digit once.

Space Complexity: O(d), mainly because of the string representation. map() itself produces an iterator rather than a complete result list.
5. Method 4 – Using Recursion
Definition: Recursion means a function calls itself repeatedly until a stopping condition is reached.

Why do we use it?

It helps us solve a problem by breaking it into smaller operations, one digit at a time.

Syntax:
def function(number):    if stopping_condition:        return result    return current_result + function(smaller_number)



Code:
n = 153p = len(str(n))def arm(x):    if x == 0:        return 0    return (x % 10) ** p + arm(x // 10)if arm(n) == n:    print("Armstrong Number")else:    print("Not an Armstrong Number")



Dry Run:

The function extracts the last digit and calls itself with the remaining number.
arm(153)
= 3³ + arm(15)
= 27 + 5³ + arm(1)
= 27 + 125 + 1³ + arm(0)
= 27 + 125 + 1 + 0
= 153


Compare 153 == 153.

Output:
Armstrong Number


Time Complexity: O(d), because the function processes each digit once.

Space Complexity: O(d), because each recursive call occupies stack memory.

6. Comparison of All Methods
Method	Time	Space	Best use
Mathematical (while)	O(d)	O(d)*	Interviews
String + sum()	O(d)	O(d)	Simple Python code
map() + lambda	O(d)	O(d)	Functional programming
Recursion	O(d)	O(d)	Understanding recursion

d = number of digits. The mathematical method uses O(1) auxiliary space for its loop, but the exact code uses str(n) to calculate the digit count, which takes O(d) space.

My recommendation: Follow Method 1 (Mathematical Approach) for fresher interviews.

Why?
1. It demonstrates your understanding of %, //, and **.
2. It shows your ability to use a while loop.
3. You can explain the logic step by step.
4. Interviewers can easily understand your approach.
Learn Method 2 as an alternative Pythonic solution.

7. Interview Questions and Answers
Q1. What is an Armstrong number?

An Armstrong number is a number equal to the sum of its digits raised to the power of the total number of digits.

Q2. Why do we use len(str(n))?

We use it to find the total number of digits in a number.

Q3. What is the purpose of % 10?

It extracts the last digit of a number.

Example: 153 % 10 = 3.

Q4. What is the purpose of // 10?

It removes the last digit of a number.

Example: 153 // 10 = 15.

Q5. What is the difference between / and //?
- / performs normal division.
- // performs floor division.
Q6. Why do we use **?

It is the exponentiation operator. It calculates the power of a number.

Example: 5 ** 3 = 125.

Q7. Can we check Armstrong numbers without converting to a string?

Yes. We can count digits using mathematical operations and process each digit using a while loop.

Q8. Which method is best for interviews?

I prefer the mathematical approach because it demonstrates my understanding of loops and arithmetic operators.

Q9. What happens if the input is 123?

The sum is:
1³ + 2³ + 3³ = 36


Since 36 is not equal to 123, it is not an Armstrong number.

Q10. What is the time complexity?

O(d), because we process every digit exactly once.

8. Interviewee Explanation (Speak Naturally)
"First, I store the original number in a temporary variable because I need it for the final comparison.

Then I find the total number of digits. I use a while loop to extract each digit using the modulo operator. I raise each digit to the power of the total number of digits and add the result to a sum variable.

Finally, I compare the sum with the original number. If both are equal, it is an Armstrong number; otherwise, it is not an Armstrong number.

The time complexity is O(d), where d is the number of digits."
 Copy answer

9. README.md – Revision Notes
You can save these notes in your Python interview preparation folder as Armstrong_Number_README.md.
Python – Armstrong Number
1. Problem
Check whether a given number is an Armstrong number.
2. Definition
A number is an Armstrong number if the sum of its digits raised to the power of the total number of digits equals the original number.

Example: 153

1³ + 5³ + 3³ = 153

Result: Armstrong Number.
3. Recommended Approach
Mathematical Approach using while loop.
4. Important Operators
Operator	Purpose
%	Extract last digit
//	Remove last digit
**	Calculate power
==	Compare two values5. Main Logic
1. Store the original number.
2. Find the total number of digits.
3. Extract each digit using % 10.
4. Calculate digit ** power.
5. Add the results.
6. Remove the last digit using // 10.
7. Compare the sum with the original number.
6. Python Code
n = 153
t = n
p = len(str(n))
s = 0

while t > 0:
    d = t % 10
    s += d ** p
    t //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
7. Output
Armstrong Number
8. Complexity
- Time Complexity: O(d)
- Auxiliary Space: O(1) for the loop logic.
- Exact implementation Space: O(d) due to str(n).
Here, d = number of digits.
9. Interview Questions
1. What is an Armstrong number?
2. Why do we use % 10?
3. Why do we use // 10?
4. What is the purpose of **?
5. Why do we store the original number?
6. What is the time complexity?
7. Can we solve this without string conversion?
8. Can we solve this using recursion?
10. Remember
- % 10 → Extract last digit.
- // 10 → Remove last digit.
- ** → Calculate power.
- len(str(n)) → Count digits.
- sum == original number → Armstrong number.




Small interview note: The given code works for non-negative integers, including 0. If the interviewer asks about negative numbers, clarify that the standard Armstrong-number check here is intended for non-negative integers.
10. Practice Questions
Try these without looking at the solution.
Armstrong Number Test
0/5 answered

1. What is the output for 370?

Armstrong Number

Not Armstrong Number




2. What does 153 % 10 return?

15

3

153




3. What does 153 // 10 return?

3

15

153




4. Why do we use len(str(n))?

To find the last digit

To count digits

To calculate power




5. What is the time complexity?

O(1)

O(d)

O(d²)



Submit answers
My advice: First practise the mathematical approach until you can write it without looking at the code. Then practise explaining the dry run for 153, 370, and 123. This is more useful in a fresher coding interview than memorising all four methods.