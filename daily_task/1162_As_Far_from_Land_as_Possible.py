class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        addx = (0,0,-1,1)
        addy = (-1,1,0,0)

        N = len(grid)
        for row in range(N):
            for col in range(N):
                if grid[row][col]:
                    queue.append((row,col))

        if len(queue) == 0 or len(queue) == N*N:
            return -1
        
        while len(queue) != 0:
            x,y = queue.pop(0)
            for i in range(4):
                newx = x + addx[i]
                newy = y + addy[i]
                if newx < 0 or newx >= N or newy < 0 or newy >= N or grid[newx][newy] != 0:
                    continue
                grid[newx][newy] = grid[x][y] + 1
                queue.append((newx,newy))
        
        return grid[x][y] - 1
