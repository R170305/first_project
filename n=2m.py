import array
arr=[]
n=int(input("enter the size of array"))
for x in range(n):
        x=int(input("enter the elements of array"))
        arr.append(x)
print(arr)
for i in range(len(arr)):
     for j in range(len(arr)):
          if(arr[i]==2*arr[j]):
              print(arr[j],arr[i])
