ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

H, W = na()
if H==1 or W==1:
    print(1)
else:
    print((H*W)//2 + (H*W)%2)