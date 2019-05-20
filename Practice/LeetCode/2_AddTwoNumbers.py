'''2. Add Two Number
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        newlist = head = ListNode(0)

        while(l1 or l2 or carry): #while number/list still exists
            v1 = 0
            v2 = 0
            if (l1 != None):
                v1 = l1.val
                l1 = l1.next

            if (l2 != None):
                v2 = l2.val
                l2 = l2.next

            curval = v1 + v2 + carry

            if ( curval >= 10):
                carry = 1
                curval = curval - 10
            else:
                carry = 0

            newlist.next = ListNode(curval)

            newlist = newlist.next

        return(head.next)
