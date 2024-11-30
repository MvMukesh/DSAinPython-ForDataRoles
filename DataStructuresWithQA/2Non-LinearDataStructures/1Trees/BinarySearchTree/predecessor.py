"""
Author: https://www.linkedin.com/in/mukesh-manral/
"""

def predecessor(root, node):
    pred = None
    while root:
        if node.val > root.val:
            pred = root
            root = root.right
        else:
            root = root.left
    return pred
