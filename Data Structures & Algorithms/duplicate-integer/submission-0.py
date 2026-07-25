class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for i in range(len(nums)):
            num = nums[i]
            duplicate[num] = False

        for i in range(len(nums)):
            num = nums[i]
            if not duplicate[num]:
                duplicate[num] = True
            else:
                return True
        
        return False