class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        one, two, three = 0, 1, 1
        for _ in range(n-2):
            one, two, three = two, three, one+two+three
        return three