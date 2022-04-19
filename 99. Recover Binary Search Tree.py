def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops = root, TreeNode(float('-inf')), []
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur: temp = temp.right
                if not temp.right:
                    temp.right, cur = cur, cur.left
                    continue
                temp.right = None
            if cur.val < prev.val: drops.append((prev, cur))
            prev, cur = cur, cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val