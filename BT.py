class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)


a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)

a.left=b
a.right=c
b.left=d
b.right=e

print(a)
