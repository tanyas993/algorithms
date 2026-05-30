"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        vis = {}

        def dfs(n):
            if n in vis:
                return vis[n]
            clone = Node(n.val)
            vis[n] = clone
            for n in n.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)