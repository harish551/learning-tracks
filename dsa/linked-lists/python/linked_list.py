
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, val) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1  

    def prepend(self, val) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self) -> int | None:
        if not self.head:
            return None

        if not self.head.next:
            val  = self.head.val
            self.head = None
            self.size -= 1
            return val
        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next
        val = curr.next.val
        curr.next = None
        self.size -= 1
        return val

    def remove(self, val) -> int | None:
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.size -= 1
                return val
            curr = curr.next  
        return None
    
    def get_size(self) -> int:
        return self.size
    
    def print_list(self) -> None:
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def reverse(self) -> None:
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

if __name__ == '__main__':
    print("Linked List Implementation")
    print("============================")
    print("1.Create a linked list")

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.print_list()

    print("2.Append a value at the end")
    ll.append(5)
    ll.print_list()

    print("3.Pop a value from the end")
    val = ll.pop()
    print("Popped value:", val)
    ll.print_list()

    print("4.Prepend a value at the beginning")
    ll.prepend(val)
    ll.print_list()
    print("5.Remove a given value")
    ll.remove(3)
    ll.print_list()
    print("6.Reverse linked list")
    ll.reverse()
    ll.print_list()
    print("7.Get size of linked list")
    print(ll.get_size())
