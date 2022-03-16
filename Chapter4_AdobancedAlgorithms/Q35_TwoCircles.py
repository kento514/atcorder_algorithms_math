ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

x1, y1, r1 = na()
x2, y2, r2 = na()
distance = ((x1-x2)**2+(y1-y2)**2)**0.5

if abs(r2-r1)>distance:
    print(1)
elif abs(r2-r1)==distance:
    print(2)
elif distance < r1+r2:
    print(3)
elif distance == r1+r2:
    print(4)
else:
    print(5)
