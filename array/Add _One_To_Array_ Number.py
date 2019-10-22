class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        t = list(map(str, A))
        p = ''.join(t)
        num = int(p) + 1
        num = str(num)
        temp = []
        for i in range(len(num)):
            temp.append(int(num[i]))
            
        return temp    
            
# Answer code            
s = Solution()
A = [1, 2, 3, 4]
print(s.plusOne(A))
