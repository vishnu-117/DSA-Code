class Node:
    
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next = third

    while linked_list.head != None:
        previous_node = linked_list.head
        head.next = previous_node
        # next_node.next = previous_node
        head = head.next

