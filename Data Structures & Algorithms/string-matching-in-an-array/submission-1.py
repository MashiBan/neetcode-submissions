class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        mapi = {}
        for i in words:
            for j in words:
                if i != j and i in j and i not in res:
                    res.append(i)

        return res
