import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()
#余弦定理
A, B, H, M = na()
Hrad = (H*60+M)/2
Mrad = M*6
ans = (A**2+B**2-2*A*B*math.cos(abs(Hrad-Mrad)*math.pi/180))**0.5
print(ans)