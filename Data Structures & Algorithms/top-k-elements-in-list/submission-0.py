class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_nums = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        topk = list(sorted_nums.items())[:k]
        output = []
        for num, counts in topk:
            output.append(num)

        return output
