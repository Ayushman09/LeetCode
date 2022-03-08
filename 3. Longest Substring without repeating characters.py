#Sliding Window approach
def lengthOfLongestSubstring(s: str) -> int:
        start = longest = 0
        seen = {}
        for end in range(len(s)):
            letter = s[end]
            if letter in seen:
                start = max(seen[letter] + 1, start)
            longest = max(longest, end - start + 1)
            seen[letter] = end
        
        return longest