class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0
        for i in s:
            if i == "1": ones += 1
            if i == "0": zeros += 1
        return '1' * (ones-1) + "0"*zeros + '1'