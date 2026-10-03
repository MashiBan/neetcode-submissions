class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()

        def dfs(node):
            for nei in adjList[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        count = 0

        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                count += 1
        return count