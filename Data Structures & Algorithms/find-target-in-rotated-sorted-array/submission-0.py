class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

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
                break
            if nums[min_index] < nums[min_index - 1]:
                break

        if target == nums[min_index]:
            return min_index
        elif target == nums[n - 1]:
            return n - 1
        elif target == nums[0]:
            return 0
        elif target > nums[min_index] and target < nums[n - 1]:
            l, r = min_index + 1, n - 2
        else:
            l, r = 1, min_index - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
            
