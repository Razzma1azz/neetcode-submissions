class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: clean the string — keep only letters/numbers, make it lowercase
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        # Step 2: two-pointer check on the cleaned string
        start = 0
        end = len(cleaned) - 1
        while start < end and cleaned[start] == cleaned[end]:
            start += 1
            end -= 1

        return start >= end