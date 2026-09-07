n=int(input("enter the number"))
temp=n
result=0
l=[]
j=0
s=""
while(temp>0):
    r=temp%2
    s=str(r)+s
    temp=temp//2
for  i in s:
  if i=="0":
    l.append(1)
  elif i=="1":
    l.append(0)
for i in range(len(l)-1,-1,-1):
  result+=l[i]*(2**j)
  j+=1
print(result)
