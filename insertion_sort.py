def insertion(list):
    for i in range(1,len(list)):
        anchor=list[i]
        j=i-1
        while j>=0 and anchor<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=anchor    
    print("sorted list is....")
    print(list)
size=int(input("enter the list size:"))
list=[]
print("enter the elements:")
for i in range(size):
    el=int(input())
    list.append(el)
insertion(list)