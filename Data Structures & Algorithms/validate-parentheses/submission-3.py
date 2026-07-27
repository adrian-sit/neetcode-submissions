class Solution:
    def isValid(self, s: str) -> bool:
        chars = ""
        for c in s:
            if len(chars) > 0:
                prev_char = chars[len(chars)-1]
                if (c == ")" and prev_char == "(") or (c == "}" and prev_char == "{") or (c == "]" and prev_char == "["):
                    chars = chars[:-1]
                else:
                    chars += c
            else:
                chars += c

        return chars == ""
    
