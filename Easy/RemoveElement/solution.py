"""
Solution file for the remove element leetcode question.
"""

def removeElement(nums:list[int], val:int)-> int:
    """
    We cannot use an external data structure. 
    The problem becomes the fact that if you remove an element, Python will not update the 
    i value to be at the same i value
    Input: nums: array of integers AND val: integer value we have to try to find and remove
    Objective: remove all of the integers in the given array that have the same value as the given 'val'
    Output: k -> the length of the list and the updated nums
    """
    working = True
    i = 0
    while(working):
        if (i == len(nums)):
            i += 1
            working = False
        elif (nums[i] == val):
            nums.pop(i)
        else:
            i += 1

    # on the Leetcode website, you only have to return the index, because of the way that the method is structured
    return i, nums
