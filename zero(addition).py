from array import *
arr=array('i',[])
n=int(input("enter the array"))
for i in range(n):
     x=int(input("enter the value"))
     arr.append(x)
for i in range(len(arr)):
       print(arr[i])

for i in range(n):
    if(arr[i]==0):
          v=i;
n=n+1;
arr.insert(v+1,0);
print(arr);

