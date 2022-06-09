import array
arr=[]
n=int(input("enter the size of array"))
for x in range(n):
        x=int(input("enter the elements of array"))
        arr.append(x)
print(arr)
key=int(input("enter the elemnet to serach"))
for i in range(len(arr)):
         if(key==arr[i]):
             print("element is present")
             break
if(key!=arr[i]):
      print("element not present")
