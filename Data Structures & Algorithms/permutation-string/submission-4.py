class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            while l < len(s2):
                if s2[l] in count:
                    break
                l += 1
            if r - l + 1 < len(s1):
                continue
            test_count = count.copy()
            for i in range(r - l + 1):
                c = s2[i + l]
                if c not in count:
                    break
                test_count[c] -= 1
                if test_count[c] < 0:
                    break
                if i == r - l:
                    return True
            l += 1
        
        return False
            
        