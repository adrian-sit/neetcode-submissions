class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            value = -heap[0]
            if len(heap) > 2:
                if -heap[1] > -heap[2]:
                    value2 = -heap[1]
                else:
                    value2 = -heap[2]
            else:
                value2 = -heap[1]
            if value == value2:
                heapq.heappop(heap)
                heapq.heappop(heap)
            if value2 < value:
                heapq.heappop(heap)
                heapq.heapify(heap)
                heap[0] = value2 - value
                heapq.heapify(heap)
            
        if not heap:
            return 0
        return -heap[0]