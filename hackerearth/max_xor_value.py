class Solution:
    # @param A : list of integers
    # @return an integer
 #   def findMinXor(self, A):
 #       A.sort()
 #       return min(map(lambda i: A[i] ^ A[i + 1], range(len(A) - 1)))

    def findMaxXor(self, A):
        ans = mask = 0

        for i in range(len(A))[::-1]:
            mask += 1 << i
            prefixSet = set([n & mask for n in A])
            temp = ans | 1 << i
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    ans = temp
                    break
            return ans

# test case
s = Solution()
A = [0, 4, 7, 9]
print(s.findMaxXor(A))
