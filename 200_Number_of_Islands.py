class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def __init__(self):
        self.length = 0
        self.width = 0
        self.grid = [[]]
    
    def numIslands(self, grid):
        if grid==[]:
            return 0
        self.grid = grid
        self.width = len(grid)
        self.length = len(grid[0])
        i,j = 0,0
        ans = 0
        for i in range(0, self.width):
            for j in range(0, self.length):
                if self.grid[i][j] == '1':
                    self.bfs(i,j)
                    ans += 1
        return ans

    def bfs(self,i,j):
        arr = []
        arr.append([i,j])
        while len(arr)>0:
           cur_pos = arr.pop(0)
           i = cur_pos[0]
           j = cur_pos[1]
           self.grid[i][j] = '0'
           if (j + 1 < self.length) and (self.grid[i][j+1] == '1'):
               arr.append([i,j+1])
               self.grid[i][j+1] = '2'
           if (i + 1 < self.width) and (self.grid[i+1][j] == '1'):
               arr.append([i+1,j])
               self.grid[i+1][j] = '2'
           if (j - 1 >= 0) and (self.grid[i][j-1] == '1'):
               arr.append([i,j-1])
               self.grid[i][j-1] = '2'
           if (i - 1 >= 0) and (self.grid[i-1][j] == '1'):
               arr.append([i-1,j])
               self.grid[i-1][j] = '2'
