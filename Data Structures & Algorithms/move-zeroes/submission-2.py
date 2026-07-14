class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] != 0:
                p1+=1
                p2 += 1
            else:
                if nums[p2] != 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                else:
                    p2 += 1
        return nums
        

# [4,2,4,0,0,3,0,5]
#        p1  p2