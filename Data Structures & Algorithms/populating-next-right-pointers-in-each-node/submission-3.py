"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

        queue = [root]
        level = 0
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                print("level", level_size)
                if i < level_size - 1:
                    next_node = queue[0]
                    node.next = next_node
                    print(next_node.val)
                print()
                if node and node.left is not None:
                    queue.append(node.left)
                if node and node.right is not None:
                    queue.append(node.right)

        return root
