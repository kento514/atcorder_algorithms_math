from collections import deque
import heapq
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

K = ni()
G = [list() for _ in range(K)]
for i in range(K):
    G[i].append([1,((i+1)%K)])
    G[i].append([0,((i*10)%K)])

TF = [False]*K
ans = [-1]*K
q = [(1,1)]
heapq.heapify(q)
while q:
    x, y = heapq.heappop(q)
    if TF[y]:
        continue
    TF[y] = True
    ans[y] = x
    if y == 0:
        print(x)
        exit()
    for x2, y2 in G[y]:
        if not(TF[y2]):
            heapq.heappush(q,(x + x2,y2))


