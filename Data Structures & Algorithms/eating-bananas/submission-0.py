class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        if len(piles) == 1:
            return (piles[0] + h - 1) // h # ceiling of (i/h)
        while True:
            k = (high + low) // 2
            hours = 0
            hours_diff = 0
            for i in piles:
                hours += (i + k - 1) // k  # ceiling of (i/k)
                hours_diff += (i + k - 2) // (k - 1) # ceiling of (i/(k-1))
            if hours <= h and hours_diff > h:
                return k
            if hours <= h:
                high = k
            else:
                low = k + 1
                