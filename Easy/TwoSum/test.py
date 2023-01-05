"""
Simple test file to check the solution from the Two Sum File
"""

from solution import twoSum

if __name__ == "__main__":
    list_one, target_one, answer_one = [2, 7, 11, 15], 9, [1, 0]
    list_two, target_two, answer_two = [3, 2, 4], 6, [2, 1]
    list_three, target_three, answer_three = [3,3], 6, [1, 0]

    result_one = twoSum(list_one, target_one)
    result_two = twoSum(list_two, target_two)
    result_three = twoSum(list_three, target_three)
    if result_one == answer_one and result_two == answer_two and result_three == answer_three:
        print("Correct")
    else:
        print("Incorrect")
