class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addCell(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                visit.add((r,c))
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r,c-1)
                addCell(r-1,c)
            dist += 1
