#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.62%)
# Likes:    2791
# Dislikes: 4370
# Total Accepted:    931.7K
# Total Submissions: 3.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start 方法一：str
# class Solution:
#     def reverse(self, x: int) -> int:
#         sol = lambda x: x if x in range (-2**31-1,2**31) else 0
#         if (x in range (-2**31-1,2**31)):
#             if (x < 0):                
#                 return sol(-int(str(x)[:0:-1]))
#             else:
#                 return sol(int(str(x)[::-1]))
#         else:
#             return 0

# @lc code=start 方法二：math
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        inrange = lambda x: x if x in range (-2**31-1,2**31) else 0
        if inrange(x)==0:
            return 0
        else:
            ans = 0
            x = abs(x)
            while(x):
                ans = ans*10+x%10
                x=x//10
            return inrange(ans)*sign

        
# @lc code=end

