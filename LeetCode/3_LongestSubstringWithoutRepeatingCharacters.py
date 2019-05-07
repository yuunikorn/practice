'''3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

"""
:type s: str
:rtype: int
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):


        #solution 2

        n = len(s)
        diction = {}
        ans = 0

        i = 0
        j = 0

        while(j < n):
            if(diction.get(s[j]) != None):
                i = max( diction.get(s[j]) , i)
            ans = max(ans, j-i+1)
            diction[s[j]] = j+1
            j += 1

        return(ans)
