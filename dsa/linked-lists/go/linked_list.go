package main

import "fmt"

type Node struct {
	Val  int
	Next *Node
}

type LinkedList struct {
	Head *Node
	Size int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{
		Head: nil,
		Size: 0,
	}
}

func (ll *LinkedList) Append(val int) {
	newNode := &Node{Val: val}
	if ll.Head == nil {
		ll.Head = newNode
	} else {
		curr := ll.Head
		for curr.Next != nil {
			curr = curr.Next
		}
		curr.Next = newNode
	}
	ll.Size++
}

func (ll *LinkedList) Prepend(val int) {
	newNode := &Node{Val: val}
	if ll.Head == nil {
		ll.Head = newNode
	} else {
		newNode.Next = ll.Head
		ll.Head = newNode
	}
	ll.Size++
}

func (ll *LinkedList) Pop() {
	if ll.Head == nil {
		return
	}
	if ll.Head.Next == nil {
		ll.Head = nil
		ll.Size--
		return
	}

	curr := ll.Head
	for curr.Next != nil && curr.Next.Next != nil {
		curr = curr.Next
	}
	curr.Next = nil
	ll.Size--
}

func (ll *LinkedList) Remove(val int) {
	if ll.Head == nil {
		return
	}
	curr := ll.Head
	for curr != nil && curr.Next != nil {
		if curr.Next.Val == val {
			curr.Next = curr.Next.Next
			ll.Size--
			return
		}
		curr = curr.Next
	}
}

func (ll *LinkedList) PrintList() {
	if ll.Head == nil {
		return
	} else {
		curr := ll.Head
		for curr != nil {
			fmt.Printf("%d -> ", curr.Val)
			curr = curr.Next
		}
		fmt.Println("nil")
	}
}

func (ll *LinkedList) Reverse() {
	if ll.Head == nil || ll.Head.Next == nil {
		return
	}
	var prev *Node
	curr := ll.Head
	for curr != nil {
		nextNode := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextNode
	}
}

func (ll *LinkedList) GetSize() int {
	return ll.Size
}

func main() {
	fmt.Println("Linked List Implementation")
	fmt.Println("============================")
	fmt.Println("1.Create a linked list")

	ll := NewLinkedList()
	ll.Append(1)
	ll.Append(2)
	ll.Append(3)
	ll.Append(4)
	ll.PrintList()

	fmt.Println("2.Append a value at the end")
	ll.Append(5)
	ll.PrintList()

	fmt.Println("3.Pop a value from the end")
	ll.Pop()
	ll.PrintList()

	fmt.Println("4.Prepend a value at the beginning")
	ll.Prepend(5)
	ll.PrintList()
	fmt.Println("5.Remove a given value")
	ll.Remove(3)
	ll.PrintList()
	fmt.Println("6.Reverse linked list")
	ll.Reverse()
	ll.PrintList()
	fmt.Println("7.Get size of linked list")
	fmt.Println(ll.GetSize())
}
