class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for a,b in edges:
            p_a = find(a)
            p_b = find(b)
            if p_a == p_b:
                print("returning here")
                return False
            parent[p_a] = p_b
        
        return n == len(edges) + 1