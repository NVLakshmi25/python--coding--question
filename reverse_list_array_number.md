Python Program to Reverse a List, Array, and Number
Recommended for fresher interviews
 Beginner level


These are three related but different interview problems:
1. Reverse a list: Change the order of list elements.
2. Reverse an array: Same logic as reversing a list in Python. An array is a collection of elements.
3. Reverse a number: Reverse the digits of an integer.
Let's understand each with different methods and choose the best one for interviews.

1. Reverse a List in Python
Problem statement
Question: Given a list, reverse the order of its elements.

Example:

Input:
[10, 20, 30, 40, 50]



Output:
[50, 40, 30, 20, 10]



Why? To rearrange elements from last to first.

Purpose: To understand lists, indexing, slicing, and swapping.

Where and when? List manipulation, data processing, and coding interviews.
Method 1: Using reverse() – Recommended for practical Python code
Definition: reverse() is a list method that reverses the original list in place.

Syntax:
list_name.reverse()



Code:
numbers = [10, 20, 30, 40, 50]numbers.reverse()print(numbers)



Output:
[50, 40, 30, 20, 10]


Important: It modifies the original list and returns None.
Method 2: Using slicing
Definition: Slicing with [::-1] creates a new reversed list.
numbers = [10, 20, 30, 40, 50]reversed_list = numbers[::-1]print(reversed_list)



Output:
[50, 40, 30, 20, 10]


[::-1] means reading the list from the end to the beginning.
Method 3: Using two pointers – Recommended for coding interviews
Definition: Two pointers start at opposite ends and swap elements until they meet.

Syntax:
left = 0right = len(numbers) - 1while left < right:    numbers[left], numbers[right] = numbers[right], numbers[left]    left += 1    right -= 1



Complete code:
numbers = [10, 20, 30, 40, 50]left = 0right = len(numbers) - 1while left < right:    numbers[left], numbers[right] = numbers[right], numbers[left]    left += 1    right -= 1print(numbers)



Output:
[50, 40, 30, 20, 10]


Dry run – Two pointers
Step	Left	Right	List
Initial	0	4	[10,20,30,40,50]
1	0	4	[50,20,30,40,10]
2	1	3	[50,40,30,20,10]
Stop	2	2	Loop ends

The loop stops when left is no longer less than right.
List reversal: complexity
Let n be the number of elements.
Method	Time	Extra space
reverse()	O(n)	O(1)
Slicing [::-1]	O(n)	O(n)
Two pointers	O(n)	O(1)

Why?
- O(n) time because elements must be visited or copied.
- O(1) auxiliary space for reverse() and two pointers because they use a fixed number of variables and modify the original list.
- O(n) space for slicing because it creates a new list.
Recruiter point of view: Learn the two-pointer method for explaining the algorithm and reverse() for everyday Python programming.

2. Reverse an Array in Python
Problem statement
Question: Given an array, reverse its elements in place.

Example:

Input:
[1, 4, 3, 2, 6, 5]



Output:
[5, 6, 2, 3, 4, 1]



Important: In Python, a normal list is commonly used for array-based coding interview problems. The same two-pointer logic works for both.
Method 1: Using a temporary list
arr = [1, 4, 3, 2, 6, 5]temp = []for i in range(len(arr) - 1, -1, -1):    temp.append(arr[i])arr = tempprint(arr)



Output:
[5, 6, 2, 3, 4, 1]


Explanation: Read the original list from the last index to the first and store each element in a new list.
Method 2: Using two pointers – Best for in-place array reversal
arr = [1, 4, 3, 2, 6, 5]left = 0right = len(arr) - 1while left < right:    arr[left], arr[right] = arr[right], arr[left]    left += 1    right -= 1print(arr)



Output:
[5, 6, 2, 3, 4, 1]


Method 3: Using a single pointer
arr = [1, 4, 3, 2, 6, 5]n = len(arr)for i in range(n // 2):    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]print(arr)



Output:
[5, 6, 2, 3, 4, 1]


How does it work?
- Swap index 0 with index n-1.
- Swap index 1 with index n-2.
- Continue until the middle of the list.
Complexity of array methods
Method	Time	Extra space
Temporary list	O(n)	O(n)
Two pointers	O(n)	O(1)
Single pointer	O(n)	O(1)
reverse()	O(n)	O(1)

Recommendation: For an interview question that says reverse the array in place, use the two-pointer or single-pointer method. Both are efficient and use O(1) auxiliary space.

3. Reverse a Number in Python
Problem statement
Question: Given an integer, reverse its digits.

Example:

Input:
12345



Output:
54321



Definition: Reversing a number means arranging its digits from last to first.

Why? To understand arithmetic operations and digit manipulation.

Purpose: To practice modulo %, floor division //, and loops.

Where and when? Number-based coding problems and fresher technical interviews.
Method 1: Using string slicing
Definition: Convert the number into a string, reverse it, and convert it back into an integer.
n = 12345rev = int(str(n)[::-1])print(rev)



Output:
54321


How?
- str(n) converts the number into a string.
- [::-1] reverses the string.
- int() converts it back into an integer.
Method 2: Using a while loop – Recommended for interviews
This method reverses the number mathematically without converting it into a string.

Syntax:
digit = n % 10rev = rev * 10 + digitn = n // 10



Complete code:
n = 6789rev = 0while n > 0:    digit = n % 10    rev = rev * 10 + digit    n //= 10print(rev)



Output:
9876


Important operators:
- % 10 – extracts the last digit.
- * 10 – shifts the existing reversed number one position to the left.
- // 10 – removes the last digit.
Dry run – While loop
Input: 6789
Iteration	n	digit = n % 10	rev = rev * 10 + digit	n // 10
1	6789	9	9	678
2	678	8	98	67
3	67	7	987	6
4	6	6	9876	0

The loop stops when n becomes 0.

Output:
9876


Method 3: Using a for loop
n = 6789rev = ""for ch in str(n):    rev = ch + revprint(int(rev))



Output:
9876


Explanation: Each new character is added to the beginning of the reversed string.
Method 4: Using recursion
def reverse_number(n):    if n < 10:        return n    return int(str(n % 10) + str(reverse_number(n // 10)))print(reverse_number(6789))



Output:
9876


Explanation: The function repeatedly calls itself with the last digit removed. It builds the reversed number as the recursive calls return.
Number reversal: complexity
Let d be the number of digits.
Method	Time	Extra space
String slicing	O(d)	O(d)
While loop	O(d)	O(1)
For loop	O(d²)	O(d)
Recursion	O(d²)	O(d)

Why?
- While loop: processes one digit per iteration, so O(d) time.
- String slicing: creates a reversed string, so O(d) time and space.
- For loop: rev = ch + rev creates a new string repeatedly, resulting in O(d²) total character copying.
- Recursion: string concatenation at each call can take O(d²) time, and recursive calls use O(d) stack space.
Important: These examples assume non-negative integers. The while-loop method can also handle negative numbers by using abs(n) and restoring the sign afterward. Reversing 1200 as an integer gives 21, because leading zeros are not retained.

4. Interview questions and answers
Q1. What is the difference between reverse() and slicing?

reverse() modifies the original list. Slicing creates a new reversed list.

Q2. What is the difference between reverse() and reversed()?

reverse() modifies the original list. reversed() returns an iterator without modifying the original list.

Q3. What is the two-pointer technique?

We use two indexes: one at the beginning and another at the end. We swap their elements and move towards the middle.

Q4. Why do we use left < right?

To stop swapping when both pointers meet or cross each other.

Q5. How do you extract the last digit of a number?

Using n % 10.

Q6. How do you remove the last digit?

Using n // 10.

Q7. Why do we use rev * 10 + digit?

To shift the existing reversed number left by one digit and add the newly extracted digit.
5. Interviewee explanations
If asked to reverse a list or array:

"I initialize two pointers, one at the beginning and another at the end of the list. I swap their elements and move both pointers towards the middle. I repeat this until the pointers meet. This reverses the list in place. The time complexity is O(n), and the auxiliary space complexity is O(1)."

If asked to reverse a number:

"I initialize a variable called rev to zero. I extract the last digit using modulo 10. Then I multiply the reversed number by 10 and add the extracted digit. After that, I remove the last digit using floor division by 10. I repeat this until the original number becomes zero. The time complexity is O(d), and the auxiliary space complexity is O(1)."
6. Final revision – What should you remember?
Problem	Recommended method	Time	Space
Reverse a list	Two pointers	O(n)	O(1)
Reverse an array in place	Two pointers	O(n)	O(1)
Reverse a number	While loop	O(d)	O(1)

My recommendation for fresher interviews: Practice the two-pointer method for list/array reversal and the mathematical while-loop method for number reversal. Also understand the built-in methods because interviewers may ask for alternative solutions.
7. README.md – Interview revision notes
Python: Reverse a List, Array, and Number
1. Reverse a List
Input: [10, 20, 30, 40, 50]

Output: [50, 40, 30, 20, 10]
Methods
- list.reverse() – modifies the original list.
- list[::-1] – creates a new reversed list.
- Two pointers – swaps elements from opposite ends.
Recommended code: Two pointers
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print(numbers)
Complexity: O(n) time, O(1) auxiliary space.
2. Reverse an Array
In Python coding interviews, a list is commonly used to represent an array.
Recommended code
arr = [1, 4, 3, 2, 6, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
Output: [5, 6, 2, 3, 4, 1]

Complexity: O(n) time, O(1) auxiliary space.
3. Reverse a Number
Input: 6789

Output: 9876
Recommended code: While loop
n = 6789
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)
Important operators
- % 10 – extracts the last digit.
- rev * 10 – shifts the reversed number.
- + digit – adds the extracted digit.
- // 10 – removes the last digit.
Complexity: O(d) time, O(1) auxiliary space.
Interview questions
1. Difference between reverse() and slicing?
2. Difference between reverse() and reversed()?
3. What is the two-pointer technique?
4. Why do we use left < right?
5. What does % 10 do?
6. What does // 10 do?
7. Why do we multiply rev by 10?
Interview explanation
List/Array: Use two pointers, swap elements from opposite ends, and move towards the middle.

Number: Extract the last digit using % 10, add it to the reversed number, and remove it using // 10.
Important complexity
Problem	Time	Auxiliary space
List reversal	O(n)	O(1)
Array reversal	O(n)	O(1)
Number reversal	O(d)	O(1)n = number of list elements.

d = number of digits in the number.




Practice: Try reversing [5, 10, 15, 20] using two pointers, and reverse the number 12045 using a while loop.