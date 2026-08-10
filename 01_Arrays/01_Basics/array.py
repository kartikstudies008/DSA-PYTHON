# ============================================================
# TOPIC: 01_Arrays / 01_Basics - 1D Array Fundamentals
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Demonstrate essential 1D array operations: element traversal, finding minimum
#    and maximum values, calculating sum and average, counting even numbers,
#    reversing an array using two pointers, and finding the second largest element.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Iterative Traversal: Scanning elements sequentially using loop indices.
#    - Two Pointers: Reversing elements in-place by swapping from both ends (left & right).
#    - Single-Pass Tracking: Maintaining running state variables (e.g., max and second largest) simultaneously.
#
# 💡 APPROACH:
#    1. Traversal: Loop from index 0 to len(arr)-1 using range() or direct element access.
#    2. Min/Max: Initialize max = arr[0], iterate and update if current element is larger.
#    3. Sum & Average: Accumulate total sum in a loop, then divide by len(arr).
#    4. Array Reversal: Set left = 0, right = len(arr)-1. Swap arr[left] and arr[right], move pointers inward.
#    5. Second Largest: Maintain largest (l) and second_largest (s). Update s = l and l = num when a new max is found.
#
# 📊 EXAMPLE:
#    Input:  arr = [10, 80, 40, 90, 30]
#    Output: Largest: 90, Second largest: 80
#
# 🔄 DRY RUN (Second Largest with [10, 80, 40, 90, 30]):
#    Initial: l = 10, s = -1
#    i = 1 (val 80): 80 > 10 -> s = 10, l = 80
#    i = 2 (val 40): 40 < 80, but 40 > 10 -> s = 40, l = 80
#    i = 3 (val 90): 90 > 80 -> s = 80, l = 90
#    i = 4 (val 30): 30 < 80 -> no change
#    Final: Largest = 90, Second largest = 80
#
# ⏱️  TIME COMPLEXITY:  O(N) — Linear pass through the array for each operation.
# 🗂️  SPACE COMPLEXITY: O(1) — Constant extra space used for state variables.
#
# 🎯 INTERVIEW POINTS:
#    - Finding second largest in O(N) single pass is preferred over sorting O(N log N).
#    - Two-pointer array reversal is optimal (O(N) time, O(1) auxiliary space).
#
# ⚠️  COMMON MISTAKES:
#    - Forgetting to update second largest when a new max is found.
#    - Out-of-bounds errors when swapping pointers during reversal.
#
# ============================================================

# arr = [12,25,37,49,51,60]

# for i in range (len(arr)):
#  print(arr[i])



# arr = []
# size = int(input("Enter size: "))

# for i in range(size):
#     num  = int(input("Enter elements: "))
#     arr.append(num)

# print("Arr elements are: ")
# for i in range(len(arr)):
#     print(arr[i])

# arr=[]
# size = int(input("Enter size: "))

# for i in range(size):
#     num = int(input("Enter elements: "))
#     arr.append(num)

# print("ARR ELEM ARE : ")
# for i in range (len(arr)):
#     print(arr[i])

# print("First element: ",arr[0])
# print("Last element: ",arr[-1])


# arr = [12,25,56,112,117,200,5,50]

# max = arr[0]

# for i in range (1,len(arr)):
#     if arr[i] > max:
#         max = arr[i]
    
# print("Max elem is : ",max)
    
# arr = [12,25,56,112,117,200,5,50]

# min = arr[0]

# for i in range (1,len(arr)):
#     if arr[i] < min:
#         min = arr[i]

# print("min element: ",min)

# arr=[]
# size = int(input("enter size :"))

# for i in range (size):
#     num = int(input("enter elem :"))
#     arr.append(num)


# max = arr[0]

# for i in range (1, len(arr)):
#     if arr[i] > max:
#         max = arr[i]

# print("max elem: ",max)

# arr=[]
# size = int(input("enter size: "))

# for i in range (size):
#     num = int(input("enter no. : "))
#     arr.append(num)

# print("elements are : ")

# for i in range (len(arr)):
#     print(arr[i])

# print("max elem :",arr[-1])
# print("min elem :",arr[0])


#SUMM ALL ARR

# arr = [10,20,30,40]

# sum = arr[0]

# for i in range (len(arr)):
#     num = sum + arr[i]
#     sum  = num
#     print(sum)
     
# arr = []
# sum = 0

# size = int(input("enter size: "))

# for i in range(size):
#     num = int(input("enter no.: "))
#     arr.append(num)


# for i in range (len(arr)):
#     num = sum + arr[i]
#     sum = num

# print(sum)



# avg of all elem 

# arr = [10,20,30,40]

# sum = 0
# size = len(arr)

# for i in range (len(arr)):
#     total = arr[i] + sum
#     sum = total

# print("Sum : ",sum)

# avg = sum / size

# print("average is: ",avg)


# arr = []
# sum = 0

# size = int(input("enter size: "))

# for i in range(size):
#     num = int(input("enter no.: "))
#     arr.append(num)


# for i in range (len(arr)):
#     sum = arr[i] + sum

# avg = sum / len(arr)

# print(avg)


# count even no. 

# arr = [10,15,20,25,30]
# count = 0

# for i in range (len(arr)):
    
#     if arr[i] % 2 == 0:
#         count += 1

# print(count) 
    

# arr = []

# size = int(input("enter size: "))

# for i in range (size):
#     num = int(input("enter num: "))
#     arr.append(num)


# count = 0

# for i in range (len(arr)):
#     if arr[i] % 2 == 0:
#         count += 1

# print(count)


# REVERSE ARRAY !

# arr = [10,20,30,40,50]

# for i in range (4,-1,-1):

#     print(arr[i])
# print(len(arr))

# using pointers 

# arr = [50,2,45,78,5]

# left = 0
# right = len(arr) -1

# while left < right :
#     arr[left], arr[right] = arr[right],arr[left]

#     left += 1
#     right -= 1

# print(arr)

#LARGEST NO >

# arr = [10,80,40,90,30]

# max = arr[0]

# for i in range(1,len(arr)):
#     if arr[i] > max :
#         max = arr[i]

# print(max)
    

# PRACTICE 

# arr = []
# size = int(input("enter size: "))

# for i in range (size):
#     num = int(input("enter elem: "))
#     arr.append(num)

# print(arr)

# l = arr[0]
# s = -1

# for i in range (1,len(arr)):
#     if arr[i] > l:
#         s = l
#         l = arr[i]

#     elif arr[i] > s:
#         s = arr[i]

# print("Largest: ",l)
# print("Second largest: ",s)
