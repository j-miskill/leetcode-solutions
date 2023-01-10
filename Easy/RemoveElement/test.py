"""
Test file for the remove element method that I am writing right now.
"""

from solution import removeElement

if __name__ == "__main__":
    test_nums_one, val_one, answer_one = [3,2,2,3], 3, [2,2]
    test_nums_two, val_two, answer_two = [0,1,2,2,3,0,4,2], 2, [0,1,4,0,3]

    result_one = removeElement(test_nums_one, val_one)
    result_two = removeElement(test_nums_two, val_two)

    print("Result one", result_one)
    print("Result two", result_two)
    