'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''
class Solution:
    # @param A: list of integers
    # @returns an integer
    def solve(self, A):
        A, n = sorted(A), len(A)
        prev, uniform = 0, 1

        if A[-1] == 0:
            return 1

        for i in range(n - 2, -1, -1):
            if A[i] != A[i + 1]:
                different = prev + uniform
                uniform = 1
            else:
                uniform += 1
                different = prev

            if different == A[i]:
                return 1
            prev = different

        return -1

# Ans/Test code
s = Solution()
A = [-4, -2, 0, -1, -6]
s.solve(A)
