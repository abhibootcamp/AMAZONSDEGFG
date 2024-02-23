'''Given an array arr[] of size N of positive integers which may have duplicates. 
The task is to find the maximum and second maximum from the array, and both of them should be different from each other, so If no second max exists, then the second max will be -1.
Input:
N = 3
arr[] = {2,1,2}
Output: 2 1
Explanation: From the given array 
elements, 2 is the largest and 1 
is the second largest.'''
class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, sizeOfArray, arr):
        first = arr[0]
        second = -1
        for i in arr:
            if i> first:
                second = first
                first = i
            elif i> second and i != first:
                second = i
        return [first, second]
        
