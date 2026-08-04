class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_index = len(digits)
        increment = True

        while increment:
            digit_index -= 1
            if digit_index == -1:
                digits.insert(0, 1)
                break
            digits[digit_index] += 1
            if digits[digit_index] == 10:
                digits[digit_index] = 0
            else:
                increment = False

        return digits
            
    
                
