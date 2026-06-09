"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copy = {}
        copy[node] = Node(node.val)
        
        q = deque()
        
        
        q.append(node)
        while q:
            old_node = q.popleft()
            for old_neighbor in old_node.neighbors:
                if old_neighbor not in copy:
                    copy[old_neighbor] = Node(old_neighbor.val)
                    q.append(old_neighbor)
                copy[old_node].neighbors.append(copy[old_neighbor])
                
            
        return copy[node]
    

        
        