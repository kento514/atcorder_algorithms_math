from collections import deque
import heapq

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

ans = [-1]*N
TF = [False]*N
serachlist = [[0,0]]
heapq.heapify(serachlist)
while serachlist:
    index = heapq.heappop(serachlist)
    if TF[index[1]]:
        continue
    TF[index[1]]=True
    ans[index[1]]=index[0]
    for i in G[index[1]]:
        if not TF[i]:
            heapq.heappush(serachlist,[index[0]+1, i])

for i in ans:
    print(i)
