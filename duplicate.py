import array
arr=[]
count=[]
n=int(input("enter the size of array"))
for x in range(n):
        count.append(0)
        x=int(input("enter the elements of array"))
        arr.append(x)
print("array elements after removing duplicates")
for x in range(n):
       count[arr[x]]=count[arr[x]]+1
       if count[arr[x]]==1:
              print(arr[x])
