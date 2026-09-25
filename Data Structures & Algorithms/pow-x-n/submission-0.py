class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(n)
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n // 2), 2)
        else:
            return self.myPow(self.myPow(x, n // 2), 2) * x
