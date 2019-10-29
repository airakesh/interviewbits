'''
You’re given a read only array of n integers. Find out if any integer occurs 
more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count1 = 0
        count2 = 0
        n = len(A)
        first = sys.maxsize
        second = sys.maxsize

        for i in range(len(A)):
            if first == A[i]:
                count1 += 1

            elif second == A[i]:
                count2 += 1

            elif count1 == 0:
                count1 += 1
                first = A[i]

            elif count2 == 0:
                count2 += 1
                second = A[i]

            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for i in range(len(A)):
             if A[i] == first:
                 count1 += 1

             elif A[i] == second:
                 count2 += 1

        if count1 > len(A) / 3:
            return first

        if  count2 > len(A) / 3:
            return second

        return -1

# Ans code
s = Solution()
A = [1, 2, 3, 1, 1]
n = len(A)
print(s.repeatedNumber(A))
