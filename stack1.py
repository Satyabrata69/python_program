import sys
def push():
    global stack,array_size
    if array_size==len(stack):
        print("stack is full.....")
    else:    
        element=int(input("enter the element"))
        stack.append(element)
def pop():
    global stack,array_size
    if len(stack)==0:
        print("stack is empty.....")
    else:
        n=len(stack)-1
        stack.pop(n)
def display():
    global stack
    if len(stack)==0:
        print("stack is empty....")
    else:
        print(stack)
def exit():
    sys.exit(0)       
def peek():
    global stack
    peeks=len(stack)-1
    print(stack[peeks])
array_size=int(input("enter your array size"))
stack=[]    
while True:
    print("1 for push")
    print("2 for pop")
    print("3 for display")
    print("4 for peek")
    print("5 for exit")
    choice=int(input("put your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        exit()
    else:
        print("put wright choice")                    