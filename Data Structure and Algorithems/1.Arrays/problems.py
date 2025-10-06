# 1.Find the maximum element in an array.
# arr = [21, 54, 8, 46, 12 ,45]
# print(f'Mximum element in array is: {max(arr)} at arr[{arr.index(max(arr))}]')



# 2.Find the minimum element in an array.
# arr = [21, 54, 8, 46, 12 ,45]
# print(f'Mximum element in array is: {min(arr)} at arr[{arr.index(min(arr))}]')



# 3.Calculate the sum of all elements.
# arr = [21, 54, 8, 46, 12 ,45]
# print(sum(arr) / len(arr)) #one mliner solution
# sum = 0
# for num in arr:
#     sum += num
# print(sum)



# 4.Find the average of array elements.
# arr = [21, 54, 8, 46, 12 ,45]
# avg = 0
# for i in arr:
#     avg += i
# print(avg/len(arr))



# 5.Count even and odd numbers.
# arr = [21, 54, 8, 46, 12 ,45]
# even_count = 0
# odd_count = 0
# for i in arr:
#     if i %2 == 0:
#         even_count+= 1
#     else:
#         odd_count += 1
# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)
# ------
# another method
# arr = [21, 54, 8, 46, 12 ,45]
# evens = [i for i in arr if i %2 ==0]
# odds = [i for i in arr if i %2 !=0]
# print(f'Even numbers: {len(evens)} : {evens}')
# print(f'Odd numbers: {len(odds)} : {odds}')


# 6.Find the second largest element.
# arr = [21, 54, 8, 46, 12 ,45]
# arr = list(set(arr))  # Remove duplicates
# arr.sort()
# print(arr)
# print(arr[::-1][1])


# 7.Check if an array is sorted or not.
# arr = [21, 54, 8, 46, 12 ,45]
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         print("Array is not sorted")
#         break
# else:
#     print("Array is sorted")    

# # another method
# if arr == sorted(arr):
#     print("Array is sorted")
# else:
#     arr.sort()
#     print(arr)
#     print("Array is not sorted")


# 8.Reverse an array (without using reverse function).
# arr = [21, 54, 8, 46, 12 ,45]
# reversed_arr = []
# for i in range(len(arr)-1, -1, -1):
#     reversed_arr.append(arr[i])
# print(reversed_arr)
# # another method
# reversed_arr = []   
# for i in arr:
#     reversed_arr = [i] + reversed_arr
# print(reversed_arr)
# # another method    
# reversed_arr = []   
# for i in arr:
#     reversed_arr.insert(0, i)
# print(reversed_arr)



# 9.Find the index of a given element.
# arr = [21, 54, 8, 46, 12 ,45]
# element = 46
# for i in range(len(arr)):
#     if arr[i] == element:
#         print(f'Element {element} found at index {i}')
#         break



# 10.Count frequency of each element.
# arr = [21, 54, 8, 46, 12 ,45, 21, 54, 8]
# frequency = {}
# for i in arr:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)


# extra. Remove duplicates from an array.
# arr = [21, 54, 8, 46, 12 ,45, 21, 54, 8]
# unique_arr = []
# for i in arr:
#     if i not in unique_arr:
#         unique_arr.append(i)    
# print(unique_arr)



# -----------------------🟡 Intermediate Level (Patterns & Logic)


# 11.Move all zeros to the end.
# arr = [0, 1, 0, 3, 12]
# non_zero_arr = [i for i in arr if i != 0]
# zero_count = arr.count(0)
# result = non_zero_arr + [0]*zero_count
# print(result)
# another method
# arr = [0, 1, 0, 3, 12]
# result = []
# for i in arr: 
#     if i != 0:
#         result.append(i)
# for i in arr:
#     if i == 0:    
#         result.append(i)
# print(result)



# 12.Rotate an array by k steps.
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)  # In case k is greater than array length    
rotated_arr = arr[-k:] + arr[:-k]
print(rotated_arr)