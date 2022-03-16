from collections import deque
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

R, C = na()
sy, sx = na()
gy, gx = na()
Route = [ns() for _ in range(R)]
ans = [[-1]*C for _ in range(R)]
ans[sy-1][sx-1] = 0
l = [[1,0], [-1,0], [0,1], [0,-1]]
searchlist = deque([[sy-1,sx-1]])
while searchlist:
    y, x = searchlist.popleft()
    for i in l:
        ny, nx = y+i[0], x+i[1]
        if not(0<=ny<R) or not(0<=nx<C) or Route[ny][nx]=='#' or ans[ny][nx]!=-1:
            continue
        ans[ny][nx] = ans[y][x]+1
        if ny == gy-1 and nx==gx-1:
            print(ans[ny][nx])
            exit()
        searchlist.append([ny,nx])