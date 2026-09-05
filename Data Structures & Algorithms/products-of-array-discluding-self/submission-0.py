class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num
        
        for i in range(len(nums)):
            if zeroes > 1:
                nums[i] = 0
            elif zeroes == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                nums[i] = int(product / nums[i])

        return nums