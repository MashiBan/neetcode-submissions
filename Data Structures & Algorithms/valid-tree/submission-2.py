class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:   return False
        premap = {i:[] for i in range(n)}
        for no, ne in edges:
            premap[no].append(ne)
            premap[ne].append(no)

        visit = set()

        def dfs(cu, prev):
            if cu in visit:
                return False
            
            if premap[cu] == []: return True

            visit.add(cu)
            for ne in premap[cu]:
                if ne == prev:  continue
                if not dfs(ne, cu): return False
            visit.remove(cu)
            premap[cu] = []
            return True


        for i in range(n):
            if not dfs(i, -1):
                return False
        return True