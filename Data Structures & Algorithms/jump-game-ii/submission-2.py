class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        nums[n - 1] = 0
        for i in range(n - 2, -1, -1):
            maxjump = nums[i]
            minjump = 1001
            for jump in range(maxjump):
                jumpto = i + jump + 1
                if jumpto < n:
                    if nums[jumpto] < minjump:
                        minjump = nums[jumpto]
            nums[i] = minjump + 1

        return nums[0]