'''
Binary Tree

A binary tree is a tree data structure where each node has at most two children. 
These two children are usually referred to as the left child and right child.
'''

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left is None:
                node.left = TreeNode(val)
                return
            else:   
                queue.append(node.left)
            
            if node.right is None:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.right)
    
    # Delete (replace with deepest node)
    def delete(self, key):
        if not self.root:
            return

        q = deque([self.root])
        key_node = None
        last = None
        parent = None

        while q:
            last = q.popleft()

            if last.val == key:
                key_node = last

            if last.left:
                parent = last
                q.append(last.left)

            if last.right:
                parent = last
                q.append(last.right)

        if key_node:
            key_node.val = last.val
            self._delete_deepest(last, parent)

    def _delete_deepest(self, node, parent):
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
    
    def search(self, val):
        if self.root is None:
            return False
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.val == val:
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return False
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end = " ")
        self.inorder(root.right)
    
    def preorder(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")

    def level_order(self):
        if not self.root:
            return

        q = deque([self.root])

        while q:
            node = q.popleft()
            print(node.val, end=" ")

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        print()


bt = BinaryTree()

bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("Level Order:")
bt.level_order()

print("Preorder:")
bt.preorder(bt.root)
print()

print("Inorder:")
bt.inorder(bt.root)
print()

print("Postorder:")
bt.postorder(bt.root)
print()

print("Delete 2:")
bt.delete(2)
bt.level_order()
        
