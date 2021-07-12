#  No idea code hackerrank python------------------
n, m=map(int,input().split())
arr=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))

s=0
d=0
for i in arr:
    if i in A:
        s=s+1
    if i in B:
        d=d-1      
print(s+d)
