class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # dummy head & tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, val):
        node = Node(val)

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

        self.size += 1

    def prepend(self, val):
        node = Node(val)

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def _remove(self, node):
        if node is None or node == self.head or node == self.tail:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove(self, val):
        curr = self.head.next
        while curr != self.tail:
            if curr.val == val:
                self._remove(curr)
                return
            curr = curr.next

    def pop(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self._remove(node)
        return node.val

    def reverse(self):
        curr = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev  # move forward after swap

        self.head, self.tail = self.tail, self.head

    def print_list(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")

    def __len__(self):
        return self.size
    

dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list()

dll.append(5)
dll.print_list()

dll.pop()
dll.print_list()

dll.prepend(10)
dll.print_list()

dll.remove(3)
dll.print_list()

dll.reverse()
dll.print_list()

print("Size:", len(dll))