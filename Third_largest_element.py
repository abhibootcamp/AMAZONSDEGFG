'''Given an array of distinct elements. Find the third largest element in it.
Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because it is the 3 largest element in the array A.
Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3'''
class Solution:
    def thirdLargest(self,a, n):
        if n < 3:
            return -1
        first = second = third = 0
        for i in a:
            if i> first:
                third = second
                second = first
                first = i
            elif i> second:
                third = second
                second = i
            elif i>third:
                third = i
        return third
