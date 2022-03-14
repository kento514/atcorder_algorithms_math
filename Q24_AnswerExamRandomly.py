ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
PQ = [nl() for _ in range(N)]
ans = 0
for i in range(N):
    ans += PQ[i][1]/PQ[i][0]
print(ans)