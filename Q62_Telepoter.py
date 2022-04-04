ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, K = na()
A = nl()
B = list()
TF = [True]*N
i = 0

while TF[i]:
    TF[i]=False
    B.append(i)
    i = A[i]-1
x = B.index(i)
C = B[x:]
mod = len(C)
if K<len(B):
    print(B[K]+1)
else:
    print(C[(K-x)%mod]+1)


