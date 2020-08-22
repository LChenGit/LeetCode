#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (46.39%)
# Likes:    1877
# Dislikes: 1463
# Total Accepted:    784.2K
# Total Submissions: 1.7M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start 方法一：str
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#             return str(x)[::-1]==str(x)
        

# @lc code=start 方法二：math
class Solution:
    def isPalindrome(self, x: int) -> bool:
            l, r = x, 0
            while l > 0:
                r = r*10+l%10
                l //=10
            return r==x
# @lc code=end

