n1=int(input())
n2=int(input())
l1=[]
l2=[]
k=0
for i in range(n1):
  d=int(input())
  l1.append(d)
for j in range(n2):
  d=int(input())
  l2.append(d)
l3=l1+l2
a=0
l4=list(set(l3))
l4=sorted(l4)
b=len(l4)
if b%2==0:
  c=l4[(b//2)-1]+l4[(b//2)]
  k=c/2
else:
  k=l4[b//2]
print(k)