
class Solution():
    """
    Bubble Sort algorithm implementation
    """
    
    def bubbleSort(self, nums):
        # initialize isSwapped as true to enter into first loop
        isSwapped = True
        
        while isSwapped:
            isSwapped = False    
            
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    # swapping two adjecent numbers
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
                    
                    isSwapped = True
                
        return nums


nums = [-9,10,3,1,22,0]
solution = Solution()
result = solution.bubbleSort(nums)

print(result)