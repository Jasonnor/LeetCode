# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 1:
            return self.find_kth(A, B, length // 2)
        else:
            return (self.find_kth(A, B, length // 2) + self.find_kth(A, B, length // 2 - 1)) / 2.   
        
    def find_kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
        
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.find_kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.find_kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.find_kth(a[:ia], b, k)
            else:
                return self.find_kth(a, b[:ib], k)
