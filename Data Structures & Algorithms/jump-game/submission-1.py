class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums[n - 1] = -1
        for i in range(n - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump < n and nums[i + jump] == -1:
                    nums[i] = -1
                    break


        return nums[0] == -1