from collections import deque
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, B = na()
ans = list()
num = 2
while N!=1:
    if N**0.5<num:
        ans.append(N)
    if N%num==0:
        ans.append(num)
        N = N//num
    else:
        if num==2:
            num+=1
        else:
            num+=2

ans1 = 1
for j in ans:
    if B%j == 0:
        ans1*=j
        B = B//j
print(ans1)
