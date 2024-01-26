a=input().split()
maxx=-99999
_mixx=0
i=0
long_a=len(a)
while i<long_a:
 if int(a[i])>int(maxx):
  maxx=a[i]
  mixx=i
 i+=1
print(maxx, end=" ")
print(mixx)