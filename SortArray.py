from typing import List


class Solution():
    """
    Given an array of integers, sort the arry in ascending orders

    solution: we can implement merge sort algorithm to sort the array in ascending order
    out of Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort; 
    Merge sort has better time complexity than other algorithm O(nLog(n))
    
    Test Case 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]

    Test Case 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    """

    def sortArray(self, nums: List[int]) ->List[int]:
        if len(nums) > 1:
            mid = len(nums)//2
            left_half = nums[:mid]
            right_half = nums[mid:]

            self.sortArray(left_half)
            self.sortArray(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

nums = [5,2,3,1]
solution = Solution()
solution.sortArray(nums)
print(nums)