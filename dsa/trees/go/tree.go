package main

import "fmt"

type TreeNode struct {
	Value int
	Left  *TreeNode
	Right *TreeNode
}

type Tree struct {
	Root *TreeNode
}

func NewTreeNode(val int) *TreeNode {
	return &TreeNode{Value: val}
}

func NewTree() *Tree {
	return &Tree{}
}

func (t *Tree) Insert(val int) {
	if t.Root == nil {
		t.Root = NewTreeNode(val)
		return
	}
	queue := []*TreeNode{t.Root}
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		if curr.Left == nil {
			curr.Left = NewTreeNode(val)
			return
		}
		queue = append(queue, curr.Left)
		if curr.Right == nil {
			curr.Right = NewTreeNode(val)
			return
		}
		queue = append(queue, curr.Right)
	}
}

func (t *Tree) InOrderTraversal() {
	if t.Root == nil {
		return
	}
	var inOrder func(node *TreeNode)
	inOrder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inOrder(node.Left)
		fmt.Printf("%d ", node.Value)
		inOrder(node.Right)
	}
	inOrder(t.Root)
}

func (t *Tree) PreOrderTraversal() {
	if t.Root == nil {
		return
	}
	var preOrder func(node *TreeNode)
	preOrder = func(node *TreeNode) {
		if node == nil {
			return
		}
		fmt.Printf("%d ", node.Value)
		preOrder(node.Left)
		preOrder(node.Right)
	}
	preOrder(t.Root)
}

func (t *Tree) PostOrderTraversal() {
	if t.Root == nil {
		return
	}
	var postOrder func(node *TreeNode)
	postOrder = func(node *TreeNode) {
		if node == nil {
			return
		}
		postOrder(node.Left)
		postOrder(node.Right)
		fmt.Printf("%d ", node.Value)
	}
	postOrder(t.Root)
}

func main() {
	// Build a Tree
	tree := NewTree()
	tree.Insert(1)
	tree.Insert(2)
	tree.Insert(3)
	tree.Insert(4)
	tree.Insert(5)
	tree.Insert(6)
	tree.Insert(7)

	fmt.Println("Tree Root")
	fmt.Println(tree.Root)

	fmt.Println("In Order Traversal")
	tree.InOrderTraversal()
	fmt.Println("\nPre Order Traversal")
	tree.PreOrderTraversal()
	fmt.Println("\nPost Order Traversal")
	tree.PostOrderTraversal()
	fmt.Println()

}
