ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
ans = 0
for i in range(1,N+1):
    for j in range(i,N+1,i):
        ans += j

print(ans)