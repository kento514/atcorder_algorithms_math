ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
ans = [2]
for i in range(2,N+1):
    TF = all([(i%j)!=0 for j in ans])
    if TF:
        ans.append(i)


print(*ans)
