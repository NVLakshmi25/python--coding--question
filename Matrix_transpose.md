# Python Program to Find the Transpose of a Matrix

## 1. Problem Statement

Given a matrix, convert its rows into columns and its columns into rows.

In simple words, transpose means swapping rows and columns.

**Example:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

**Expected Output:**

```python
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

**Explanation:**

Original matrix:

```text
1  2  3
4  5  6
```

After transpose:

```text
1  4
2  5
3  6
```

Notice:
- First row `[1, 2, 3]` becomes the first column.
- Second row `[4, 5, 6]` becomes the second column.

**Important:** A 2 × 3 matrix becomes a 3 × 2 matrix.

---

## 2. Definition, Purpose and Uses

**Definition:** Matrix transpose means converting rows into columns and columns into rows.

**Why:** To change the arrangement of matrix elements without changing their values.

**Purpose:** To rearrange matrix data for calculations and processing.

**Where:**
- Mathematical calculations.
- Data science and machine learning.
- Tables and spreadsheets.
- Image processing.

**When:** When we need to convert rows into columns or columns into rows.

---

## 3. Important Python Syntax

| Syntax | Purpose |
|---|---|
| `len(matrix)` | Returns the number of rows |
| `len(matrix[0])` | Returns the number of columns |
| `range()` | Generates indexes |
| Nested loops | Access rows and columns |
| `append()` | Adds elements to a list |
| `zip()` | Groups corresponding elements |
| `*matrix` | Unpacks matrix rows |
| `.T` | Transposes a NumPy array |

---

## 4. Method 1: Using Nested For Loops (Recommended for Interviews)

This method helps you understand the actual logic behind matrix transposition.

### Code

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

transposed = []

for i in range(cols):
    new_row = []

    for j in range(rows):
        new_row.append(matrix[j][i])

    transposed.append(new_row)

print(transposed)
```

**Output:**

```python
[[1, 4], [2, 5], [3, 6]]
```

### How does it work?

1. `rows` stores the number of rows (2).
2. `cols` stores the number of columns (3).
3. Create an empty list called `transposed`.
4. The outer loop iterates through the original column indexes.
5. The inner loop accesses elements from the original rows.
6. `matrix[j][i]` gets the element at the required position.
7. `append()` adds the elements to the new row.
8. Finally, append the new row to the transposed matrix.

### Dry Run (Tracing)

Original matrix:

```text
1  2  3
4  5  6
```

| Iteration | i | j | matrix[j][i] | New row |
|---|---:|---:|---:|---|
| 1 | 0 | 0 | 1 | [1] |
| 2 | 0 | 1 | 4 | [1, 4] |
| 3 | 1 | 0 | 2 | [2] |
| 4 | 1 | 1 | 5 | [2, 5] |
| 5 | 2 | 0 | 3 | [3] |
| 6 | 2 | 1 | 6 | [3, 6] |

After every inner loop, the new row is added to the result.

**Final result:**

```python
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

### Important Syntax

```python
matrix[j][i]
```

- `j` represents the original row index.
- `i` represents the original column index.
- We use `matrix[j][i]` because we are swapping the row and column positions.

### Time and Space Complexity

Let:
- r = number of rows.
- c = number of columns.

**Time Complexity: O(r × c)**

Why? The outer loop runs c times and the inner loop runs r times. Therefore, the total operations are c × r.

**Auxiliary Space Complexity: O(r × c)**

Why? We create a new matrix containing all r × c elements.

---

## 5. Method 2: Using zip() and Unpacking (*)

This is the shortest and cleanest built-in Python method.

### Code

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = [list(row) for row in zip(*matrix)]

print(transposed)
```

**Output:**

```python
[[1, 4], [2, 5], [3, 6]]
```

### Definition

`zip()` combines elements from multiple iterables based on their positions.

`*matrix` unpacks the rows of the matrix and passes them separately to `zip()`.

### How does it work?

1. `*matrix` unpacks the two rows.
2. `zip()` groups elements at matching positions.
3. First group: `(1, 4)`.
4. Second group: `(2, 5)`.
5. Third group: `(3, 6)`.
6. `list(row)` converts each tuple into a list.
7. List comprehension creates the final matrix.

### Dry Run

```python
zip(*matrix)
```

Conceptually produces:

```python
(1, 4)
(2, 5)
(3, 6)
```

After converting each tuple into a list:

| Group | Result |
|---|---|
| (1, 4) | [1, 4] |
| (2, 5) | [2, 5] |
| (3, 6) | [3, 6] |

**Final Output:**

```python
[[1, 4], [2, 5], [3, 6]]
```

### Important Syntax

```python
zip(*matrix)
```

- `zip()` groups corresponding elements.
- `*` unpacks the matrix rows.
- `list()` converts tuples into lists.

**Complexity:**

- Time: O(r × c) – Every matrix element is processed.
- Auxiliary Space: O(r × c) – A new transposed matrix is created.

**When to use:** When you want short, clean and Pythonic code.

---

## 6. Method 3: Using List Comprehension

This method uses indexes and list comprehension to create the transposed matrix.

### Code

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = [
    [matrix[j][i] for j in range(len(matrix))]
    for i in range(len(matrix[0]))
]

print(transposed)
```

**Output:**

```python
[[1, 4], [2, 5], [3, 6]]
```

### How does it work?

1. `len(matrix)` returns the number of rows (2).
2. `len(matrix[0])` returns the number of columns (3).
3. The outer comprehension iterates through column indexes.
4. The inner comprehension accesses elements from each row.
5. `matrix[j][i]` swaps the positions.
6. The result is stored in a new matrix.

### Dry Run

| Outer index (i) | Inner index (j) | Values collected |
|---:|---|---|
| 0 | 0, 1 | [1, 4] |
| 1 | 0, 1 | [2, 5] |
| 2 | 0, 1 | [3, 6] |

**Final Output:** `[[1, 4], [2, 5], [3, 6]]`

### Syntax

```python
[
    [expression for inner_variable in iterable]
    for outer_variable in iterable
]
```

**Complexity:**

- Time: O(r × c) – Every element is accessed once.
- Auxiliary Space: O(r × c) – A new matrix is created.

**When to use:** When you understand list comprehension and want a compact solution without `zip()`.

---

## 7. Method 4: Using NumPy

NumPy is useful for mathematical calculations and large numerical datasets.

### Code

```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transposed = matrix.T

print(transposed)
```

**Output:**

```text
[[1 4]
 [2 5]
 [3 6]]
```

### How does it work?

1. `np.array()` converts the matrix into a NumPy array.
2. `.T` swaps rows and columns.
3. The result is a transposed NumPy array.

### Dry Run

| Original row | Transposed column |
|---|---|
| [1, 2, 3] | [1, 2, 3] |
| [4, 5, 6] | [4, 5, 6] |

The original rows become the columns in the output.

**Complexity:**

- Time: O(1) for NumPy's `.T` view creation in the usual case.
- Additional Space: O(1) for the transpose view itself.

**Important:** NumPy transpose generally returns a view with changed strides, rather than copying all elements.

**When to use:** Data science, machine learning and numerical calculations.

---

## 8. Method 5: In-Place Transpose (Only for Square Matrices)

This method swaps elements across the main diagonal without creating another matrix.

### Code

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
```

**Output:**

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

### How does it work?

1. Get the matrix size using `len(matrix)`.
2. Use two nested loops.
3. Start the inner loop at `i + 1` to avoid swapping an element with itself or swapping a pair twice.
4. Swap `matrix[i][j]` and `matrix[j][i]`.
5. The original matrix is updated directly.

### Dry Run

Original matrix:

```text
1  2  3
4  5  6
7  8  9
```

| i | j | Swap | Matrix changes |
|---:|---:|---|---|
| 0 | 1 | 2 ↔ 4 | First row becomes [1, 4, 3] |
| 0 | 2 | 3 ↔ 7 | First row becomes [1, 4, 7] |
| 1 | 2 | 6 ↔ 8 | Second row becomes [2, 5, 8] |

**Final Output:**

```text
1  4  7
2  5  8
3  6  9
```

**Complexity:**

- Time: O(n²) – We visit each pair above the diagonal once.
- Auxiliary Space: O(1) – We swap elements in the original matrix without creating another matrix.

**When to use:** When the interviewer specifically asks for an in-place transpose of a square matrix.

---

## 9. Method Comparison

| Method | Time | Auxiliary Space | Best Use |
|---|---|---|---|
| Nested loops | O(r × c) | O(r × c) | Coding interviews |
| zip() | O(r × c) | O(r × c) | Clean Python code |
| List comprehension | O(r × c) | O(r × c) | Compact solution |
| NumPy `.T` | O(1)* | O(1)* | Numerical computing |
| In-place | O(n²) | O(1) | Square matrix |

*NumPy figures refer to creating a transpose view, not copying the entire array.*

---

## 10. Which Method Should You Follow in Interviews?

**My recommendation:**

1. **First priority: Nested loops** – Shows your understanding of matrix indexes and problem-solving logic.
2. **Second priority: zip()** – Shows your knowledge of Python built-in functions.
3. **Third priority: List comprehension** – Shows your ability to write compact Python code.
4. Learn NumPy and in-place transpose as additional methods.

**Recruiter's point of view:**

The interviewer generally wants to understand:
- Can you identify rows and columns?
- Can you use nested loops?
- Can you access matrix elements using indexes?
- Can you explain how the output is formed?
- Can you calculate time and space complexity?

For a fresher interview, start with nested loops. It makes your logic easier to explain.

---

## 11. Important Interview Questions and Answers

**Q1. What is matrix transpose?**

Matrix transpose means converting rows into columns and columns into rows.

**Q2. What happens to the dimensions after transpose?**

An r × c matrix becomes a c × r matrix.

**Q3. Why do we use nested loops?**

To access every element using its row and column indexes.

**Q4. What does `matrix[i][j]` mean?**

It accesses the element at row i and column j.

**Q5. What is the purpose of `zip(*matrix)`?**

It groups elements from different rows at the same positions.

**Q6. What is the use of the `*` operator in `zip(*matrix)`?**

It unpacks the matrix rows and passes them separately to `zip()`.

**Q7. Can we transpose a rectangular matrix?**

Yes. Nested loops, zip() and list comprehension support rectangular matrices.

**Q8. Can we use in-place transpose for rectangular matrices?**

The simple diagonal-swapping method works only for square matrices.

**Q9. What is the time complexity of matrix transpose?**

O(r × c), because every element is processed once when creating a new transposed matrix.

**Q10. What is the auxiliary space complexity?**

O(r × c), because a new matrix is created to store all elements.

---

## 12. Interviewee Explanation (Natural English)

"First, I calculate the number of rows and columns in the matrix. Then I create an empty result matrix. I use nested for loops to access the elements. The outer loop iterates through the original column indexes, and the inner loop iterates through the original row indexes. I use matrix[j][i] to swap the row and column positions. Finally, I store the elements in a new matrix and print the result.

The time complexity is O(r × c), and the auxiliary space complexity is also O(r × c), because I create a new matrix."

---

## 13. What, Why, How, Where and When – Quick Revision

| Question | Simple Answer |
|---|---|
| What? | Swapping rows and columns of a matrix. |
| Why? | To rearrange matrix elements. |
| Purpose? | To convert rows into columns. |
| How? | Using nested loops, zip() or list comprehension. |
| Where? | Mathematics, data science and image processing. |
| When? | When we need to change the row-column arrangement. |

---

## 14. Final Summary

- **Problem:** Convert rows into columns and columns into rows.
- **Recommended interview method:** Nested for loops.
- **Pythonic method:** `zip(*matrix)`.
- **Original dimensions:** 2 × 3.
- **Transposed dimensions:** 3 × 2.
- **Expected output:** `[[1, 4], [2, 5], [3, 6]]`.
- **Time Complexity:** O(r × c) for a newly constructed matrix.
- **Auxiliary Space Complexity:** O(r × c) for a newly constructed matrix.

**Remember:** Practise nested loops first. Understand why we use `matrix[j][i]` instead of `matrix[i][j]`. This is the most important logic in this problem.

One important interview tip: Don't memorise only the code. Understand this one concept:
- Original matrix: matrix[i][j]
- Transposed matrix position: transposed[j][i]