"""
This is my test file to the "Palindrome Number" leetcode question. 
"""

from solution import isPalindrome

if __name__ == "__main__":

    num_one, answer_one = 121, True
    num_two, answer_two = -121, False
    num_three, answer_three = 10, False

    result_one = isPalindrome(num_one)
    result_two = isPalindrome(num_two)
    result_three = isPalindrome(num_three)

    if result_one == answer_one and result_two == answer_two and result_three == answer_three:
        print("Correct")
    else:
        print("Incorrect")
