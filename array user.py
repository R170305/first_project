import array as arr
arr1=arr.array('i',[])
n=int(input("enter the array"))
for i in range(n):
     x=int(input("enter the value"))
     arr1.append(x)
for i in range(len(arr1)):
       print(arr1[i])
k=int(input("enter the index"))
print(arr1[k])
