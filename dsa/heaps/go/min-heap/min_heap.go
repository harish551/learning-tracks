
package main

import (
    "container/heap"
    "fmt"
)

type MinHeap []int

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func main() {
    minHeap := &MinHeap{}
    heap.Init(minHeap)
    heap.Push(minHeap, 10)
    heap.Push(minHeap, 40)
    heap.Push(minHeap, 15)
    heap.Push(minHeap, 20)


	fmt.Printf("Min Heap: %v\n", minHeap)
	fmt.Printf("Popped: %d\n", heap.Pop(minHeap))
	fmt.Printf("Min Heap: %v\n", minHeap)
	fmt.Printf("Popped: %d\n", heap.Pop(minHeap))
	fmt.Printf("Min Heap: %v\n", minHeap)
	fmt.Printf("Popped: %d\n", heap.Pop(minHeap))
	fmt.Printf("Min Heap: %v\n", minHeap)
}