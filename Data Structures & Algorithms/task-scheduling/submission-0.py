class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        heap = []
        time = 0
        queue = deque()

        for task, frequency in counts.items():
            heapq.heappush(heap, (-frequency, task))

        while heap or queue:
            time += 1

            if queue and queue[0][0] == time:
                available_time, frequency, task = queue.popleft()
                heapq.heappush(heap, (frequency, task))

            if heap:
                frequency, task = heapq.heappop(heap)
                frequency += 1
                if frequency != 0:
                    queue.append((time + n + 1, frequency, task))

        return time
        