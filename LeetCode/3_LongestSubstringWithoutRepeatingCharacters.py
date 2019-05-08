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

        n = len(s)      #length of word s

        diction = {}    #dictionary of letters

        i = 0           #index of last letter occurance
        j = 0           #index of letter in s

        ans = 0         #running total

        while(j < n):

            if(diction.get(s[j]) != None):          #if character already seen
                i = max( diction.get(s[j]) , i)     #bring up last occurance value


            ans = max(ans, j-i+1)       #keeps tracks of maximum running length
            diction[s[j]] = j+1         #sets my current character appearance
            j += 1

        return(ans)             #returns maximum running length





'''
"""
:type s: str
:rtype: int
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        wordlength = len(s)

        diction = {}

        i = 0
        currLetterIndex = 0

        currLongest = 0

        while(currLetterIndex < wordlength):

            #if letter has been seen
            if(diction.get(s[currLetterIndex]) != None):
                #compare dictionary value of current letter
                #to last known index of current letter
                i = max( diction.get(s[currLetterIndex]) , i)


            currLongest = max(currLongest, currLetterIndex-i+1)
            diction[s[currLetterIndex]] = currLetterIndex + 1
            currLetterIndex += 1

        return(currLongest)             #returns maximum running length

'''
