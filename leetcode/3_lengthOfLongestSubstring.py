def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 1:
            return 1
        start = 0
        end = 1
        length = 0
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
                length = max(length, end - start)
            
            else:
                start += 1
            
        return length