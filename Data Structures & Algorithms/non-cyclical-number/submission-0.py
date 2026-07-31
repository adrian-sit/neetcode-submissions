class Solution:
    def isHappy(self, n: int) -> bool:
        count = {}
        while True:
            square_sum = 0
            while n != 0:
                m = n - (n // 10) * 10
                n //= 10
                square_sum += m ** 2
            if square_sum == 1:
                return True
            count[square_sum] = count.get(square_sum, 0) + 1
            if count[square_sum] == 2:
                return False
            n = square_sum
