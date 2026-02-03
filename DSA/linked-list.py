class Node:
    def __init__(self,data=None ,next=None):
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    
    
    def insert_at_end(self, data):
        # Case 1: If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = Node(data, None)
            return

        # Case 2: Traverse to the very last node
        itr = self.head
        while itr.next:        # Keep moving as long as there is a next node
            itr = itr.next

        # Now itr is the last node. Point its 'next' to our new node.
        itr.next = Node(data, None)
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
       #linked list string llstr
        llstr=""
        while itr:
            llstr+=str(itr.data) + "-->"
            itr=itr.next
        print(llstr)
        
        
    def insert_values(self,data_list):
        # self.head=None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count ==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invelid Index")
        if index==0:
            self.insert_at_begining(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            
            itr=itr.next
            count+=1
            
            
        
        
        
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(88)
    ll.insert_at_end(77)
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.remove_at(0)
    ll.insert_at(0,"fug")
    ll.print()
    ll.insert_at(2,"cake")
    ll.print()
    print("length : ",ll.get_length())
       
       