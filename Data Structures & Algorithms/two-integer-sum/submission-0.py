class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_j = {}
        for i in range(len(nums)):
            i_num = nums[i]
            if i_num in find_j:
                return [find_j.get(i_num), i]
            j_num = target - i_num
            find_j[j_num] = i
        