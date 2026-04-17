package main

import "fmt"

type Node struct {
	Val  int
	Next *Node
	Prev *Node
}

type DoublyLinkedList struct {
	Head *Node // dummy head
	Tail *Node // dummy tail
	Size int
}

// Constructor
func NewDoublyLinkedList() *DoublyLinkedList {
	head := &Node{}
	tail := &Node{}
	head.Next = tail
	tail.Prev = head

	return &DoublyLinkedList{
		Head: head,
		Tail: tail,
		Size: 0,
	}
}

// Append at tail
func (dll *DoublyLinkedList) Append(val int) {
	newNode := &Node{Val: val}

	newNode.Next = dll.Tail
	newNode.Prev = dll.Tail.Prev

	dll.Tail.Prev.Next = newNode
	dll.Tail.Prev = newNode

	dll.Size++
}

// Prepend at head
func (dll *DoublyLinkedList) Prepend(val int) {
	newNode := &Node{Val: val}

	newNode.Next = dll.Head.Next
	newNode.Prev = dll.Head

	dll.Head.Next.Prev = newNode
	dll.Head.Next = newNode

	dll.Size++
}

// Remove a node (internal)
func (dll *DoublyLinkedList) Remove(node *Node) {
	if node == nil || node == dll.Head || node == dll.Tail {
		return
	}

	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
	dll.Size--
}

// Remove by value (for usability)
func (dll *DoublyLinkedList) RemoveByValue(val int) {
	curr := dll.Head.Next
	for curr != dll.Tail {
		if curr.Val == val {
			dll.Remove(curr)
			return
		}
		curr = curr.Next
	}
}

// Pop from tail
func (dll *DoublyLinkedList) PopFromTail() {
	if dll.Size == 0 {
		return
	}
	dll.Remove(dll.Tail.Prev)
}

// Print list
func (dll *DoublyLinkedList) PrintList() {
	curr := dll.Head.Next
	for curr != dll.Tail {
		fmt.Printf("%d <-> ", curr.Val)
		curr = curr.Next
	}
	fmt.Println("nil")
}

// Reverse list (correct DLL reversal)
func (dll *DoublyLinkedList) Reverse() {
	curr := dll.Head
	for curr != nil {
		curr.Next, curr.Prev = curr.Prev, curr.Next
		curr = curr.Prev // move forward after swap
	}
	dll.Head, dll.Tail = dll.Tail, dll.Head
}

// Get size
func (dll *DoublyLinkedList) GetSize() int {
	return dll.Size
}

// ---------------- MAIN ----------------

func main() {
	fmt.Println("Doubly Linked List Implementation")
	fmt.Println("================================")

	ll := NewDoublyLinkedList()

	fmt.Println("1. Append elements")
	ll.Append(1)
	ll.Append(2)
	ll.Append(3)
	ll.Append(4)
	ll.PrintList()

	fmt.Println("2. Append one more")
	ll.Append(5)
	ll.PrintList()

	fmt.Println("3. Pop from tail")
	ll.PopFromTail()
	ll.PrintList()

	fmt.Println("4. Prepend element")
	ll.Prepend(10)
	ll.PrintList()

	fmt.Println("5. Remove value 3")
	ll.RemoveByValue(3)
	ll.PrintList()

	fmt.Println("6. Reverse list")
	ll.Reverse()
	ll.PrintList()

	fmt.Println("7. Size of list:", ll.GetSize())
}
