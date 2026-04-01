/***
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

*/

package main

import (
	"container/heap"
	"fmt"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	h := &MaxHeap{}
	heap.Init(h)
	for idx, scr := range score {
		heap.Push(h, Rank{Score: scr, Index: idx})
	}
	answers := make([]string, len(score))
	for i := range len(score) {
		rank := heap.Pop(h).(Rank)
		switch i {
		case 0:
			answers[rank.Index] = "Gold Medal"
		case 1:
			answers[rank.Index] = "Silver Medal"
		case 2:
			answers[rank.Index] = "Bronze Medal"
		default:
			answers[rank.Index] = strconv.Itoa(i + 1)
		}
	}
	return answers
}

type Rank struct {
	Score int
	Index int
}

type MaxHeap []Rank

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].Score > h[j].Score } // maxHeap condition
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Rank))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]

	return x
}

func main() {
	fmt.Println("Example 1: ")
	scores1 := []int{5, 4, 3, 2, 1}
	fmt.Printf("Scores: %+v\n", scores1)
	answers1 := findRelativeRanks(scores1)
	fmt.Printf("Answers: %+v\n", answers1)

	fmt.Println("Example 2: ")
	scores2 := []int{10, 3, 8, 9, 4}
	fmt.Printf("Scores: %+v\n", scores2)
	answers2 := findRelativeRanks(scores2)
	fmt.Printf("Answers: %+v\n", answers2)
}
