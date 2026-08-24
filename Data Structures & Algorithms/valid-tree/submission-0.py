class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
                print(f"x went from {x} to {parent[x]}")
            return x
        
        for a,b in edges:
            print("going into leader a:", a)
            leader_a = find(a)
            print("going into leader b: ", b)
            leader_b = find(b)

            parent[leader_a] = leader_b
            if leader_a == leader_b:
                return False
        
        return len(edges) == n - 1