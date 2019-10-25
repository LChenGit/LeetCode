/*
 * @lc app=leetcode id=925 lang=cpp
 *
 * [925] Long Pressed Name
 *
 * https://leetcode.com/problems/long-pressed-name/description/
 *
 * algorithms
 * Easy (44.44%)
 * Likes:    305
 * Dislikes: 40
 * Total Accepted:    22.9K
 * Total Submissions: 51.5K
 * Testcase Example:  '"alex"\n"aaleex"'
 *
 * Your friend is typing his name into a keyboard.  Sometimes, when typing a
 * character c, the key might get long pressed, and the character will be typed
 * 1 or more times.
 * 
 * You examine the typed characters of the keyboard.  Return True if it is
 * possible that it was your friends name, with some characters (possibly none)
 * being long pressed.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: name = "alex", typed = "aaleex"
 * Output: true
 * Explanation: 'a' and 'e' in 'alex' were long pressed.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: name = "saeed", typed = "ssaaedd"
 * Output: false
 * Explanation: 'e' must have been pressed twice, but it wasn't in the typed
 * output.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: name = "leelee", typed = "lleeelee"
 * Output: true
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: name = "laiden", typed = "laiden"
 * Output: true
 * Explanation: It's not necessary to long press any character.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * name.length <= 1000
 * typed.length <= 1000
 * The characters of name and typed are lowercase letters.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
#include <stdio.h>
#include <iostream>
using namespace std;
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        if (name.compare(typed) > 0 || (name[0]!= typed[0])){
            return false;
        }
        if (name.compare(typed) == 0){
            return true;
        }

        int i = 0, m = name.length(), n = typed.length();
        for (unsigned int j = 0; j < n; j++){
            if (i < m and name[j] == typed[j])
                ++i;
            else if ( j == 0 or typed[j] != typed[j-1])
                return false;
        }

        return i == m;
    }
};

// int main()
// {
//     Solution sol;
//     string s1 = "alex";
//     string s2 = "aalex";
//     if (sol.isLongPressedName(s1, s2) == true){
//         printf("true\n");
//     }else printf("false\n");
// }
// @lc code=end

