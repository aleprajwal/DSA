
class Solution:
    """
    Python3 implementation of Merge Sort algorithm
    """

    def mergeSort(self, arr: list()):
        if len(arr) > 1:    # check if length of an array is greater than 1, i.e, if the array contains two or more items proceed to split the array
            mid = len(arr)//2
            left_half_arr = arr[:mid]
            right_half_arr = arr[mid:]
            print(left_half_arr, right_half_arr)
            
            self.mergeSort(left_half_arr)
            self.mergeSort(right_half_arr)

            i = j = k = 0
            while i < len(left_half_arr) and j < len(right_half_arr): # check array out of bound condition 
                if left_half_arr[i] < right_half_arr[j]:
                    arr[k] = left_half_arr[i]
                    i += 1
                
                else:
                    arr[k] = right_half_arr[j]
                    j += 1
                
                k += 1

            while i < len(left_half_arr):
                arr[k] = left_half_arr[i]
                i += 1
                k += 1
            
            while j < len(right_half_arr):
                arr[k] = right_half_arr[j]
                j += 1
                k += 1


if __name__ == "__main__":
    arr = [4,3,5,7,6,9,8,2]
    solution = Solution()
    solution.mergeSort(arr)
    print(arr)