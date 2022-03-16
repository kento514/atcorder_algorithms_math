ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

ax, ay = na()
bx, by = na()
cx, cy = na()
ab_bc = (bx - ax)*(cx - bx) + (by - ay)*(cy - by)
ac_bc = (cx - ax)*(cx - bx) + (cy - ay)*(cy - by)
if bx==cx and by==cy:
    ans = ((ax-bx)**2 + (ay-by)**2)**0.5
elif ab_bc*ac_bc>0:
    if abs(ab_bc)<abs(ac_bc):
        ans = ((ax-bx)**2 + (ay-by)**2)**0.5
    else:
        ans = ((ax-cx)**2 + (ay-cy)**2)**0.5
else:
    ans = (abs((by-cy)*ax-(bx-cx)*ay+bx*cy-by*cx))/((by-cy)**2+(bx-cx)**2)**0.5
print(ans)