def binary_search(arr,search):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==search:
            return mid
        elif search<arr[mid]:
            high=mid-1
        else:
            low=mid+1     
    return -1
array_size=int(input("enter the array size:"))
print("the the elements....")
arr=[]
for i in range(array_size):
    el=int(input())
    arr.append(el)
print(arr)    
for i in range(1,len(arr)):
    anchor=arr[i]
    j=i-1
    while j>=0 and anchor<arr[j]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=anchor
print(arr)        
search=int(input("enter the search element "))    
output=binary_search(arr,search)    
if output==-1:
    print("the element is not found.....")
else:
    print("element is present and positon is",output+1)    
