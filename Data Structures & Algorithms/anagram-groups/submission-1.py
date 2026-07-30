class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        letters_map = {}
        output = []
        for s in strs:
            letters = tuple(sorted(s))
            if letters not in letters_map:
                letters_map[letters] = i
                output.append([])
                i += 1
            output[letters_map.get(letters)].append(s)

        return output