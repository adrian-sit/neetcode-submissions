class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        hand = sorted(hand)
        n = len(hand)
        i = 0

        while i < n:
            for num in hand:
                if count[num] > 0:
                    x = num
                    break
            for j in range(x, x + groupSize):
                if count.get(j, 0) == 0:
                    return False 
                else:
                    count[j] -= 1
            i += groupSize

        return True



