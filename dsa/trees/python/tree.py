'''
Tree Data Structure

Tree is a non-linear data structure which is used to store data in a hierarchical manner.

Tree Data Structure is a non-linear data structure in which 
a collection of elements known as nodes
are connected to each other via edges such that 
there exists exactly one path between any two nodes.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []


'''
Tree

        1
       / \
      2   3
     / \
    4   5

Root Node: The topmost node in a tree, which does not have a parent
Parent Node: A node that has one or more child nodes
Child Node: A node that has a parent node
Leaf Node: A node that has no child nodes
Edge: A connection between two nodes
Ancestor: Any node on the path from the root to a given node (excluding the node itself)
Descendant: Any node on the path from a given node to a leaf node (excluding the node itself)
Internal Node: A node with at least one child.
Neighbor of a Node: The parent or children of a node.
Subtree:  A node and all its descendants form a subtree

Height of the Tree: The number of edges on the longest path from the root to a leaf node
Height of the Node: The number of edges on the longest path from the node to a leaf node
Depth of a Node: The number of edges on the path from the root to the node

Height of the tree = Height of the root node
Depth of the root node = 0
Hieght of a leaf node = 0

Types of trees:
1. General Tree
2. Binary Tree
    a. Full Binary Tree
    b. Complete Binary Tree
    c. Perfect Binary Tree
    
3. Binary Search Tree
4. AVL Tree
5. Red-Black Tree
6. B-Tree
7. B+ Tree
8. Trie
9. Segment Tree
10. Fenwick Tree

'''
from collections import deque

class Tree:
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    # add child to a parent node
    def add_child(self, parent, val):
        node = TreeNode(val)
        parent.children.append(node)
        return node

    # remove a node (by value)
    def remove(self, val):
        if not self.root:
            return

        if self.root.val == val:
            self.root = None
            return

        queue = deque([self.root])

        while queue:
            curr = queue.popleft()

            for child in curr.children:
                if child.val == val:
                    curr.children.remove(child)
                    return
                queue.append(child)

    # DFS traversal (recursive)
    def dfs(self, node):
        if node is None:
            return

        print(node.val, end=" ")
        for child in node.children:
            self.dfs(child)

    # BFS traversal
    def bfs(self):
        if not self.root:
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            queue.extend(node.children)

    # find node by value
    def find(self, val):
        if not self.root:
            return None

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node.val == val:
                return node
            queue.extend(node.children)

        return None

    # print tree (indented format)
    def print_tree(self, node=None, level=0):
        if self.root is None:
            print("Empty tree")
            return

        if node is None:
            node = self.root

        print("  " * level + str(node.val))
        for child in node.children:
            self.print_tree(child, level + 1)


# Example usage
tree = Tree("A")

b = tree.add_child(tree.root, "B")
c = tree.add_child(tree.root, "C")
d = tree.add_child(b, "D")
e = tree.add_child(b, "E")
f = tree.add_child(c, "F")

print("Tree structure:")
tree.print_tree()

print("\nDFS:")
tree.dfs(tree.root)

print("\nBFS:")
tree.bfs()

print("\nFind E:")
node = tree.find("E")
print(node.val if node else "Not found")

print("\nRemove B:")
tree.remove("B")
tree.print_tree()