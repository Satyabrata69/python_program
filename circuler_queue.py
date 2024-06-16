import sys
def insert():
    global list,f,r,n
    if f==-1 and r==-1:
        el=int(input("enter the element"))
        list.append(el)
        f=f+1
        r=r+1
    elif (r+1)%n==f:
        print("queue is full.....")   
    else:    
        el=int(input("enter the element"))
        list.append(el)
        r=(r+1)%n   
def delete():
    global list,f,r,n
    if f==r==-1 and f==r:
        print("queue is empty...")
    else:
        list.pop(0)   
        f=(f+1)%n   
def display():
    global list,f,r,n
    if f==r==-1 and f==r:
        print("queue is empty..")
    else:
        print(list)
def exit():
    sys.exit()                          
n=int(input("enter the array size..."))
list=[]
f=-1
r=-1
while True:
    print("1 for insert")
    print("2 for delete")
    print("3 for dispaly")
    print("4 for exit")
    ch=int(input("enter your choice"))
    if ch==1:
        insert()
    if ch==2:
        delete()
    if ch==3:
        display()
    if ch==4:
        exit()    
