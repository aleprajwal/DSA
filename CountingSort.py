from typing import List


class Solution():
    """
    Python3 implementation of a Counting Sort Algorithm

    Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array. 
    
    Working of Counting Sort

    1. Find out the maximum element (let it be max) from the given array.
    
    2. Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array.
    
    3. Store the count of each element at their respective index in count array
    For example: if the count of element 3 is 2 then, 2 is stored in the 3rd position of count array. If element "5" is not present in the array, then 0 is stored in 5th position.
    
    4. Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array.
    
    5. Find the index of each element of the original array in the count array. This gives the cumulative count. Place the element at the index calculated as shown in figure below.
    
    6. After placing each element at its correct position, decrease its count by one.
   
   
   Counting Sort Algorithm

    countingSort(array, size)
        max <- find largest element in array
        initialize count array with all zeros
        for j <- 0 to size
            find the total count of each unique element and 
            store the count at jth index in count array
        for i <- 1 to max
            find the cumulative sum and store it in count array itself
        for j <- size down to 1
            restore the elements to array
            decrease count of each element restored by 1


    Source: https://www.programiz.com/dsa/counting-sort

    """
    
    def countingSort(self, arr: List[int]) -> List[int]:
        max_num = max(arr)
        count_arr_size = max_num + 1
        arr_size = len(arr)
        
        count_arr = [0] * count_arr_size
        output_arr = [0] * arr_size

        for num in arr: # count of each unique element
            count_arr[num] += 1

        for i in range(1, count_arr_size):  # cumulative sum
            count_arr[i] += count_arr[i-1]

        for num in arr: # sorting number
            sort_index = count_arr[num] - 1
            output_arr[sort_index] = num
            count_arr[num] -= 1

        return output_arr


arr = [4, 2, 2, 8, 3, 3, 6, 5, 5, 1]
solution = Solution()
result = solution.countingSort(arr)
print(result)    
