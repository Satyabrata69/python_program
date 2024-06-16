import sys
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class cll:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if self.last==temp:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)
        else:
            print("circuler ll is empty...") 
    def delete_at_firs(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next    
s=cll()
while True:
    print("1 for display")
    print("2 for insert at first")
    print("3 for insert at last")
    print("4 for insert after")
    print("5 for delete at first")
    ch=int(input("enter your choice..."))
    if ch==1:
        s.print_list()
    if ch==2:
        n=int(input("enter the element"))
        s.insert_at_first(n) 
    if ch==3:
        n=int(input("ente the element"))
        s.insert_at_last(n)
    if ch==4:
        k=int(input("enter the previous valu"))
        n=int(input("enter the valu"))
        s.insert_after(s.search(k),n)                                     
    if ch==5:
        s.delete_at_firs()    