"""
This is the test file for the Roman to Integer Leetcode solution that I created!
"""
from solution import romanToInt


if __name__ == "__main__":
    string_one, answer_one = "III", 3
    string_two, answer_two = "LVIII", 58
    string_three, answer_three = "MCMXCIV", 1994

    result_one = romanToInt(string_one)
    result_two = romanToInt(string_two)
    result_three = romanToInt(string_three)

    if result_one == answer_one and result_two == answer_two and result_three == answer_three:
        print("Correct")
    else:
        print("Incorrect")
