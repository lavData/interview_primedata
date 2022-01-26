# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

''' My algorithm:
    1. If head = None return
    2. Consider each node, in turn, starting from the head. 
       If the value of the next node is equal to the value of the current node. 
       Points the current node's next pointer to the next node's next node. 
    
    => The complexity is O(n)
'''

# Linked list
class Linked_link:
    def __init__(self):
        self.head = None

    def push(self, Node):
        if self.head == None:
            self.head = Node
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = Node
    
    def remove_duplicated(self):
        if self.head == None:
            return
        
        temp = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self.head
    
    def print_list(self):
        temp = self.head
        while temp.next != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

if __name__ == "__main__":
    link_list = Linked_link()

    link_list.push(Node(11))
    link_list.push(Node(11))
    link_list.push(Node(12))
    link_list.push(Node(13))
    link_list.push(Node(14))
    link_list.push(Node(14))
    link_list.push(Node(14))
    link_list.push(Node(15))

    link_list.print_list()

    link_list.remove_duplicated()

    link_list.print_list()