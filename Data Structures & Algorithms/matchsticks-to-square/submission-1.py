class Solution:
    def makesquare(self, match: List[int]) -> bool:
        length = sum(match)//4
        match.sort(reverse=True)
        if sum(match)/4 != length:  return False
        side = [0]*4

        def backtrack(i):
            if i == len(match):
                return True
            
            for j in range(4):
                if side[j] + match[i] <= length:
                    side[j] += match[i]
                    if backtrack(i+1):  return True
                    side[j] -= match[i]
            return False
        return backtrack(0)
