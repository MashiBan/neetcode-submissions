class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = double = 0
        n = len(grid)
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])
        
        for num in range(1, n*n+1):
            if num not in seen:
                missing = num
                break
        
        return [double, missing]