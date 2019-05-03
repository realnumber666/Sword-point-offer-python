class Solution:
    def __init__(self):
            self.headNode = None
            self.preNode = None
    def Convert(self, pRootOfTree):
        # write code here
        def tranv(node):
            if (node):
                tranv(node.left)
                if not (self.preNode):
                    self.preNode = node
                    self.headNode = self.preNode
                else:
                    self.preNode.right = node
                    node.left = self.preNode
                    self.preNode = node
                tranv(node.right)
        # headNode = None
        # global preNode = None
        tranv(pRootOfTree)
        return self.headNode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

print Solution().Convert(TreeNode(1)).val