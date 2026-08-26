class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                # parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        last_edge = []
        for a, b in edges:
            p_a = find(a)
            p_b = find(b)

            if p_a == p_b:
                last_edge = [a, b]
            
            parent[p_a] = p_b
        print(parent)
        return last_edge