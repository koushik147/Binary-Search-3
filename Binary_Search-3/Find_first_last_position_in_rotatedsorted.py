#Time_Complexity: O(log n)
#Space_Complexity: 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        first = self.binarySearch(True) #By setting first to True the binary search is performed on the left side of the array to find the first position of the target
        last = self.binarySearch(False) #By setting last to False the binary search is performed on the right side of the array to find the last position of the target
        return [first, last]    #Returning first and last will give the first and last positions of the target
        
    def binarySearch(self,leftFlag):    #binarySearch function to perform Binary search over the array
        low = 0 #Initializing low to 0
        high = len(self.nums)-1 #Initializing high to the length of nums -1
        index = -1  #Initializing index to -1, it'll be changed to the index of the target once the target is found

        while low <= high:  #Loop over the array till low becomes less than or equal to high
            mid = low+(high-low)//2 #Calculating mid by dividing low+high //2

            if self.nums[mid] == self.target:   #If the element in mid index is equal to the target then change index value to mid
                index = mid

                if leftFlag:    #If leftFlag is true then the binarySearch is done for the left side of the array
                    high = mid-1    #Change the high to mid-1
                else:
                    low = mid+1 #Else change the low to mid+!

            elif self.nums[mid] < self.target:  #Else if the element in the mid is less than the target change low to mid+1
                low = mid+1
            else:
                high = mid-1    #Else the element is greater than the target change high to mid-1
                
                    
                    
        return index    #Return index