"""
Solution code for the Longest common prefix question
"""

def longest_common_prefix(strs: list[str])-> str:
    # include checks at the beginning
    if len(strs) == 0:
        return ""
    if strs[0] == "":
        return ""

    valid_prefix = True
    checking_index = 0
    checking_character = ""
    longest_prefix = ""
    word_index = 0

    while(valid_prefix):
        if checking_index >= len(strs[0]):
            valid_prefix = False
            print("Break 3")
            break

        checking_character = strs[0][checking_index]
        print("Checking character is", checking_character)

        for s in strs:
            print("Word: ", s)
            if s == "" or checking_index >= len(s):
                valid_prefix = False
                print("Break 1")
                break
            elif s[checking_index] != checking_character:
                valid_prefix = False
                print(s[checking_index])
                print("Break 2")
                break
            elif word_index == len(strs) - 1 and s[checking_index] == checking_character:
                checking_index += 1
                word_index = 0
                longest_prefix = longest_prefix + checking_character
            else:
                word_index += 1
                continue

    return longest_prefix
                
