class Solution:
    def isValid(self, s: str) -> bool:
        chars = ""
        for c in s:
            chars += c
            if len(chars) > 1:
                prev_char = chars[len(chars)-2]
                if (c == ")" and prev_char == "(") or (c == "}" and prev_char == "{") or (c == "]" and prev_char == "["):
                    chars = chars[:-2]
        
        return len(chars) == 0

        