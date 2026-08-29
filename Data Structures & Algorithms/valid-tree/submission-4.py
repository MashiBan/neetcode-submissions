class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:   return False
        premap = {i:[] for i in range(n)}
        for crs, nei in edges:
            premap[crs].append(nei)
            premap[nei].append(crs)

        visit = set()
        def dfs(crs, prev):
            if crs in visit:    return False
            if premap[crs] == []:    return True

            visit.add(crs)
            for nei in premap[crs]:
                if nei == prev: continue
                if not dfs(nei, crs):   return False
            visit.remove(crs)
            premap[crs] = []
            return True

        for i in range(n):
            if not dfs(i, -1):  return False
        return True



