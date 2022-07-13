def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result