ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, M = na()
ans = [0]*N
for _ in range(M):
    a, b = na()
    if a < b:
        ans[b-1]+=1
    else:
        ans[a-1]+=1

print(ans.count(1))