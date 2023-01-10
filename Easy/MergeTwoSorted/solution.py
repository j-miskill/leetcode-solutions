"""
the test file for merge two sorted lists

Problem: we are given the heads of two sorted linked lists. Merge the lists into one sorted list
and return the head of the sorted list

1) definition: input: two sorted linked lists
               output: the head node of the fully sorted list (meaning we need to create a head node and point to the first node we decide on)
               thoughts: definitely need a loop. We need to update the .next fields that each listnode has and point a blank head node at the initial node 
                         we decide on. Obviously the logic should look at the current node for each of the lists and then whichever is smaller will be the next node.
                         So, we will need a curNode for each list (but we can just use the listnode that they give us). We need to include something for when we get to the end where only one list has a value and 
                         the other list is empty.
2) constraints: each list is already sorted, so we don't need to percolate down or anything like that. 
                we only need to update the .next values for each of the nodes.
                is both lists are empty/one is empty, return only the other list 9should automatically happen based on logic we use.
                node.val is a number between -100 and 100.
                the lists are sorted in ascending order (ie 1,2,3,4 not 4,3,2,1)

3) approach: use a while loop and the listnodes provided and a curNode. The curNode will represent the place we are at in the newly sorted list. Each iteration we
             will choose a node to add to the curNode.next value and then iterate the ListNode to it's next value. We will have something at the very end that will
             check if one of the listnodes is not null and add that final value or values to the list (so another while loop)
4) algorithm: will write out below
5) run-time/analysis: should be O(n) because we look at every node exactly one time. 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
    head = curNode = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            curNode.next = list1
            list1 = list1.next
            curNode = curNode.next
        elif list2.val < list1.val:
            curNode.next = list2
            list2 = list2.next
            curNode = curNode.next
        else:
            curNode.next = list1
            list1 = list1.next
            curNode = curNode.next

    
    while list1 or list2:
        if list1:
            curNode.next = list1
            list1 = list1.next
            curNode = curNode.next
        else:
            curNode.next = list2
            list2 = list2.next
            curNode = curNode.next

    return head.next
