arr = [12,13,14,15,16] #arr --1221118ddTGM6JU55GNE

left = 0
right = len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

    print(arr)

    
