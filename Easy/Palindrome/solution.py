"""
This is my actual solution to the "Palindrome Number" question on Leetcode.
"""

def isPalindrome(x):
        forward = str(x)
        backward = ""
        for character in forward:
            backward = character + backward


        return forward == backward