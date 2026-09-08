class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        min_index = math.ceil(r / 2)

        while True:
            if nums[l] < nums[min_index]:
                l = min_index
                min_index = math.ceil((l + r) / 2)
            if nums[r] > nums[min_index]:
                r = min_index
                min_index = math.ceil((l + r) / 2)
            if l == r:
                min_index = 0
            if min_index == 0:
                return nums[min_index]
            if nums[min_index] < nums[min_index - 1]:
                return nums[min_index]          
