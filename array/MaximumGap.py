'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
'''
# Do not write main() function.
# Do not read input, instead use the arguments to the function.
# Do not print the output, instead return values as specified
class Solution:
    # @params A: a list of integers
    # @returns an integers
        def maximumGap(self, A):
            if not A:
                return -1
            N = len(A)
            leftMin = [0] * N
            rightMax = [0] * N
            leftMin[0] = A[0]
            for i in range(1, N):
                leftMin[i] = min(leftMin[i - 1], A[i])
                rightMax[N - 1] = A[N - 1]
            for i in range(N - 2, -1, -1):
                rightMax[i] = max(rightMax[i + 1], A[i])

            minI = maxJ = 0
            currMax = 0
            while minI < N and maxJ < N:
                if leftMin[minI] <= rightMax[maxJ]:
                    currMax = max(currMax, maxJ - minI)
                    maxJ += 1
                else:
                    minI += 1

            return currMax

# Test cases
# s = Solution()
# A = [3, 5 4 2]
# print(s.maximumGap(A))
