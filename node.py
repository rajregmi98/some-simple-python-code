class Node:
    def __init__(self,data):
        self.data = data #assign data 
        self.next = None #initialize next 
    
class likedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next
        
if __name__ == "__main__":
    llist = likedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;
    second.next = third;
    llist.printlist()
