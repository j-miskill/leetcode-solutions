"""
Test file for valid parentheses.
"""
from solution import isValid

if __name__ == "__main__":

    string_one, answer_one = "()", True
    string_two, answer_two = "()[]{}", True
    string_three, answer_three = "(]", False

    result_one = isValid(string_one)
    result_two = isValid(string_two)
    result_three = isValid(string_three)

    print("Result One: ", result_one)
    print("Result two: ", result_two)
    print("Result three", result_three)