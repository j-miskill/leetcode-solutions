"""
A solution file for the binary tree in order traversal
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root:TreeNode) -> list[int]:
    """
    https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    in order means left, root, right 
    typically, this is done as a recursive method (or a while loop)
    we can do it this way, too. 
    Need to stop when the curNode that we are on is None

    """


    if root == None:
        return
    
    return inorderTraversal(root.left) + root.val + inorderTraversal(root.right)

    