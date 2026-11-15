Python Program to Check Palindrome Number – Interview Notes
Let's understand this problem in simple English with multiple methods, dry runs, interview explanations, syntax, and time and space complexity.

We will cover both number palindrome and array palindrome, because your shared material contains both problems.
1. What is a palindrome number?
Definition: A palindrome number is a number that remains the same when we reverse its digits.

Examples:
Number	Reversed	Result
121	121	Palindrome
1221	1221	Palindrome
123	321	Not palindrome
454	454	Palindrome
12345	54321	Not palindrome

Problem statement:

Given an integer, check whether the number reads the same forwards and backwards.
- Input: 1221
- Expected output: Palindrome
Why do we use this problem?
- To understand while loops.
- To practice mathematical operators.
- To understand digit extraction.
- To improve logical thinking for coding interviews.
2. Method 1: Using while loop and mathematical operators
Important for coding interviews
This is the method used in your first program.

Syntax and important concepts
Operator	Meaning	Example
%	Modulus – gets remainder	1221 % 10 = 1
//	Floor division – removes last digit	1221 // 10 = 122
*	Multiplication	12 * 10 = 120
+	Addition	120 + 1 = 121

Code:
num = int(input("Enter a number: "))temp = numreverse = 0while num > 0:    last_digit = num % 10    reverse = reverse * 10 + last_digit    num = num // 10if temp == reverse:    print("Palindrome")else:    print("Not Palindrome")



How does it work?
1. Take a number from the user.
2. Store the original number in temp.
3. Extract the last digit using % 10.
4. Add that digit to the reversed number.
5. Remove the last digit using // 10.
6. Repeat until the number becomes zero.
7. Compare the original and reversed numbers.
Dry run (step-by-step)
Let's take:
num = 1221temp = 1221reverse = 0



Iteration	num	last_digit = num % 10	reverse = reverse * 10 + last_digit	num // 10
1	1221	1	1	122
2	122	2	12	12
3	12	2	122	1
4	1	1	1221	0

Now the while loop stops because num > 0 is false.

Final comparison:
temp == reverse1221 == 1221True



Output:
Palindrome


Understand these two important lines:
last_digit = num % 10



Why? To extract the last digit.
num = num // 10



Why? To remove the last digit so we can process the next digit.

Interview explanation:

"I take the input number and store its original value in a temporary variable. Then I use a while loop to extract the last digit using modulus 10. I construct the reversed number by multiplying the previous result by 10 and adding the extracted digit. I remove the last digit using floor division. Finally, I compare the original number with the reversed number. If both are equal, it is a palindrome."

Time and space complexity:
- Time: O(d), because we process each digit once.
- Space: O(1), because we use only a fixed number of variables.
Here, d means the number of digits in the input number.

Why O(1) space? We don't create another list or string. We only use temp, reverse, num, and last_digit.

3. Method 2: Using string conversion and slicing
Shortest and easiest method
Definition: Convert the integer into a string, reverse it using slicing, and compare both values.

Syntax:
str(number)[::-1]



Code:
num = 1221text = str(num)reverse = text[::-1]if text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Output:
Palindrome


Dry run:
num = 1221

str(num) = "1221"

text[::-1] = "1221"

Compare:

"1221" == "1221"

True


Interview explanation:

"I convert the number into a string using str(). Then I reverse the string using slicing with a negative one step. Finally, I compare the original string and reversed string. If they are equal, the number is a palindrome."

Complexity:
- Time: O(d), because we convert and reverse all digits.
- Space: O(d), because we create string copies.
When should we use it?

When the interviewer allows built-in string methods and wants a simple solution.

4. Method 3: Using a for loop
Definition: A for loop processes each character of a string one by one.

Code:
num = 1221text = str(num)reverse = ""for digit in text:    reverse = digit + reverseif text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Dry run:
Iteration	digit	reverse
1	1	1
2	2	21
3	2	221
4	1	1221

Comparison:
"1221" == "1221"
True


Interview explanation:

"I convert the number into a string and initialize an empty string. I use a for loop to read each digit. In every iteration, I add the current digit to the beginning of the result. Finally, I compare both strings."

Complexity:
- Time: O(d²) due to repeated string concatenation.
- Space: O(d) for the reversed string.

5. Method 4: Using two pointers (number as a string)
Definition: Two pointers means using two indexes to compare elements from opposite ends.

Code:
def is_palindrome(num):    text = str(num)    left = 0    right = len(text) - 1    while left < right:        if text[left] != text[right]:            return False        left += 1        right -= 1    return Trueprint(is_palindrome(1221))



Output:
True


Dry run:
text = "1221"

Index:  0  1  2  3
        1  2  2  1
        ↑        ↑
       left    right


Iteration	Left character	Right character	Comparison
1	1	1	Equal
2	2	2	Equal

Now left becomes 2 and right becomes 1.

Condition left < right becomes false.

Return True.

Interview explanation:

"I use two pointers. One starts from the beginning and the other starts from the end. I compare both characters. If they are different, I return False. Otherwise, I move the left pointer forward and the right pointer backward. If all pairs match, the number is a palindrome."

Complexity:
- Time: O(d), because we compare at most half the digits.
- Space: O(d), because we convert the number into a string.

6. Comparison of number palindrome methods
Method	Time	Space
While + mathematical operators	O(d)	O(1)
String + slicing	O(d)	O(d)
For loop + concatenation	O(d²)	O(d)
Two pointers + string	O(d)	O(d)

Which is best?
- Best without converting to string: Method 1.
- Easiest to write: Method 2.
- Best for demonstrating two-pointer logic: Method 4.

7. Important interview questions
Q1. What is a palindrome number?

A number that remains the same when its digits are reversed.

Q2. Why do we store the original number in temp?

Because the while loop changes the original num variable by removing its digits. We need the original value for comparison.

Q3. Why do we initialize reverse = 0?

Because we need an empty numeric value to build the reversed number.

Q4. Why do we multiply reverse by 10?

To shift the existing digits one position to the left and make space for the new last digit.

Example:
12 * 10 = 120
120 + 3 = 123


Q5. What happens if we enter 123?

The reversed number becomes 321. Since 123 is not equal to 321, it is not a palindrome.

Q6. What happens if we enter 7?

It is a palindrome because a single-digit number is always equal to its reverse.

Q7. Can negative numbers be palindromes?

Under the usual integer definition, no. For example, -121 reverses to 121-, so it is not a palindrome.

Q8. Why is the mathematical approach space O(1)?

Because it uses a fixed number of variables regardless of the number of digits.

8. Important: Array palindrome
Your shared material also includes a second problem: checking whether an array is a palindrome.

Definition: An array is a palindrome if its elements remain the same when read from left to right and right to left.

Example:
nums = [10, 12, 15, 12, 10]



Expected result:
True


Method 1: Using slicing
nums = [10, 12, 15, 12, 10]if nums == nums[::-1]:    print("Palindrome")else:    print("Not Palindrome")



Dry run:
Original: [10, 12, 15, 12, 10]

Reverse:  [10, 12, 15, 12, 10]

Comparison: True


Complexity: Time O(n), Space O(n).
Method 2: Using two pointers
Best for array space efficiency
def is_palindrome(nums):    left = 0    right = len(nums) - 1    while left < right:        if nums[left] != nums[right]:            return False        left += 1        right -= 1    return Truenums = [10, 12, 15, 12, 10]print(is_palindrome(nums))



Output:
True


Dry run:
Iteration	Left element	Right element	Result
1	10	10	Equal
2	12	12	Equal
3	15	15	Middle element

All pairs match, so it returns True.

Complexity:
- Time: O(n).
- Space: O(1), because we use only two pointers.
Why is the two-pointer method efficient?

It compares elements directly without creating a reversed copy of the array.
9. README.md – Quick revision notes
Here is a README-style version you can keep for Python interview preparation.
Python – Palindrome Number and Array
1. Problem Statement
Check whether a number or an array reads the same forwards and backwards.
Examples
Input	Output
121	True
1221	True
123	False
7	True2. Number Palindrome – Mathematical Method
num = int(input("Enter a number: "))

temp = num
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
Important operators
- % 10: Extracts the last digit.
- // 10: Removes the last digit.
- reverse * 10: Shifts existing digits left.
- + last_digit: Adds the extracted digit.
Complexity
- Time: O(d)
- Space: O(1)
Here, d is the number of digits.
3. Number Palindrome – Slicing Method
num = 1221

text = str(num)
reverse = text[::-1]

print(text == reverse)
Complexity
- Time: O(d)
- Space: O(d)
4. Number Palindrome – Two Pointers
def is_palindrome(num):
    text = str(num)

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True
Complexity
- Time: O(d)
- Space: O(d)
5. Array Palindrome – Slicing
nums = [10, 12, 15, 12, 10]

print(nums == nums[::-1])
Complexity
- Time: O(n)
- Space: O(n)
6. Array Palindrome – Two Pointers
def is_palindrome(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] != nums[right]:
            return False

        left += 1
        right -= 1

    return True
Complexity
- Time: O(n)
- Space: O(1)
7. Interview Summary
A palindrome is a number or sequence that remains the same when reversed.

For number palindrome, I can use mathematical operators such as modulus and floor division to extract digits and construct the reversed number.

For array palindrome, I can use two pointers to compare elements from both ends.

Important concepts to remember:
1. Modulus % extracts the last digit.
2. Floor division // removes the last digit.
3. Slicing [::-1] reverses a sequence.
4. Two pointers compare elements from opposite ends.
5. Always preserve the original number when using the mathematical method.
Best interview approach:
- Number: Mathematical reversal – O(d) time and O(1) space.
- Array: Two pointers – O(n) time and O(1) space.




10. Practice test
Test your understanding
0/5

1. What does 1221 % 10 return?

122

1

12

0




2. What does 1221 // 10 return?

122.1

1

122

221




3. Why do we use reverse * 10?

To remove digits

To shift digits left

To compare numbers

To stop the loop




4. What is the space complexity of mathematical palindrome checking?

O(n)

O(n²)

O(1)

O(log n)




5. Which method checks an array using O(1) extra space?

Slicing

Two pointers

Sorting

Copying the array .

-------------------------------------------------
1. What is a palindrome string?
Definition: A palindrome string is a word or string that reads the same from left to right and right to left.

Examples:
Input	Reverse	Result
MADAM	MADAM	Palindrome
LEVEL	LEVEL	Palindrome
RADAR	RADAR	Palindrome
HELLO	OLLEH	Not palindrome
PYTHON	NOHTYP	Not palindrome

Problem statement:

Given a string, check whether it is a palindrome or not.
Example 1

Input: "MADAM"

Output: True

Example 2

Input: "HELLO"

Output: False

Why do we solve this problem?
- To understand string manipulation.
- To practice loops and conditions.
- To understand indexing and slicing.
- To improve logical thinking for coding interviews.
2. Method 1: Using slicing [::-1]
Simplest method
Definition: Slicing is used to extract characters from a string using indexes.

Syntax:
string[start:stop:step]



For reversing:
string[::-1]



Why -1?

Because a negative step tells Python to read characters from right to left.

Code:
text = "MADAM"reverse = text[::-1]if text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Output:
Palindrome


Dry run
Original string:
Index:  0  1  2  3  4
        M  A  D  A  M


Reversed string:
Index:  4  3  2  1  0
        M  A  D  A  M


Comparison:
text == reverse"MADAM" == "MADAM"True



Interview explanation:

"I take a string and reverse it using slicing with a negative one step. Then I compare the original string with the reversed string. If both are equal, it is a palindrome; otherwise, it is not."

Complexity:
- Time: O(n) – We process all characters.
- Space: O(n) – A new reversed string is created.

3. Method 2: Using reversed() and join()
Definition: reversed() returns an iterator that provides characters in reverse order. join() combines those characters into a string.

Syntax:
"".join(reversed(string))



Code:
text = "LEVEL"reverse = "".join(reversed(text))if text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Output:
Palindrome


Dry run
First:
reversed("LEVEL")



Characters produced:
L → E → V → E → L


Next:
"".join(...)



Result:
"LEVEL"


Comparison:
"LEVEL" == "LEVEL"

True


Interview explanation:

"I use reversed() to read the characters backwards. Since reversed() returns an iterator, I use join() to combine the characters into a string. Finally, I compare both strings."

Complexity:
- Time: O(n)
- Space: O(n) for the resulting string; the iterator itself uses O(1) auxiliary space.

4. Method 3: Using a for loop
Definition: A for loop reads each character from the string one by one.

Why do we use it?

To understand how to reverse a string manually without using slicing or reversed().

Code:
text = "MADAM"reverse = ""for char in text:    reverse = char + reverseif text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Dry run
Initially:
reverse = ""



Iteration	char	Expression	reverse
1	M	M + ""	M
2	A	A + M	AM
3	D	D + AM	DAM
4	A	A + DAM	ADAM
5	M	M + ADAM	MADAM

Final comparison:
MADAM == MADAM
True


Important line:
reverse = char + reverse



Why?

We add the current character at the beginning of the existing string. This creates the reversed string.

Interview explanation:

"I initialize an empty string and use a for loop to read every character. In each iteration, I add the current character to the beginning of the result. Finally, I compare the original and reversed strings."

Complexity:
- Time: O(n²) – Repeated string concatenation creates new strings.
- Space: O(n) – We store the reversed string.

5. Method 4: Using while loop
Definition: A while loop executes as long as its condition is true.

Why do we use it?

To reverse a string by manually controlling its index.

Code:
text = "MADAM"reverse = ""index = len(text) - 1while index >= 0:    reverse += text[index]    index -= 1if text == reverse:    print("Palindrome")else:    print("Not Palindrome")



Dry run
Initially:
index = len(text) - 1index = 5 - 1index = 4



Iteration	index	text[index]	reverse
1	4	M	M
2	3	A	MA
3	2	D	MAD
4	1	A	MADA
5	0	M	MADAM

After the last iteration, index becomes -1.

Condition:
index >= 0



It becomes false, so the loop stops.

Interview explanation:

"I start from the last index using len(text) - 1. Then I use a while loop to access each character from right to left. I add each character to the result and decrease the index. Finally, I compare both strings."

Complexity:
- Time: O(n²) – Repeated string concatenation.
- Space: O(n) – Reversed string storage.

6. Method 5: Using two pointers
Best for space-efficient checking
Definition: Two pointers means using two indexes to compare characters from opposite ends of a string.

Syntax:
left = 0right = len(text) - 1



Code:
def is_palindrome(text):    left = 0    right = len(text) - 1    while left < right:        if text[left] != text[right]:            return False        left += 1        right -= 1    return Trueprint(is_palindrome("MADAM"))



Output:
True


Dry run
text = "MADAM"

Index:  0  1  2  3  4
        M  A  D  A  M
        ↑           ↑
       left        right


Iteration	Left	Right	Comparison
1	M	M	Equal
2	A	A	Equal

Now:
left = 2
right = 2


Condition left < right becomes false.

The function returns True.

What if the input is HELLO?
H E L L O
↑       ↑


First comparison:
H != O


The function immediately returns False.

Interview explanation:

"I use two pointers. The left pointer starts from the beginning, and the right pointer starts from the end. I compare both characters. If they are different, I return False. Otherwise, I move both pointers towards the center. If all characters match, I return True."

Complexity:
- Time: O(n) – We compare at most half of the characters.
- Space: O(1) – We only use two pointer variables and do not create another string.

7. Comparison of all methods
Method	Time	Space
Slicing	O(n)	O(n)
reversed() + join()	O(n)	O(n)
For loop	O(n²)	O(n)
While loop	O(n²)	O(n)
Two pointers	O(n)	O(1)

Which method should you use in interviews?
- Easiest: Slicing.
- To demonstrate loops: For loop.
- To demonstrate index handling: While loop.
- To demonstrate efficient logic: Two pointers.
8. Important interview questions
Q1. What is a palindrome string?

A string that reads the same forwards and backwards.

Q2. Why do we use [::-1]?

The negative step reverses the order of characters.

Q3. What is the difference between reversed() and slicing?

reversed() returns an iterator, whereas slicing creates a new reversed string.

Q4. Why do we use char + reverse in the for loop?

To add each new character at the beginning of the existing result.

Q5. Why do we use two pointers?

To compare characters from both ends without creating another string.

Q6. What is the time complexity of two pointers?

O(n), because we compare at most half the characters.

Q7. Is an empty string a palindrome?

Yes. It is generally considered a palindrome because there are no mismatching characters.

Q8. Is a single-character string a palindrome?

Yes. For example, "A" is a palindrome.
9. Important real-world variations
Sometimes interviewers give strings with capital letters, small letters, or spaces.

For example:
"Madam"


Should this be a palindrome?

If we compare case-sensitively, "Madam" is not equal to "madaM".

If the interviewer wants case-insensitive checking, convert the string to lowercase.
text = "Madam"text = text.lower()print(text == text[::-1])



Output:
True


For a phrase containing spaces, such as "nurses run", we can remove spaces and convert to lowercase:
text = "nurses run"text = text.replace(" ", "").lower()print(text == text[::-1])



Output:
True


This handles spaces and letter case, but not punctuation. If punctuation should also be ignored, use isalnum() to keep only letters and numbers.
10. README.md – Quick revision
You can save these notes as README.md for future interview revision.
Python – Palindrome String
1. Problem Statement
Given a string, check whether it reads the same forwards and backwards.
Examples
Input	Output
MADAM	True
LEVEL	True
RADAR	True
HELLO	False
PYTHON	False2. Method 1 – Slicing
text = "MADAM"

reverse = text[::-1]

print(text == reverse)
Time: O(n)
Space: O(n)
3. Method 2 – reversed() and join()
text = "MADAM"

reverse = "".join(reversed(text))

print(text == reverse)
Time: O(n)
Space: O(n)
4. Method 3 – For Loop
text = "MADAM"
reverse = ""

for char in text:
    reverse = char + reverse

print(text == reverse)
Time: O(n²)
Space: O(n)
5. Method 4 – While Loop
text = "MADAM"
reverse = ""
index = len(text) - 1

while index >= 0:
    reverse += text[index]
    index -= 1

print(text == reverse)
Time: O(n²)
Space: O(n)
6. Method 5 – Two Pointers
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome("MADAM"))
Time: O(n)
Space: O(1)
7. Important Concepts
- Palindrome: Same forwards and backwards.
- Slicing: Extracting characters using indexes.
- reversed(): Returns characters in reverse order through an iterator.
- join(): Combines characters into a string.
- Two pointers: Compare characters from opposite ends.
- Immutable: Python strings cannot be modified directly.
8. Interview Summary
A palindrome string reads the same from left to right and right to left.

I can solve this problem using slicing, reversed(), loops, and two pointers.

For an efficient solution, I prefer the two-pointer approach because it takes O(n) time and O(1) extra space without creating another string.
9. Edge Cases
- Empty string: True
- Single character: True
- "MADAM": True
- "HELLO": False
- "Madam": False with case-sensitive comparison


11. Practice these interview questions
Predict the output before revealing the answer.
1. {t.q}


Reveal

2. {t.q}


Reveal

3. {t.q}


Reveal

4. {t.q}


Reveal

5. {t.q}
Answer: True