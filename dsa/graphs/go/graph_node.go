package main

import "fmt"

// Node based Graph
type Node struct {
	Val       int
	Neighbors []*Node
}

func addEdge(u, v *Node) {
	u.Neighbors = append(u.Neighbors, v)
	v.Neighbors = append(v.Neighbors, u)
}

// DFS Traversal
func dfs(node *Node, visited map[*Node]bool) {
	if node == nil {
		return
	}

	visited[node] = true
	fmt.Print(node.Val, "->")

	for _, nei := range node.Neighbors {
		if !visited[nei] {
			dfs(nei, visited)
		}
	}
}

// BFS Traversal
func bfs(start *Node) {
	visited := make(map[*Node]bool)
	queue := []*Node{start}
	visited[start] = true

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		fmt.Print(node.Val, "->")

		for _, nei := range node.Neighbors {
			if !visited[nei] {
				visited[nei] = true
				queue = append(queue, nei)
			}
		}
	}
}

// Clone Graph (DFS)
func cloneGraph(node *Node) *Node {
	visited := make(map[*Node]*Node)

	var dfsClone func(*Node) *Node
	dfsClone = func(n *Node) *Node {
		if n == nil {
			return nil
		}

		if clone, ok := visited[n]; ok {
			return clone
		}

		clone := &Node{Val: n.Val}
		visited[n] = clone

		for _, nei := range n.Neighbors {
			clone.Neighbors = append(clone.Neighbors, dfsClone(nei))
		}

		return clone
	}

	return dfsClone(node)
}

// Weighted Graph Example
type Edge struct {
	Node   *Node
	Weight int
}

type WeightedNode struct {
	Val       int
	Neighbors []Edge
}

func main() {

	n1 := &Node{Val: 1}
	n2 := &Node{Val: 2}
	n3 := &Node{Val: 3}
	n4 := &Node{Val: 4}
	n5 := &Node{Val: 5}
	n6 := &Node{Val: 6}

	// Build graph
	addEdge(n1, n2)
	addEdge(n1, n3)
	addEdge(n2, n3)
	addEdge(n2, n5)
	addEdge(n5, n6)
	addEdge(n3, n6)
	addEdge(n3, n4)
	addEdge(n4, n1)

	fmt.Println("DFS:")
	dfs(n1, make(map[*Node]bool))
	fmt.Print("End\n")

	fmt.Println("\nBFS:")
	bfs(n1)
	fmt.Print("End\n")

	// Clone graph
	clone := cloneGraph(n1)
	fmt.Println("\nCloned Graph DFS:")
	dfs(clone, make(map[*Node]bool))
	fmt.Print("End\n")
}
