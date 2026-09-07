n=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in l:
  x=i
  for j in range(s):
      x=x//2
  print(x,end=" ")