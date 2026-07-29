class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        directions = [(0, 1), (1,0), (-1, 0), (0,-1)]
        seen = set()
        def bfs(i, j):
            if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return

            if grid[i][j] == "1":
                if (i, j) not in seen:
                    seen.add((i, j))
                else:
                    return
            for dx, dy in directions:
                bfs(i + dx, j + dy)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    count += 1
                bfs(i, j)
        return count

                    

            

            