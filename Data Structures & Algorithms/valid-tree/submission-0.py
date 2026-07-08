class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        premap = {i:[] for i in range(n)}
        for e, ne in edges:
            premap[e].append(ne)
            premap[ne].append(e)
        visit = set()

        def dfs(e, parent):
            if e in visit:  return False
            if premap[e] == []: return True

            visit.add(e)
            for ne in premap[e]:
                if ne == parent: continue
                if not dfs(ne, e):  return False
            visit.remove(e)
            premap[e] = []
            return True
            

        for i in range(n):
            if not dfs(i, -1):  return False
        return True