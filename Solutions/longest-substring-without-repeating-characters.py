# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        n = i = j = 0
        word_list = {}
        while i < length and j < length:
            if not (s[j] in word_list):
                word_list[s[j]] = j
                j += 1
                n = max(n, len(word_list))
            else:
                word_list.pop(s[i])
                i += 1
        return n
