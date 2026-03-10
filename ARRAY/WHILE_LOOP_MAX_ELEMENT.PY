# MAXIMUM ELEMENT FIND USING WHILE LOOP !

arr = [4,1,8,6]
maximum = arr[0]
i = 0

while i < len(arr):
    if arr[i] > maximum:
        maximum = arr[i]
    i+=1
print(maximum)

