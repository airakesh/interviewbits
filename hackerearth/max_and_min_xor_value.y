'''
Milly is feeling bored during her winter vaccations, so she has decided to do some random fun on some arrays. 
She will take K number of arrays of same same size N. She will make all possible non-empty subsets of these arrays. 
She will make a Set S made up of the same-sized subsets of these arrays while considering the same indexes of the arrays . 
Then she will apply the operation P in each of these possible S sets. Your task is to help her in this question.

For example, say there are 2 arrays [1, 2] , [3, 4]. So while making Sets of subsets she will make subsets of both arrays 
with considering only same indexes. These will be the all possible sets of subsets while considering the same indexes of 
both the arrays.

                    S1 = {[1], [3]}
                    S2 = {[2], [4]}
                    S3 = {[1, 2], [3, 4]}
Now she will apply an operation P one bye one on these sets and try to find the sets having maximum as well as 
the minimum values of P. She is also interested in knowing the lengths of those subsets that made the resultant 
sets with maximum and minimum values of P. There can be multiple such maximum and minimum values of P that are 
possible so you have to choose the maximum value set of subsets with minimum length and minimum value set of subsets with maximum length.

Suppose there are K arrays, so the value of P for a particular set of X - sized subsets with i, j ... m indexes of those arrays is defined below :
Q = ( (A1[i] + ... AK[i]) * (A1[j] + ... AK[j]) * (A1[m] + ... AK[m]) ) / X
P = Q%(109+7)

Input
First line of the input will contain T (no. of test cases). For every test case first line will have two space separated 
values N and K.Then the next K lines will have N space separated integers of corresponding arrays.

Output
Since your result will be two sets having maximum and minimum values of P. Therefore print two space separated values. 
First value should be the XOR of maximum and minimum values of P and the second value should be the XOR of the length 
of subsets of these sets.

Constraints
1 <= T <= 5
1 <= N <= 16
1 <= K <= 10
0 <= values of arrays <= 109

SAMPLE INPUT 
1
2 2
1 2
3 4

SAMPLE OUTPUT 
8 3

Explanation
There are sets that can be possible. These are :
S1 = { [1] , [3] }, so P = (1 + 3)/1 = 4
S2 = { [2] , [4] }, so P = (2 + 4)/1 = 6
S3 = { [1, 2] , [3, 4] }, so P = ((1 + 3)*(2 + 4))/2 = 12
Therefore maximum value of P is 12 with subsets of length = 2 and the minimum value of P is 4 with subsets of length = 1. So ans will be 12 XOR 4 and 1 XOR 2.

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        return min(map(lambda i: A[i] ^ A[i + 1], range(len(A) - 1)))

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
print(s.findMaxXor(A), s.findMinXor(A))
