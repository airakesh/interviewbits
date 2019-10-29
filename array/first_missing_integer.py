'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''
# Do not write main() function.
# Do not read input, instead use the arguments to the function.
# Do not print the output, instead return values as specified
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        if length == 0:
            return 1

        count = {}
        for i in range(length):
            count[A[i]] = True

        maxElement = max(A)
        for i in range(1, maxElement):
            if not count.get(i):
                return i

        if maxElement < 0:
            return 1
        return maxElement + 1
