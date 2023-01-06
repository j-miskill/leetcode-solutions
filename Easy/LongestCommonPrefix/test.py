"""
Test file for the longest common prefix code. 
"""

from solution import longest_common_prefix

if __name__ == "__main__":

    list_one, answer_one = ["flower", "flow", "flight"], "fl"
    list_two, answer_two = ["dog", "racecar", "car"], ""
    list_three, answer_three = [""], ""
    list_four, answer_four = [], ""
    list_five, answer_five = ["detail", "determine", "eggs"], ""
    list_six, answer_six = ["benefit", "beneficiary", "benefits", "benedict", "beneights"], "bene"
    list_seven, answer_seven = ["ab", "a"], "a"
    list_eight, answer_eight = ["flower", "flower", "flower", "flower"], "flower"

    
    # result_one = longest_common_prefix(list_one)
    # result_two = longest_common_prefix(list_two)
    # result_three = longest_common_prefix(list_three)
    # result_four = longest_common_prefix(list_four)
    # result_five = longest_common_prefix(list_five)
    # result_six = longest_common_prefix(list_six)
    # result_seven = longest_common_prefix(list_seven)
    
    result_eight = longest_common_prefix(list_eight)

    # print("Result one", result_one)
    # print("Result two", result_two)
    # print("Result three",  result_three)
    # print("Result four", result_four)
    # print("Result five",  result_five)
    # print("Result six", result_six)
    # print("Result seven", result_seven)
    print("Result eight", result_eight)


