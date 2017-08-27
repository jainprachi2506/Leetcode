problem(i) -> f(problem(a-1))
problem(i, j)

X: ABCBDAB
Y: BDCABA

problem(i, j) => the longest subsequence of X[0..i] and Y[0..j]

problem(i, j)
if X[i] == Y[j]:
	problem(i, j) = 1 + problem(i-1, j-1)
else:
	problem(i, j) = max(problem(i, j-1), problem(i-1, j))

problem(0, ..j..)
problem(..i.., 0)
problem:
j
0 1 2 3 4 5 6 
1 0 1 
2
3
4
5


SCS
X: ABCBDAB
Y: BDCABA

problem(i, j) = SCS of string X[0:i] and Y[0:j]

problem(i, j) =
if X[i] == Y[j]:
	problem(i, j) = problem(i-1, j-1) + 1
else:
	min(
		problem(i-1, j),
		problem(i, j-1)
	) + 1


problem(len(X), len(Y))





A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

LIS length

problem(i) = longest increasing subsequence ending at A[i]
final result = max(problem(0),problem(1),problem(2)...problem(A[-1]))

problem(i)
for j in xrange(i):
	if A[j] < A[i]:
		problem(i) = max(problem(i), problem(j) + 1)

[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
[1, 2, 2, 3, ...]




kitten -> sitten (substitution of s for k)
sitten -> sittin (substitution of i for e)
sittin -> sitting (insertion of g at the end)

edit distance problem

X = kitten
Y = sittingn

X -> Y
1. add 2. remove 3. substitution

a b c z
x y z

problem(i, j) = edit distance to convert X[0:i] -> Y[0:j]
final solution is problem(len(X), len(Y))
problem(i, j)
if X[i] == Y[j]:
	problem(i, j) = problem(i-1, j-1)
else:
	problem(i, j) = min(
		problem(i-1, j),
		problem(i, j-1),
		problem(i-1, j-1)
	) + 1


(weight, value) pairs

weights = [ (1,20), (2,5), (3,10), (8,40), (7,15), (4,25) ]
int W = 10

problem(i, W) = 
how much max value can 
we produce if we carry weight exactly W and we use only weights[0:6]
only first i weights

final solution = max(problem(len(weights), 0), problem(len(weights), 1), problem(len(weights), 2) ... problem(len(weights), W))

i = 0
W = 0
problem(i, W) = 0
problem(6, 1) = ? weights[0:6] the weight should be exactly 1 = 20
problem(6, 2) = 5
problem(6, 3) = 25
problem(6, 4) = 30
problem(6, 5) = 45
problem(6, 6) = 

def problem(i, W):
	wi = weights[i][0]
	vi = wi = weights[i][1]
	return max(problem(i-1, W), vi + problem(i-1, W-wi))







S = [3,1,1,2,2,1] = 10
sum = sum(S)
find a subset which sums to 5

problem(i, s) = is there a subset of S[0:i] (first i elements of S) which sum to s
final solution: problem(len(S), sum(S)/2)

problem(i, s): problem(i-1, s) or problem(i-1, s-S[i])
# take S[i]
# don't take S[i]
problem(i, s) in dp[i][s]



 S = [ 1, 3, 5, 7 ]

 problem(i): Min number of coins required to make change for i using coins from S

 problem(1) = 1
 problem(2) = 2 (1+1)
 problem(3) = 1 (3)
 problem(4) = 2 (1+3)

 def problem(i):
 	ret = i+1
 	for coin in S:
 		ret = min(ret, problem(i-coin) + 1)
	return ret

[1, 2, 1, .... C] 



























































