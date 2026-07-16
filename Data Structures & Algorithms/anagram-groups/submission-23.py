class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in ordered:
                ordered[key] = []
            ordered[key].append(word)
        return list(ordered.values())