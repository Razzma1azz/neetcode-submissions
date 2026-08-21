class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            word = str(len(s)) + "#" + s
            encoded.append(word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = i

        while i < len(s):

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
            j = i
        
        return decoded



        


