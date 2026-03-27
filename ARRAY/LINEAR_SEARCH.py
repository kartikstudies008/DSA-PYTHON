#LINEAR SEARCH 
arr = [4,8,1,6]
target = 1
found = False   #INITIALIZE found TO False; IT WILL BE SET TO True IF THE TARGET IS FOUND IN THE ARRAY

for num in arr:    #ITERATE THROUGH EACH ELEMENT IN THE ARRAY
    if num == target:   #IF THE CURRENT ELEMENT MATCHES THE TARGET VALUE, MARK IT AS FOUND
        found = True
if found:   #AFTER THE LOOP, CHECK WHETHER THE TARGET WAS FOUND AND PRINT THE RESULT
    print("found")    
else:
    print("not found")
