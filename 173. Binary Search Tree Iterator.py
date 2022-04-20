class BSTIterator:

    def __init__(self, root):
        self.st = []
        self.pushLeft(root)
        
    def pushLeft(self, root):
        while root != None:
            self.st.append(root)
            root = root.left

    def next(self):
        node = self.st.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self):
        return len(self.st) > 0
