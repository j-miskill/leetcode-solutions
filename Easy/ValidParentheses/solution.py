"""
valid Parentheses solution
"""

def isValid(s:str)->bool:
    """
    Return true if all open brackets are closed by the corresponding close brackets and all are closed in the same order"
    """
    open_pairings = {
                "(": ")",
                "{": "}",
                "[": "]"
                }
    close_pairings = {
                    ")": "(",
                    "}": "{",
                    "]": "["
                    }

    open_queue = []
    for character in s:
        if character in open_pairings:
            open_queue.append(character)
        elif character in close_pairings:
            if len(open_queue) == 0:
                return False
            top = open_queue.pop()
            if open_pairings[top] != character:
                return False
        else:
            return False
    
    if len(open_queue) != 0:
        return False
    else:
        return True
