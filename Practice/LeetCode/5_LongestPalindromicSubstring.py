'''5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """






'''bad solution w/ bad runtime
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(s == ""):
            return("")
        else:
            listing = []
            for i in range(len(s)):
                for j in range(len(s)):
                    word = s[i:j+1]
                    if(word == word[::-1] and word not in listing):
                        listing.append(word)
            return(max(listing, key=len))
'''
####################Concise Answer
# class Solution:
#     def longestPalindrome(self, s):
#         def check(l, r):
#             while 0 <= l <= r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             return s[l + 1:r]
#         pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
#         return sorted(pals, key = len)[-1] if pals else ''



####################Expand around the corners
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         self.maxLen = 0
#         self.maxStr = ''

#         def expandAroundCenter(left, right):
#             l,r=left,right
#             while(l>=0 and r<len(s) and s[l]==s[r]):
#                 l-=1
#                 r+=1
#             if r-l-1 > self.maxLen:
#                 self.maxStr = s[l+1:r]
#                 self.maxLen = r-l-1

#         for i in range(0,len(s)):
#             expandAroundCenter(i,i)
#             expandAroundCenter(i,i+1)
#         return self.maxStr

####################Manacher's Algorithm #1
# class Solution:
#     def longestPalindrome(self, s):
#         if len(s) <= 1:
#             return s
#         s_temp = "$#"+ '#'.join(list(s)) + "#&"
#         temp_len = len(s_temp)
#         P = [0 for i in range(temp_len - 1)]
#         P[0], P[1] = 1 ,1
#         mx, center = 3, 2
#         rescenter, maxlen = 1, 1
#         for i in range(2, temp_len - 1):
#             P[i] = min(P[2*center - i], mx - i) if mx > i else 1
#             while s_temp[i + P[i]] == s_temp[i - P[i]]:
#                 P[i] += 1
#             if(mx < i + P[i]):
#                 mx = i + P[i]
#                 center = i
#             if(maxlen < P[i]):
#                 rescenter = i
#                 maxlen = P[i]
#         start = int((rescenter - maxlen) / 2)
#         return s[start:start + maxlen - 1]
####################

####################Manacher's Algorithm #2
# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         T = '#'.join('^{}$'.format(s))
#         n = len(T)
#         P = [0] * n
#         C = R = 0
#         for i in range (1, n-1):
#             if i<R:
#                 P[i]=min(P[2*C - i],R-i )
#             # Attempt to expand palindrome centered at i
#             while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
#                 P[i] += 1
#             # If palindrome centered at i expand past R,
#             # adjust center based on expanded palindrome.
#             if i + P[i] > R:
#                 C, R = i, i + P[i]
#             if R == '#':
#                 break
#
#         # Find the maximum element in P.
#         maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
#         return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
# 		```
#
# 		change the last part to get 120 ms, faster than 94.87% :
# 		```
# 		        # Find the maximum element in P.
#         #maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
#         maxLen = max(P)
#         centerIndex = P.index(maxLen)
#         return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
