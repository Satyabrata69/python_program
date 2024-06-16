import sys
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class singleLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):           
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next        
    def exit():
        sys.exit(0)        
s=singleLL()
while True:
    print("1 for insert_at_start")
    print("2 for insert_at_last")
    print("3 for insert_after")
    print("4 for exit")
    print("5 for display")
    print("6 for delete at first")
    print("7 for delete at last")
    print("8 for delete item") 
    ch=int(input("enter your choice..."))
    if ch==1:
        n=int(input("enter the element"))
        s.insert_at_start(n)
    if ch==2:
        n=int(input("enter the element"))
        s.insert_at_last(n)
    if ch==3:
        k=int(input("enter the before element"))
        n=int(input("enter the element"))
        s.insert_after(s.search(k),n) 
    if ch==4:
        s.exit()   
    if ch==5:
        s.print_list()    
    if ch==6:
        s.delete_first()
    if ch==7:
        s.delete_last()
    if ch==8:
        n=int(input("enter the element"))
        s.delete_item(n)                     

