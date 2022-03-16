ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, X = na()
A = nl()
A.sort()

start = 0
end = N-1
ans = 'No'
while start<=end:
    mid = (start+end)//2
    if A[mid]==X:
        ans = 'Yes'
        break
    elif A[mid]>X:
        end = mid-1
    else:
        start = mid + 1
print(ans)