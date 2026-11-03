class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = 0
        sum_it = 0
        for num in nums:
            sum_it += num
            if sum_it < 0:
                sum_it = 0
            maxsum = max(sum_it, maxsum)
        if maxsum == 0:
            maxsum = -10000
            for num in nums:
                maxsum = max(maxsum, num)

        return maxsum