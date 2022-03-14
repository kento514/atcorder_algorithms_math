from itertools import combinations
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
count = 0
for i in combinations(A, 5):
    s = 0
    for j in i:
        s+=j
    if s==1000:
        count+=1
print(count)



