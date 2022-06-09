import array
def binarysearch(arr,k):
        l=0
        h=len(arr)-1
        mid=0
        while l<=h:
                mid=(h+l)//2
                if arr[mid]<k:
                       l=mid+1
                elif arr[mid]>k:
                       h=mid-1
                else:
                      return mid
        return 1
arr=[]
n=int(input("enter the size of array"))
for x in range(n):
        x=int(input("enter the elements of array"))
        arr.append(x)
print(arr)
k=int(input("enter the elemnet to serach"))
a=binarysearch(arr,k)
if(a!=1):
    print("element is at index:",a)
else:
    print("element is not present")
         
