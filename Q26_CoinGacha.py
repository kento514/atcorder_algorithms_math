ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
ans = 0
for i in range(1, N+1):
    ans += 1/i

print(N*ans)