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
            return t

        temp.append(st + 1)
        temp.append(e + 1)

        return temp

# Ans code
s = Solution()
A = '010'
print(s.flip(A))

output: [1, 1]
