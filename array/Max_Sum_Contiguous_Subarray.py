class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


# Answer code
s = Solution()
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(A))
