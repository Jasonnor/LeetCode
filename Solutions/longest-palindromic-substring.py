# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# Example:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Example:
# 
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
        	return ""
        start = 0
        end = 1
        for i in xrange(len(s)):
        	if i - end >= 1 and s[i - end - 1:i + 1] == s[i - end - 1:i + 1][::-1]:
        		start = i - end - 1
        		end += 2
        	elif i - end >= 0 and s[i - end:i + 1] == s[i - end:i + 1][::-1]:
        		start = i - end
        		end += 1
        return s[start:start + end]
