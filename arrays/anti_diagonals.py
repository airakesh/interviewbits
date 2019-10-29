'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]
'''
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        
        res = [list() for i in range(2 * len(A) - 1)]

        for i in range(len(A)):
            for j in range(len(A)):
                res[i + j].append(A[i][j])

        return res


# Ans/test code
s = Solution()
A = [
    [1, 2, 3],
    [3, 5, 6],
    [6, 8, 9]
]
s.diagonal(A)
