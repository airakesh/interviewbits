'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        if A == 0:
            return [1]
        else:
            N = self.solve(A-1)
            return [1] + [N[i] + N[i+1] for i in range(A-1)] + [1]

    # create a triangle of n rows

    def pascalTriangle(self, A):
        triangle = []
        for i in range(A):
            triangle.append(self.solve(i))

        return triangle

s = Solution()
A = 4
print(s.pascalTriangle(A))
