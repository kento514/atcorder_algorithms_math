ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

x1, y1 = na()
x2, y2 = na()
x3, y3 = na()
x4, y4 = na()
f1 = lambda x, y: (y2 - y1)*x - (x2 - x1)*y + x2*y1-y2*x1
f2 = lambda x, y: (y4 - y3)*x - (x4 - x3)*y + x4*y3-y4*x3

if (x2-x1)*(y4-y3)-(y2-y1)*(x4-x3)==0:
    if ((x3-x1)*(x4-x1)+(y3-y1)*(y4-y1)>0) and ((x3-x2)*(x4-x2)+(y3-y2)*(y4-y2)>0):
        print('No')
    elif ((x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)>0) and ((x1-x4)*(x2-x4)+(y1-y4)*(y2-y4)>0):
        print('No')
    else:
        print('Yes')
elif f1(x3, y3)*f2(x4, y4)<=0 and f2(x1, y1)*f2(x2, y2)<=0:
    print('Yes')
else:
    print('No')
