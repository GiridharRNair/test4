class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substr = 0
        seen = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                longest_substr = max(longest_substr, len(seen))
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return longest_substr