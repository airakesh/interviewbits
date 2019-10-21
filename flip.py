'''
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. 
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. 
By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. 
If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting 
L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,
S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we ret

Another example,
If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
'''

import sys

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        t = list(map(str, A))
        temp = []

        for i in range(len(A)):
            if A[i] == '1':
                t[i] = -1
            else:
                t[i] = 1

        ms = me = k = 0
        st = e = sys.maxsize

        for i in range(len(t)):
            if me + t[i] < 0:
                k = i + 1
                me = 0
            else:
                me += t[i]

            if me > ms:
                ms = me
                st = k
                e = i

        if st == sys.maxsize:
            return temp

        temp.append(st + 1)
        temp.append(e + 1)

        return temp

# Ans code
s = Solution()
A = '111'
# A = '010'
print(s.flip(A))
