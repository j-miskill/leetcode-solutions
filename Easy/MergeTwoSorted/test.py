"""
test file for the merge two sorted linked-lists
"""

from syslog import LOG_LOCAL7
from solution import mergeTwoLists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    l1 = ListNode(val=1)
    l2 = ListNode(val=2)
    l3 = ListNode(val=3)
    l4 = ListNode(val=4)

    l1.next = l3
    l2.next = l4

    result_one = mergeTwoLists(l1, l2)
    print("HERE")
    input()
    while result_one:
        print(result_one.val)
        result_one = result_one.next
    print("HERE")
    input()
    l5 = None
    l6 = ListNode()
    result_two = mergeTwoLists(l5, l6) 
    while result_two:
        print(result_two.val)
        result_two = result_two.next

