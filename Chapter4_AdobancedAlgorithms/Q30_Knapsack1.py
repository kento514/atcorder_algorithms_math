ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, W = na()
wv = [nl() for _ in range(N)]
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j < wv[i][0]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-wv[i][0]]+wv[i][1])

print(dp[-1][-1])