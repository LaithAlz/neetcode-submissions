class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        last_edge = []
        for a, b in edges:
            edge_a = find(a)
            edge_b = find(b)
            if edge_a == edge_b:
                last_edge = [a,b]
            
            parent[edge_a] = edge_b
        
        return last_edge