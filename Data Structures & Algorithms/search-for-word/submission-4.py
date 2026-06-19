class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()
        
        def bfs(i, j, k):
            if i >= len(board) or j >= len(board[0]) or k >= len(word):
                return False
            
            if i < 0 or j < 0:
                return False
            if (i, j) in visited:
                return False

            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True
            visited.add((i,j))
            for dx, dy in directions:
                if bfs(i+dx, j+dy, k+1):
                    visited.remove((i,j))
                    return True
            visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(f"we recurse at {i} {j}, word: {board[i][j]}")
                if bfs(i, j, 0):
                    return True
        
        return False

