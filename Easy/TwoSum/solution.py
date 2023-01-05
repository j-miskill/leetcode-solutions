"""
This is my solution to the two sum easy problem on leetcode. You can simply use a double for loop to check every number
against every other number, or you can use a dictionary to store the values you already know. 
"""

def twoSum(nums, target):
        check = {}
        
        for i in range(0, len(nums)):
            num_looking_for = target - nums[i]
            if num_looking_for in check:
                return [i, check[num_looking_for]]
            else:
                check[nums[i]] = i