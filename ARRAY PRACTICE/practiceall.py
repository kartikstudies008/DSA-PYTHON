arr = [10,20,30,40,50] # ARRAY CREATED
print(arr)


# EACH ELEMENT HAS ITS INDEX 

print(arr[1])
print(arr[-2])

#SWAP FIRST AND LAST ARRAY 

arr = [1,2,3,4]

left = 0 
right = len(arr)-1

while left < right :
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)

#SUM OF ALL ELEMENTS IN AN ARRAY    #FOR LOOP 

arr =[2,4,6,8]
total = 0

for num in arr:
    total = total + num 
print(total)

#SUM OF ALL ELEMENTS IN AN ARRAY    #WHILE LOOP 

arr1 =[2,4,6,7]
total = 0 
i = 0

while i < len(arr1):
    total = total + arr1[i]
    i += 1
print(total)

#FIND MAX ELEM OF AN ARRAY  #FOR LOOP 
arr2 = [3,5,1,8,2]

max = arr2[0]

for num in arr2:
    if num > max:
        max = num
print(max)

#FIND MAX ELEM OF AN ARRAY  #WHILE LOOP 

arr3 = [3,1,9,15]

max = arr3[0]
i = 0

while i < len(arr3):
    if arr3[i] > max:
        max = arr3[i]
    i += 1
print(max)                #ADD ON


