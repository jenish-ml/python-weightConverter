class treeNode:
    def __init__(self, data, leftNode = None, rightNode = None):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode

root = treeNode(1)
root.leftNode = treeNode(2)
root.rightNode = treeNode(3)

print(root.data)
print(root.leftNode.data)
print(root.rightNode.data)