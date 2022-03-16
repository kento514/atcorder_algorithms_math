ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
dp = [0]*N
dp[0:2] = A[0:2]
dp[2] = dp[0] + A[2]
for i in range(3,N):
    dp[i] = max(dp[i-2]+A[i], dp[i-3]+A[i])

print(max(dp[-1], dp[-2]))