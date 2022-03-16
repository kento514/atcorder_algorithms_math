ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, Q = na()
A = nl()
LR = [nl() for _ in range(Q)]
Asum = [0]*(N+1)
for i in range(N):
    Asum[i+1] = Asum[i]+A[i]

for j in range(Q):
    print(Asum[LR[j][1]]-Asum[LR[j][0]-1])