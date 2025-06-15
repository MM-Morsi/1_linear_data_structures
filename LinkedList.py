import Node


class LinkedList:
    def __init__(self):
        self.head = None
    # reperentation function 
    def __repr__(self):
        # ignore for now
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None") # important as a stopping condition in the future
        return " -> ".join(nodes) # assumes string nodes only no integer values

# creating the linkedlist 
node1 = Node.Node(1)
node2 = Node.Node(2)
node3 = Node.Node(3)

node1.next = node2
node2.next = node3
# testing individual nodes

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)

# testing the linkedlist 
list = LinkedList()
list.head = node1
print(list)