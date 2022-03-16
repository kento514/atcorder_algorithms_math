from collections import deque

ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, M = na()
G = [list() for _ in range(N)]
for _ in range(M):
    A, B = na()
    G[A-1].append(B-1)
    G[B-1].append(A-1)

ans = [False]*N
serachlist = deque([0])
while serachlist:
    index = serachlist.popleft()
    if ans[index]:
        continue
    ans[index]=True
    for i in G[index]:
        if not ans[i]:
            serachlist.append(i)
if all(ans):
    print('The graph is connected.')
else:
    print('The graph is not connected.')