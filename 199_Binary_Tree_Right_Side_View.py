# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []
        arr = []
        ans = []
        layer = []
        arr.append(root)
        arr.append(None)
        while True:
            #print("kkk",layer)
            #print(arr)
            head = arr.pop(0)
            if head is None:
                if len(arr) == 0:
                    ans.append(layer)
                    break
                else:
                    ans.append(layer)
                    layer = []
                    arr.append(None)
            else:
                layer.append(head.val)
                if head.left is not None:
                    arr.append(head.left)
                if head.right is not None:
                    arr.append(head.right)
        re = []
        for layer in ans:
            re.append(layer[-1])
        return re
        
