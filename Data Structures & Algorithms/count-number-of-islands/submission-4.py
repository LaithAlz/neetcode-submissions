class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return
            if grid[i][j] == '0' or (i,j) in visited:
                return
            visited.add((i,j))
            for dx, dy in directions:
                bfs(i + dx, j + dy)
            return True
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if bfs(i, j):
                    count += 1
        return count
                
            
