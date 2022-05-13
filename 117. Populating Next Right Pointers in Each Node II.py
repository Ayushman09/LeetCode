def connect(self, root: 'Node') -> 'Node':
        prev = tail = None
        node = root
        
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
                if not(tail):
                    tail = prev
                
            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
                if not(tail):
                    tail = prev
                
            node = node.next
            if not node:
                node = tail
                prev = tail = None
                
        return root