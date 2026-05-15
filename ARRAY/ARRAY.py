#PRINTING ARRAY 
arr = [10,20,30,40]   #ARR ---1---454
print(arr)    #arr 4 44

#INDEXING 
print(arr[0])

#NEGATIVE INDEXING 
print(arr[-1])

#SLICING
print(arr[1:3])

#ADD ELEMENT 
arr.append(50)
print(arr)

#REMOVE ELEMENT
arr.remove(20)
print(arr)

#POP
arr.pop()
print(arr)

#POP INDEXING 
arr.pop(1)
print(arr)

#INSERT ELEMENT
arr.insert(0,25)  #INSERT 25 AT INDEX 0`
print(arr)

#TRAVERSING AN ARRAY
for num in arr:
     print(num)

#FIND MAX ELEMENT 
arr2 = [5,10,15,20]
maximum = arr2[0]       #INITIALIZE THE MAXIMUM VARIABLE TO THE FIRST ELEMENT OF THE ARRAY

for num in arr2:          #ITERATE THROUGH THE ARRAY AND CHECK IF THE CURRENT NUMBER IS GREATER THAN THE MAXIMUM
     if num > maximum:
          maximum = num
print("Maximum element:", maximum)

#FIND MIN ELEMENT
arr3 = [5,10,2,23]
minimum = arr3[0]       #INITIALIZE THE MINIMUM VARIABLE TO THE FIRST ELEMENT OF THE ARRAY
for num in arr3:    #ITERATE THROUGH THE ARRAY AND CHECK IF THE CURRENT NUMBER IS LESS THAN THE MINIMUM 
     if num < minimum:  #IF THE CURRENT NUMBER IS LESS THAN THE MINIMUM, UPDATE THE MINIMUM TO THE CURRENT NUMBER
          minimum = num   #AFTER THE LOOP, THE MINIMUM VARIABLE WILL HOLD THE MINIMUM ELEMENT IN THE ARRAY
print("Minimum element:", minimum)


