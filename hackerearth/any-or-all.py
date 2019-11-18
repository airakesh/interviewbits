''' Method 1:'''
'''Three lins code'''

n = int(input())

nums = list(map(int, input().split()))

print('True') if (all(i > 0 for i in nums) and any(str(i) == str(i)[::-1] for i in nums)) else print('False')


''' Method 2'''

class Solution:
    def __init__(self):
        self.n = int(input())
        self.nums = list(map(int, input().split()))
        
    def palinInt(self):
        print(all(i > 0 for i in self.nums) and any(str(i) == str(i)[::-1] for i in self.nums))
        
if __name__ == '__main__':
    s = Solution()
    s.palinInt()
