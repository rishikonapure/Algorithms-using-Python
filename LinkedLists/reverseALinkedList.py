class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        if self.head is None:
            print("inside base")
            return

        previous = None
        current = self.head

        while current:
             current.next, previous, current = previous, current, current.next # procedure 1

             # next = current.next
             # current.next = previous  #procedure 2
             # previous = current
             # current = next

        self.head = previous

        print("Now head is",self.head.data)



    def printList(self):
        current = self.head
        while current:
            print(current.data,"-->",end="")
            current = current.next
        print("null")


    def push(self,newnode):  #you can insert the new node at the head - This takes less time than inseting at the end
        newnode = Node(newnode)
        newnode.next = self.head
        self.head = newnode



# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("PrintList")
llist.printList()
llist.reverse()

print("PrintReversedList")
llist.printList()
