
# ----------------------------------------------------------------------------------------------

# 🧩 2. Array Declaration and Initialization


# Empty array
# arr = []

# Array with elements
# arr = [1, 2, 3, 4, 5]

# Mixed types (allowed in Python but not recommended for DSA)
# arr = [1, "hello", 3.5]

# --------------------

# ⚙️ 3. Accessing Elements (Indexing)
# Indexes start from 0.

# arr = [10,20,30,40,50]
# print(arr[0])
# print(arr[2])
# print(arr[4])
# print(arr[-1])  # Last element
# print(arr[-2])  # Second last element

# --------------------

# 🔁 4. Traversing an Array
# To process or display each element:

# arr = [10, 20, 30, 40, 50]

# # Using a for loop
# for i in range(len(arr)):
#     print(arr[i])

# # Using a for-each loop
# for i in arr:
#     print(i)


# --------------------

# ✏️ 5. Insertion in Array

arr = [10, 20, 30, 40, 50]

# insert at the end
# arr.append(60)
# print(arr)

# insert at a specific position (index 2)
# arr.insert(2,70)
# print(arr)

# insert at the beginning
# arr.insert(0,5)
# print(arr)


# --------------------

# ❌ 6. Deletion in Array

arr = [10, 20, 30, 40, 50]
# arr.pop()  # removes last element
# arr.pop(1)   # removes element at index 1
# arr.remove(30)  # removes first occurrence of value 30
# arr.clear()  # removes all elements
# del arr  # deletes the entire array
# print(arr)


# --------------------

# 🔍 7. Searching in Array

# arr = [10, 20, 30, 40, 50]

# num = int(input("Enter number to search: "))
# if num in arr:
#     print(f'{num} found at inedx {arr.index(num)}')
# else:
#     print(f'{num} not found in array')

# linear search

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# print(linear_search([5, 10, 15, 20], 25))  


# --------------------

# 🔄 8. Updating Elements

# arr = [10,20,30]
# arr[1] = 25  # Update index 1 to 25
# print(arr)


# --------------------

# 🔢 9. Common Built-in Functions

# | Function        | Description         | Example             |
# | --------------- | ------------------- | ------------------- |
# | `len(arr)`      | length of array     | `len([1,2,3]) → 3`  |
# | `sum(arr)`      | sum of all elements | `sum([1,2,3]) → 6`  |
# | `max(arr)`      | maximum value       | `max([1,2,3]) → 3`  |
# | `min(arr)`      | minimum value       | `min([1,2,3]) → 1`  |
# | `arr.sort()`    | sort ascending      | `[3,1,2] → [1,2,3]` |
# | `arr.reverse()` | reverse order       | `[1,2,3] → [3,2,1]` |



# --------------------


# 🧮 10. Slicing

# arr = [10,20,30,40,50,60,70]

# print(arr[1:5])  # Elements from index 1 to 4-
# print(arr[:4])  # Elements from start to index 3
# print(arr[3:]) # Elements from index 3 to end
# print(arr[::-1]) # Reversed array



# -----------------

# ⏱️ 11. Time Complexity of Operations

# | Operation              | Time Complexity |
# | ---------------------- | --------------- |
# | Access element         | O(1)            |
# | Update element         | O(1)            |
# | Insert at end          | O(1) amortized  |
# | Insert/delete at index | O(n)            |
# | Search element         | O(n)            |
# | Traverse array         | O(n)            |


# ------------------

# 🧩 12. Mini Project Example — Array Rotation

# arr = input("Enter array elements separated by space: ").split()
# arr = [int(x) for x in arr]
# d = int(input("Enter number of rotations: "))

# def rotate_array(arr, d):
#     n = len(arr)
#     # Rotate the array
#     d = d % n  # Handle rotations greater than array size
#     rotated_arr = arr[d:] + arr[:d]
#     return rotated_arr

# rotated_arr = rotate_array(arr, d)

# print("Original Array:", arr)
# print("Rotated Array:", rotated_arr)
