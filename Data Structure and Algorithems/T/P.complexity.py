

# -------------------------------------------------------------------------------------





# 🧠 1. What is Time Complexity?

# Time complexity tells us how fast an algorithm runs as the input size grows.

# It’s not about how many seconds it takes, but how the number of operations increases with input size.

# Think of it as:

# “If I double the input size, how much slower does my code get?”

# 🧮 2. Why We Use It

# Instead of measuring actual time (which depends on CPU, language, etc.), we measure growth rate — how runtime increases with input size n.

# For example:

# Input Size (n)	Operations (f(n))	Growth Type
# 10	10	Linear
# 100	100	Linear
# 10	100	Quadratic
# 🏁 3. Big O Notation

# Big O describes the upper bound (worst case) of time complexity.
# It helps us understand how the runtime grows as the input grows.

# # Common Big O complexities:
# | Big O          | Name             | Example                                  |
# | -------------- | ---------------- | ---------------------------------------- |
# | **O(1)**       | Constant Time    | Accessing an element in a list: `arr[0]` |
# | **O(log n)**   | Logarithmic Time | Binary Search                            |
# | **O(n)**       | Linear Time      | Loop through a list                      |
# | **O(n log n)** | Log-linear       | Merge Sort, Quick Sort (avg)             |
# | **O(n²)**      | Quadratic        | Nested loops                             |
# | **O(2ⁿ)**      | Exponential      | Recursive Fibonacci                      |
# | **O(n!)**      | Factorial        | Permutation generation                   |



# 🧩 4. Examples in Python
# 🟢 Example 1 — O(1): Constant Time
# def get_first_element(arr):
#     return arr[0]  # Always one operation, regardless of size

# 🔵 Example 2 — O(n): Linear Time
# def print_all(arr):
#     for i in arr:
#         print(i)


# → Operations grow directly with n.

# 🟠 Example 3 — O(n²): Quadratic Time
# def print_pairs(arr):
#     for i in arr:
#         for j in arr:
#             print(i, j)


# → Two nested loops → n * n = n² operations.

# 🔴 Example 4 — O(log n): Logarithmic Time
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


# → Each step cuts the array in half — grows logarithmically.

# ⌛ 5. Visual Intuition
# n	O(1)	O(log n)	O(n)	O(n²)
# 10	1	3	10	100
# 100	1	6	100	10,000
# 1000	1	10	1000	1,000,000

# Notice how O(n²) explodes fast 🚀 — that’s why efficient algorithms matter.

# 🧮 6. Quick Exercise

# Predict the time complexity for each:

# 1️⃣

# for i in range(n):
#     print(i)


# 2️⃣

# for i in range(n):
#     for j in range(10):
#         print(i, j)


# 3️⃣

# for i in range(n):
#     for j in range(n):
#         print(i, j)


# 👉 Answers:
# 1️⃣ O(n)
# 2️⃣ O(n) (since 10 is constant → O(10n) → O(n))
# 3️⃣ O(n²)



# ------------------------------------------------------------------------------------


# 🧩 7. Space Complexity

# Similar concept — but measures memory usage.

# Examples:

# Operation	Space Complexity
# arr = [1,2,3]	O(1)
# arr = [i for i in range(n)]	O(n)
# Recursive calls	O(n) (stack memory)
# 🧭 Summary
# Complexity	Example	Description
# O(1)	arr[0]	Constant
# O(log n)	Binary Search	Divide & conquer
# O(n)	Single loop	Linear
# O(n²)	Nested loops	Quadratic
# O(2ⁿ)	Recursion	Exponential


# 🧠 Part 1 — Identify the Time Complexity
# Q1.
# def func1(arr):
#     print(arr[0])


# 👉 What’s the time complexity?

# Q2.
# def func2(arr):
#     for i in arr:
#         print(i)


# 👉 What’s the time complexity?

# Q3.
# def func3(arr):
#     for i in arr:
#         for j in arr:
#             print(i, j)


# 👉 What’s the time complexity?

# Q4.
# def func4(n):
#     i = 1
#     while i < n:
#         print(i)
#         i *= 2


# 👉 What’s the time complexity?

# Q5.
# def func5(arr):
#     for i in arr:
#         for j in range(10):
#             print(i, j)


# 👉 What’s the time complexity?

# Q6.
# def func6(n):
#     for i in range(n):
#         for j in range(i, n):
#             print(i, j)


# 👉 What’s the time complexity?

# Q7.
# def func7(arr):
#     for i in range(len(arr)):
#         print(arr[i])
#         if arr[i] == 5:
#             break


# 👉 What’s the time complexity (best and worst case)?

# Q8.
# def func8(arr):
#     if len(arr) == 0:
#         return None
#     print(arr[len(arr)//2])


# 👉 What’s the time complexity?

# Q9.
# def func9(n):
#     for i in range(n):
#         for j in range(1000):
#             print(i, j)


# 👉 What’s the time complexity?

# Q10.
# def func10(n):
#     if n <= 1:
#         return 1
#     return func10(n-1) + func10(n-2)


# 👉 What’s the time complexity?

# 🧩 Part 2 — Mix of Space Complexity
# Q11.
# def create_list(n):
#     return [i for i in range(n)]


# 👉 What’s the space complexity?

# Q12.
# def recursive_sum(n):
#     if n == 0:
#         return 0
#     return n + recursive_sum(n-1)


# 👉 What’s the space complexity?

# | No.  | Complexity                      | Explanation                               |
# | ---- | ------------------------------- | ----------------------------------------- |
# | 1️⃣  | **O(1)**                        | Only one operation                        |
# | 2️⃣  | **O(n)**                        | One loop → linear                         |
# | 3️⃣  | **O(n²)**                       | Two nested loops                          |
# | 4️⃣  | **O(log n)**                    | i doubles each time (1,2,4,8,...)         |
# | 5️⃣  | **O(n)**                        | Inner loop runs constant 10 times         |
# | 6️⃣  | **O(n²)**                       | Triangular pattern → n(n+1)/2 ≈ n²        |
# | 7️⃣  | **Best: O(1)**, **Worst: O(n)** | If 5 is first element vs last             |
# | 8️⃣  | **O(1)**                        | Constant access (middle element)          |
# | 9️⃣  | **O(n)**                        | 1000 is constant → O(1000n) → O(n)        |
# | 🔟   | **O(2ⁿ)**                       | Recursive Fibonacci (two calls per level) |
# | 11️⃣ | **O(n)**                        | List stores n elements                    |
# | 12️⃣ | **O(n)**                        | Recursion depth = n (stack memory)        |
