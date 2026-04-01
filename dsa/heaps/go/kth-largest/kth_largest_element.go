/***
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

*/

package main

import (
    "container/heap"
	"fmt"
)

func findKthLargest(nums []int, k int) int {
    h := &MinHeap{}
    heap.Init(h)
    for _, num := range nums {
        heap.Push(h, num)
        if h.Len() > k {
            heap.Pop(h)
        }
    }
    return heap.Pop(h).(int)
}

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
	fmt.Println("Example 1: ")
	elements := []int{3,2,1,5,6,4} 
	fmt.Printf("Elements: %+v\n", elements)
	ans := findKthLargest(elements, 3)
	fmt.Printf("K=%d, K'th largets element is %d\n", 3, ans)
}