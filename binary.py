def binary_search(arr,low,high,x):
        if high>=low:
                mid=(high+low)//2
                if arr[mid]==x:
                        return mid
                elif arr[mid]>x:
                        return binary_search(arr,low,mid-1,x)
                else:
                        return binary_search(arr,mid+1,high,x)
        else:
                        return -1
arr=[3,5,7,8,9,10]
x=5
result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
        print("element is present at index",str(result))
else:
        print("element is not present in array")
