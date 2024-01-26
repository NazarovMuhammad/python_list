a = input().split()
b = int(input())
cnt = 1
for i in a:
    if b<=int(i):
      cnt+=1
print(cnt) 
    