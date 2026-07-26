class Solution:
    def search(self, nums: List[int], target: int) -> int:
        removedfront = 0
        while len(nums) > 0:
            mid = len(nums) // 2
            print(mid)
            if target < nums[mid]:
                nums = nums[:mid]
            elif target > nums[mid]:
                if len(nums) == 1:
                    return -1
                nums = nums[mid:]
                removedfront += len(nums[:mid])
            else:
                return mid + removedfront

        return -1