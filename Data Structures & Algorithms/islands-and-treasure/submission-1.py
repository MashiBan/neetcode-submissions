class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        def addroom(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == -1 or (i, j) in visit:
                return
            visit.add((i, j))
            q.append([i, j])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addroom(r+1, c)
                addroom(r, c+1)
                addroom(r-1, c)
                addroom(r, c-1)
            dist += 1