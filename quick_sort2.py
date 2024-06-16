def quick(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[len(arr)//2]
        left=[x for x in  arr if x<pivot]
        middle=[x for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
        return quick(left)+middle+quick(right)

size=int(input("enter the size of a element"))
arr=[]
print("enter the element")
for i in range(size):
    el=int(input(""))
    arr.append(el)
sort=quick(arr)
print(sort)
