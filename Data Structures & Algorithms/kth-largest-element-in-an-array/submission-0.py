class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-i for i in nums]
        heapq.heapify(heap)

        for i in range(k):
            value = -heapq.heappop(heap)

        return value

