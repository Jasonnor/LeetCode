# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        temp = abs(x)
        while temp:
            answer = answer * 10 + temp % 10
            temp /= 10
        if answer > 0x7FFFFFFF:
            return 0
        return answer if x >= 0 else answer * -1
