#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.73%)
# Likes:    1030
# Dislikes: 1666
# Total Accepted:    469K
# Total Submissions: 1.4M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start 牛顿迭代法
class Solution0:
    def mySqrt(self, x: int) -> int:
        r=x
        while (r**2>x):
            r = (r+x//r)//2
        return r

# @lc code=start 牛顿迭代法 二分法 ``r*r<x`` ``(r+1)*(r+1)>x``
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x < 2:
            return x
        while (low < high):
            mid = low +(high-low)//2 # 防溢出
            if(mid*mid <= x and (mid+1)**2>x):
                return mid
            else:
                if (mid*mid >x):
                    high = mid - 1
                else:
                    low = mid + 1
        return low
# @lc code=end

