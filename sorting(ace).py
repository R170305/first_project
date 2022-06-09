import numpy as np
temp=0
arr1=np.array([1,2,3,4,5])
arr2=np.array([2,6,7,8])
arr=np.concatenate((arr1,arr2));
for i in range(0,len(arr)):
  for j in range(i+1,len(arr)):
    if(arr[i]>arr[j]):
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
print(arr)
