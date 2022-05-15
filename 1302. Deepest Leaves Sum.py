def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=[root]
        res=[]
        while q:
            ans=[]
            l=len(q)
            for i in range(l):
                node=q.pop(0)
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        return sum(res[-1])