Python Program to Find the Missing Number in an Array
Recommended for fresher interviews
 Beginner level

1. Problem statement
Question: Given an array containing distinct numbers from 1 to n+1, find the one missing number.

Definition: A missing number is a number that should be present in a sequence but is not present in the given array.

Example:

Input:
arr = [1, 2, 4, 5]



Output:
Missing number: 3


Here, the expected sequence is [1, 2, 3, 4, 5], but 3 is missing.

Assumption: The array contains distinct positive integers from 1 to n+1, with exactly one number missing.
2. Why, purpose, how, where and when?
- Why? To understand arrays, loops, mathematical formulas, and searching.
- Purpose: Find the missing value in a sequence.
- How? Compare the expected numbers with the numbers present in the array.
- Where? Coding interviews, data validation, and sequence-processing problems.
- When? When a question gives numbers from a known range and asks for the missing number.
3. Method 1: Using the Sum Formula
Recommended for fresher interviews
Definition: Calculate the expected sum of numbers from 1 to n+1, then subtract the actual array sum.

Formula:
\[
\text{Expected Sum} = \frac{N(N+1)}{2}
\]

\[
\text{Missing Number} = \text{Expected Sum} - \text{Actual Sum}
\]

Here, N = len(arr) + 1.

Syntax:
expected_sum = n * (n + 1) // 2actual_sum = sum(arr)missing = expected_sum - actual_sum



Code:
arr = [1, 2, 4, 5]n = len(arr) + 1expected_sum = n * (n + 1) // 2actual_sum = sum(arr)missing = expected_sum - actual_sumprint("Missing number:", missing)



Output:
Missing number: 3


4. Dry run – Sum Formula
Input: [1, 2, 4, 5]

Step 1: Find the expected range size.

n = len(arr) + 1 = 4 + 1 = 5

Step 2: Calculate the expected sum.
\[
\frac{5 \times 6}{2} = 15
\]

Step 3: Calculate the actual sum.
\[
1 + 2 + 4 + 5 = 12
\]

Step 4: Subtract both sums.
\[
15 - 12 = 3
\]

Final answer: 3
Variable	Value
Array length	4
Expected sum	15
Actual sum	12
Missing number	3

Why is this method good? It uses a simple formula and does not require sorting or an additional data structure.
5. Method 2: Using XOR (^)
Definition: XOR is a bitwise operator. When the same number is XORed twice, it cancels out.

Important properties:
- a ^ a = 0
- a ^ 0 = a
Code:
def find_missing_xor(arr):    n = len(arr) + 1    xor_all = 0    xor_arr = 0    for i in range(1, n + 1):        xor_all ^= i    for num in arr:        xor_arr ^= num    return xor_all ^ xor_arrprint(find_missing_xor([1, 2, 4, 5]))



Output:
3


Dry run:

Expected numbers: 1, 2, 3, 4, 5
- xor_all = 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1
- xor_arr = 1 ^ 2 ^ 4 ^ 5 = 2
- missing = 1 ^ 2 = 3
The matching numbers cancel out, leaving only 3.
6. Method 3: Using a Set
Definition: A set stores unique elements and allows efficient membership checking.

Code:
arr = [1, 2, 4, 5]num_set = set(arr)n = len(arr) + 1for i in range(1, n + 1):    if i not in num_set:        print("Missing number:", i)        break



Output:
Missing number: 3


Dry run:
Number checked	Is it in the set?	Action
1	Yes	Continue
2	Yes	Continue
3	No	Missing number found

Why use a set? It is useful when you need to check whether values exist, especially when there may be multiple missing numbers.
7. Method 4: Using Sorting
Definition: Sort the array and compare each number with its expected position.

Code:
arr = [5, 2, 1, 4]arr.sort()for i, num in enumerate(arr):    if num != i + 1:        print("Missing number:", i + 1)        breakelse:    print("Missing number:", len(arr) + 1)



Output:
Missing number: 3


Dry run:

After sorting:

[1, 2, 4, 5]
Index i	Expected i + 1	Actual number	Result
0	1	1	Match
1	2	2	Match
2	3	4	Missing 3

The first mismatch tells us that 3 is missing.

Note: Sorting changes the original list.
8. Time and space complexity
Let n be the number of elements in the given array.
Method	Time complexity	Auxiliary space
Sum formula	O(n)	O(1)
XOR	O(n)	O(1)
Set	O(n) average	O(n)
Sorting	O(n log n)	Depends on sorting implementation

Why?
- Sum formula – O(n): Python's sum() visits all array elements once.
- XOR – O(n): One loop visits the expected range and another visits the array.
- Set – O(n) average: Building the set and checking the expected numbers take O(n) average time.
- Sorting – O(n log n): Sorting requires comparisons between elements.
Space note: Python's list.sort() can use O(n) temporary memory in the worst case. So do not automatically claim O(1) space for Python sorting.
9. Which method should you follow?
My recommendation is Method 1: Sum Formula.

Why?
1. Easy mathematical logic.
2. Simple to explain to an interviewer.
3. O(n) time complexity.
4. O(1) auxiliary space.
5. No sorting or extra set required.
Also practice XOR because interviewers may ask for an alternative solution.

Important interview condition: The sum formula and XOR methods work under the stated assumption: numbers are distinct, from 1 to n+1, and exactly one number is missing.
10. Interview questions and answers
Q1. What is a missing number?

A number that should be present in a sequence but is absent from the given array.

Q2. Why do we use len(arr) + 1?

Because the array contains one missing number. If there are 4 elements, the complete sequence should contain 5 numbers.

Q3. Why do we use // 2 in the formula?

To perform integer division and get the whole-number result.

Q4. What is XOR?

XOR is a bitwise operator. A number XORed with itself gives zero.

Q5. Which method is best?

The sum formula is a simple and efficient choice when the input follows the given conditions.

Q6. What happens if the array is already complete?

That is outside the problem's assumption of exactly one missing number. We would need to validate the input separately.
11. Interviewee explanation
"I use the sum formula to find the missing number. First, I calculate the expected number of elements by adding one to the array length. Then I calculate the expected sum using the formula n multiplied by n plus one divided by two. Next, I calculate the actual sum of the array using Python's sum() function. Finally, I subtract the actual sum from the expected sum. The result is the missing number. The time complexity is O(n), and the auxiliary space complexity is O(1)."
12. README.md – Interview revision notes
Find the Missing Number in Python
Problem Statement
Given an array containing distinct numbers from 1 to n+1, find the one missing number.

Input:
arr = [1, 2, 4, 5]
Output:
Missing number: 3
Method 1: Sum Formula (Recommended)
Formula
Expected Sum = n * (n + 1) // 2

Missing Number = Expected Sum - Actual Sum
Code
arr = [1, 2, 4, 5]

n = len(arr) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("Missing number:", missing)
Dry Run
- Array: [1, 2, 4, 5]
- Expected range: 1 to 5
- Expected sum: 5 * 6 // 2 = 15
- Actual sum: 1 + 2 + 4 + 5 = 12
- Missing number: 15 - 12 = 3
Method 2: XOR
def find_missing_xor(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

print(find_missing_xor([1, 2, 4, 5]))
Output: 3

XOR cancels matching numbers, leaving the missing number.
Method 3: Set
arr = [1, 2, 4, 5]

num_set = set(arr)
n = len(arr) + 1

for i in range(1, n + 1):
    if i not in num_set:
        print("Missing number:", i)
        break
Method 4: Sorting
arr = [5, 2, 1, 4]

arr.sort()

for i, num in enumerate(arr):
    if num != i + 1:
        print("Missing number:", i + 1)
        break
else:
    print("Missing number:", len(arr) + 1)
Complexity Comparison
Method	Time	Auxiliary Space
Sum Formula	O(n)	O(1)
XOR	O(n)	O(1)
Set	O(n) average	O(n)
Sorting	O(n log n)	Depends on implementationImportant Python Concepts
- len(arr) – returns the number of elements.
- sum(arr) – calculates the total.
- set(arr) – creates a set of unique elements.
- // – integer division.
- ^ – bitwise XOR.
- sort() – sorts the original list.
- enumerate() – returns index and element together.
Interview Questions
1. What is a missing number?
2. Why do we add one to the array length?
3. What is the sum formula?
4. Why do we use integer division?
5. What is XOR?
6. Why is the sum formula O(n)?
7. What is the difference between a set and a list?
Interview Recommendation
Use the sum formula as your first solution. Learn XOR as an alternative O(n)-time, O(1)-space solution.

Assumption: The input contains distinct numbers from 1 to n+1, with exactly one missing number.




13. Practice question
Try this without looking at the solution:
arr = [1, 3, 4, 5, 6]



What is the missing number?

Hint: First calculate n = len(arr) + 1, then apply the sum formula.