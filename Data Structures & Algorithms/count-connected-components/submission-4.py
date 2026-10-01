class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        visit = set()
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(node):
            for nei in adjList[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        
        res = 0
        for n in adjList:
            if n not in visit:
                visit.add(n)
                dfs(n)
                res += 1
        
        return res


