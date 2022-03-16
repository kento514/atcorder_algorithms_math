ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
h = nl()
dp = [0]*N
dp[1] = abs(h[0] - h[1])
for i in range(N-2):
    dp[i+2] = min(dp[i+1]+abs(h[i+2]-h[i+1]), dp[i]+abs(h[i+2]-h[i]))

print(dp[-1])