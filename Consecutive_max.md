
# Maximum Consecutive Occurrence in Python

## Problem Statement
Find the element that appears the maximum number of times continuously in a list.

### Example

Input:
```python
nums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]
```

Output:
```text
5
```

## Method 1: For Loop (Recommended)

```python
def max_consecutive(nums):
    if not nums:
        return None

    max_element = nums[0]
    max_count = 1
    current_count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_element = nums[i]

    return max_element


nums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]
print(max_consecutive(nums))
```

## Method 2: itertools.groupby()

```python
from itertools import groupby

nums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]

result = max(
    groupby(nums),
    key=lambda item: len(list(item[1]))
)

print(result[0])
```

## Method 3: Sliding-window Style

```python
def max_consecutive(nums):
    if not nums:
        return None

    current_element = nums[0]
    current_count = 1
    max_element = nums[0]
    max_count = 1

    for i in range(1, len(nums)):
        num = nums[i]

        if num == current_element:
            current_count += 1
        else:
            current_element = num
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_element = current_element

    return max_element
```

## Complexity

| Method | Time | Auxiliary Space |
|---|---|---|
| For loop | O(n) | O(1) |
| groupby() | O(n) | O(n) worst case |
| Sliding-window style | O(n) | O(1) |

## Important Concepts

- Consecutive occurrence means adjacent repeated elements.
- `current_count` tracks the current group.
- `max_count` tracks the longest group.
- Reset the current count when the element changes.
- `groupby()` groups adjacent equal elements.
- Dictionary frequency counts total occurrences, not consecutive occurrences.

## Interview Recommendation

Use the for-loop approach.

It is easy to understand, efficient, and uses O(1) auxiliary space.

## Key Point

Total frequency and maximum consecutive occurrence are different problems.


Practice question: Try this input without looking at the solution:

nums = [4, 4, 2, 2, 2, 3, 3, 3, 3, 1] .

--------------------------------------------------------------
Find the Maximum Consecutive Occurring Element in Python
1. Problem statement
What is the task?

Given a list, find the element that appears the maximum number of times continuously (next to each other).

Example:
nums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]



Output:
5


Why is the answer 5?
- 1 appears continuously 3 times.
- 2 appears continuously 2 times.
- 4 appears continuously 1 time.
- The next 2 appears continuously 2 times.
- 5 appears continuously 4 times.
So, 5 has the longest consecutive occurrence.
Important difference
- Consecutive occurrence: count identical elements next to each other.
- Total frequency: count all occurrences, even if they are separated.
Example: [2, 2, 3, 2, 2, 2]
- Maximum consecutive occurrence of 2 = 3
- Total frequency of 2 = 5

2. Basic definitions
Term	Meaning
Consecutive	Elements appearing continuously next to each other
Occurrence	Number of times an element appears
Current count	Count of the current continuous group
Maximum count	Highest continuous count found so far
Sliding window	A window that moves through elements
groupby()	Groups adjacent equal elements

3. Why, how, where and when?
- Why? To identify the longest continuous repetition in a list.
- Purpose? Find which element has the highest consecutive count.
- How? Compare each element with the previous element and update the counts.
- Where? Coding interviews, sequence analysis and data processing.
- When? When a problem asks for the longest repeated or consecutive sequence.
4. Method 1: Using a simple for loop
Recommended for interviews
def max_consecutive(nums):    if not nums:        return None    max_element = nums[0]    max_count = 1    current_count = 1    for i in range(1, len(nums)):        if nums[i] == nums[i - 1]:            current_count += 1        else:            current_count = 1        if current_count > max_count:            max_count = current_count            max_element = nums[i]    return max_elementnums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]print(max_consecutive(nums))



Output:
5


Syntax
for i in range(1, len(nums)):    if nums[i] == nums[i - 1]:        current_count += 1    else:        current_count = 1



How does it work?
- max_element: stores the element with the longest consecutive occurrence.
- max_count: stores the highest count.
- current_count: counts the current consecutive elements.
- If the current element equals the previous element, increase the count.
- Otherwise, reset the count to 1.
- If the current count is greater than the maximum count, update the answer.
Dry run
Input:
[1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]



Current element	Current count	Maximum count	Maximum element
1	1	1	1
1	2	2	1
1	3	3	1
2	1	3	1
2	2	3	1
4	1	3	1
2	1	3	1
2	2	3	1
5	1	3	1
5	2	3	1
5	3	3	1
5	4	4	5

Final answer: 5
Complexity
- Time: \(O(n)\) – visits each element once.
- Auxiliary space: \(O(1)\) – uses only a fixed number of variables, regardless of list size.
5. Method 2: Using itertools.groupby()
Python built-in approach
from itertools import groupbynums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]result = max(    groupby(nums),    key=lambda item: len(list(item[1])))print(result[0])



Output:
5


Syntax
groupby(iterable)



How does it work?
- groupby() groups adjacent equal elements.
- item[0] is the element.
- item[1] is the group iterator.
- len(list(item[1])) calculates the size of that group.
- max() selects the group with the highest size.
Dry run:
Input:
[1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]

Groups:
1 → [1, 1, 1]       Count = 3
2 → [2, 2]          Count = 2
4 → [4]             Count = 1
2 → [2, 2]          Count = 2
5 → [5, 5, 5, 5]    Count = 4

Maximum group = 5


Complexity:
- Time: \(O(n)\) – all elements are processed.
- Auxiliary space: \(O(n)\) worst case – list() temporarily stores a group, which could contain all elements.
Interview note: groupby() groups only adjacent equal values. It does not combine separated groups of the same value.
6. Method 3: Using a sliding-window style single pass
This is similar to Method 1. We track the current run and the longest run while moving through the list.
def max_consecutive(nums):    if not nums:        return None    current_element = nums[0]    current_count = 1    max_element = nums[0]    max_count = 1    for num in nums[1:]:        if num == current_element:            current_count += 1        else:            current_element = num            current_count = 1        if current_count > max_count:            max_count = current_count            max_element = current_element    return max_elementnums = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]print(max_consecutive(nums))



Output:
5


How does it work?
- Keep track of the current element and its count.
- If the next element is the same, increase the count.
- Otherwise, start a new run.
- Update the maximum whenever the current run becomes longer.
Complexity:
- Time: \(O(n)\) – one pass through the list.
- Auxiliary space: \(O(1)\) – only a few variables are used.
7. Important: Why the dictionary method is not suitable here
The dictionary approach in your article counts the total frequency of each element, not its consecutive frequency.

Example:
nums = [1, 1, 2, 2, 2, 1, 1, 1]



- Total frequency: 1 appears 5 times, 2 appears 3 times.
- Maximum consecutive occurrence: 2 appears 3 times continuously.
So, a normal frequency dictionary solves a different problem. For consecutive occurrence, use the loop or groupby().
8. Special variation: Maximum consecutive ones
If the interviewer specifically asks for the maximum number of consecutive 1s, use this simpler solution:
nums = [1, 1, 0, 1, 1, 1]max_ones = 0current_ones = 0for num in nums:    if num == 1:        current_ones += 1        max_ones = max(max_ones, current_ones)    else:        current_ones = 0print(max_ones)



Output:
3


- Time: \(O(n)\)
- Auxiliary space: \(O(1)\)
This returns the maximum count, not the element itself.
9. Complexity comparison
Method	Time	Auxiliary space	Recommendation
For loop	O(n)	O(1)	Best for interviews
groupby()	O(n)	O(n) worst case	Pythonic alternative
Sliding-window style	O(n)	O(1)	Good alternative
Dictionary frequency	O(n) average	O(n)	Not suitable for consecutive count

Small coding improvement: In Method 3, use nums[1:] only if you are comfortable creating a copy. To keep O(1) auxiliary space, change:
for num in nums[1:]:



to:
for i in range(1, len(nums)):    num = nums[i]



10. Interview questions and answers
Q1. What is consecutive occurrence?

It means the same element appears continuously next to each other.

Q2. What is the difference between frequency and consecutive frequency?

Frequency counts all occurrences. Consecutive frequency counts only adjacent repeated elements.

Q3. Why do we initialize current_count = 1?

Because the first element itself is one occurrence.

Q4. Why do we reset current_count = 1?

When the current element is different from the previous one, a new consecutive group starts.

Q5. Why is the time complexity O(n)?

Because we visit each element only once.

Q6. Why is the space complexity O(1)?

Because we use only a fixed number of variables and do not create another list.

Q7. What happens if two elements have the same maximum consecutive count?

The recommended loop uses > rather than >=, so it returns the element from the first longest group.

Q8. What if the list is empty?

The solution returns None, because there is no element to return.
11. Interviewee explanation
You can say:
I need to find the element that appears the maximum number of times consecutively in a list. I use a current count and a maximum count. I compare each element with the previous element. If both are equal, I increase the current count. Otherwise, I reset it to one. Whenever the current count becomes greater than the maximum count, I update the maximum count and the element. This solution takes O(n) time and O(1) auxiliary space because I traverse the list only once and use a fixed number of variables.

12. Summary
- Problem: Find the element with the longest consecutive occurrence.
- Best interview method: Simple for loop.
- Alternative: itertools.groupby().
- Time complexity: O(n).
- Auxiliary space: O(1) for the loop solution.
- Important: Consecutive occurrence is different from total frequency.
---------------------------------------------