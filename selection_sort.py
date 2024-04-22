#selection sort 
def sorts(nums):
    for i in range(len(nums)):
        small_pos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[small_pos]:
                small_pos=j
        nums[small_pos],nums[i]=nums[i],nums[small_pos]   
    print("sorted list....") 
    print(nums)        
size=int(input("how many elements you want to add in list:"))
nums=[]
print("enter the elements....")
for i in range(0,size):
    el=int(input())
    nums.append(el)
print("your list is ......")  
print(nums,"\n")
sorts(nums)