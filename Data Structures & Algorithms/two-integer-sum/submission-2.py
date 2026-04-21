class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in nums and nums.index(sec) != i:
                return sorted([i, nums.index(sec)])
        return [0,0]