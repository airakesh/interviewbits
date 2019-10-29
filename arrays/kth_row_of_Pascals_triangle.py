'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?
'''
# Do not write main() function.
# Do not read input, instead use the arguments to the function.
# Do not print the output, instead return values as specified

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        else:
            N = self.getRow(A-1)
            return [1] + [N[i] + N[i+1] for i in range(A-1)] + [1]

    def pascalTriangle(self, A):
        triangle = []
        for i in range(A):
            triangle.append(self.getRow(i))
        if A == 0:
            return [1]
        else:
            return str(triangle.pop(-1))
            
# Test cases
# s = Solution()
# A = 0
# A = 4 (For input 4, indexes k are 0 1 2 3)
# print(s.pascalTriangle(A))
