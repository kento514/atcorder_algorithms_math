ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
sumA = [0]*N
for i in range(N-1):
    sumA[i+1] = sumA[i]+A[i]

M = ni()
B = [ni() for _ in range(M)]
ans = 0
for i in range(M-1):
    if B[i]>B[i+1]:
        ans += (sumA[B[i]-1]-sumA[B[i+1]-1])
    else:
        ans += (sumA[B[i+1]-1]-sumA[B[i]-1])
print(ans)