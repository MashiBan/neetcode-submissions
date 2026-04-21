class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     sec = target - nums[i]
        #     if sec in nums and nums.index(sec) != i:
        #         return sorted([i, nums.index(sec)])
        # return [0,0]
        dict = {}
        for index, value in enumerate(nums):
            sec = target-value
            if sec in dict and dict[sec] != index:
                return sorted([index, dict[sec]])
            dict[value] = index
        return [0, 0]