"""
A test file for the binary tree in order traversal.
"""
from solution import inorderTraversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # create initial nodes
    test_node_one = TreeNode(val=1)
    test_node_two = TreeNode(val=2)
    test_node_three = TreeNode(val=3)
    test_node_four = TreeNode(val = 4)

    # assigning left and right values to the nodes
    test_node_one.left = None
    test_node_one.right = test_node_two
    test_node_two.left = test_node_three
    test_node_two.right = None
    test_node_three.left = None
    test_node_three.right = None
    test_node_four.left = None
    test_node_four.right = None

    # testing
    result_one = inorderTraversal(test_node_one)
    result_two = inorderTraversal(None)
    result_three = inorderTraversal(test_node_four)

    print("Result one:", result_one)
    print("Result two:", result_two)
    print("Result three:", result_three)
