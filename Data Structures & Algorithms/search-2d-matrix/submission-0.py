class Solution:

    def binarySearchList(self, nums: List[int], target: int) -> bool:
        while len(nums) > 0:
            mid = len(nums) // 2
            if target < nums[mid]:
                nums = nums[:mid]
            elif target > nums[mid]:
                if len(nums) == 1:
                    return False
                nums = nums[mid:]
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        while len(matrix) > 0:
            # Regular binary search if only 1 row
            if len(matrix) == 1:
                return self.binarySearchList(matrix[0], target)
            # Else matrix binary search
            mid = len(matrix) // 2
            if target < matrix[mid][0]:
                matrix = matrix[:mid]
            elif target > matrix[mid][0]:
                # Regular binary search if 2 rows left passing through larger row
                if len(matrix) == 2:
                    return self.binarySearchList(matrix[1], target)
                # Regular binary search if found the row
                if target < matrix[mid+1][0]:
                    return self.binarySearchList(matrix[mid], target)
                else:
                    matrix = matrix[mid:]
            else:
                return True

        return False
