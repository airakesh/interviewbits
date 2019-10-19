''' Array Probem: Min Steps in Infinite Grid '''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        min_number_of_steps = 0
        for i in range(1, len(A)):
             min_number_of_steps += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))

        return  min_number_of_steps


'''
Answer code of the problem
'''
s = Solution()
A = [0, 1, 1]
B = [0, 1, 2]

print(s.coverPoints(A, B))
