class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        print(count)
        for i in ransomNote:
            print(count[i])
            if i not in count.keys() or count[i] < 1: return False
            count[i] -= 1
        return True
