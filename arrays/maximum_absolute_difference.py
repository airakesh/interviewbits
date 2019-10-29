'''
You are given an array of N integers, A1, A2 ,…, AN. 
Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
   def maxArr(self, A):
        self.A = A
        max1 = -1000000000
        min1 = +1000000000
        max2 = -999999999
        min2 = +1000000001
        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)

        return max(max1 - min1, max2 - min2)

# Ans code (Test case)
s = Solution()
arr = [1, 3, -1]
# arr = [-70, -64, -6, -56, 64, 61, -57, 16, 48, -98] 
print(s.maxArr(arr))
