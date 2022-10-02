def FindMissingElement(arr):
    low = 0 #Initialize low to 0
    high = len(arr)-1   #Initialize high to lenght of arr-1
    
    if arr[0] != 1: #If the first element is not 1 then 1 is the missing element return 1
        return 1
    
    if arr[-1] == len(arr): #If the last element is equal to the length of arr then the last element is missing return lenght of arr+!
        return len(arr)+1
    
    while low+1 != high:    #Continue till low+1 is not equal to high
        mid = low + (high-low) //2  #Integer overflow
        
        if (arr[mid]-mid) == 1: #If the difference between the element in the middle and mid is 1 move the low to mid
            low = mid
        else:   #Else move the high to mid
            high = mid  
    return arr[low]+1   #Return low+1 as the missing element
    
    
    
    
    
    
    
    
print(FindMissingElement([1,2,3,4,6]))