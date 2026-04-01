package main 

import (
	"container/heap"
	"fmt"
)

type MaxHeap []int

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // maxHeap condition
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]

	return x
}

func main() {
	maxheap := &MaxHeap{}

	heap.Init(maxheap)
	heap.Push(maxheap, 10)
	heap.Push(maxheap, 45)
	heap.Push(maxheap, 20)
	heap.Push(maxheap, 8)
	

	fmt.Printf("Max Heap: %v\n", maxheap)
	fmt.Printf("Popped: %d\n", heap.Pop(maxheap))
	fmt.Printf("Max Heap: %v\n", maxheap)
	fmt.Printf("Popped: %d\n", heap.Pop(maxheap))
	fmt.Printf("Max Heap: %v\n", maxheap)
	fmt.Printf("Popped: %d\n", heap.Pop(maxheap))
	fmt.Printf("Max Heap: %v\n", maxheap)
}